"""Bounded security evaluation of committed events, independent of session age.

One page per wake; no filesystem reads or network activity under the writer
lock. The cursor follows ingestion rather than the source event timestamp.
"""
from __future__ import annotations

import json
import logging
import os
import threading
import time
from collections import defaultdict

log = logging.getLogger(__name__)
CURSOR_KEY = "guard.security.cursor"
STATUS_KEY = "guard.security.status"
PAGE_SIZE = 128
CHUNK_SIZE = 64
INITIAL_LOOKBACK_MS = 300_000
_WAKE = threading.Event()
_START_LOCK = threading.Lock()
_THREAD = None


def notify_commit():
    """Coalesce a batch into one wakeup. Safe inside the flush critical section."""
    _WAKE.set()


def _runtime(row):
    from clawmetry.local_store import _NON_OPENCLAW_RUNTIME_PREFIXES
    prefix = str(row.get("session_id") or "").split(":", 1)[0]
    if prefix in _NON_OPENCLAW_RUNTIME_PREFIXES:
        return prefix
    value = str(row.get("agent_type") or "")
    return "openclaw" if value in ("", "main", "subagent", "cron") else value


def _cursor(settings, now_ms):
    raw = settings.get(CURSOR_KEY)
    if raw is None:
        return None, None
    obj = json.loads(raw)
    if (obj.get("version") != 2 or type(obj.get("position")) is not int
            or not isinstance(obj.get("epoch"), str)):
        raise ValueError("Invalid security cursor; evidence inspection needs repair")
    return obj["position"], obj["epoch"]


def _deliver(store, incident):
    from clawmetry.incident_alerts import deliver_incident
    return deliver_incident(store, incident)


def _policy(store, incidents, row):
    incidents = [inc for inc in incidents if inc.get("incident_state") == "active"
                 and inc.get("kind") != "inspection_incomplete"
                 and (inc.get("evidence") or {}).get("policy_eligible") is not False]
    if not incidents:
        return
    if not row or row.get("ended_at") or str(row.get("status") or "").lower() in (
            "ended", "completed", "stopped", "failed"):
        return
    from clawmetry import otlp_guard, sync
    if otlp_guard.observe_only_runtime(row):
        return
    state = {}
    facts = sync._detector_session_facts([row], state, time.time(), store=store)
    sid = row["session_id"]
    first = min((inc.get("first_seen_ms") or time.time() * 1000) for inc in incidents)
    facts[sid]["bad_for_seconds"] = max(0.0, time.time() - first / 1000)
    sync._apply_guard_policies(
        store, state, incidents, facts, strict=True,
        deliver_alert=lambda incident, policy_id, decision: store.enqueue_security_notification(
            incident=incident, policy_id=policy_id))


def process_batch(store, *, now=None, limit=PAGE_SIZE, deliver=None, apply_policies=None):
    """Handle one page. A failed write leaves its cursor unchanged for retry."""
    from clawmetry import detectors, guard_checks
    from clawmetry.detector_money import SECURITY_KINDS
    now_ms = int((time.time() if now is None else now) * 1000)
    settings = store.query_security_settings()
    position, epoch = _cursor(settings, now_ms)
    if any(os.environ.get(key, "1") == "0" for key in
           ("CLAWMETRY_DETECTORS", "CLAWMETRY_STUCK_DETECT")):
        return {"processed": 0, "findings": 0, "status": "disabled"}
    journal = store.query_security_changes(
        position=position, epoch=epoch, limit=max(1, min(PAGE_SIZE, int(limit))),
        bootstrap_after=max(0, now_ms - INITIAL_LOOKBACK_MS))
    page = journal["rows"]
    if not page and not journal["history_gap"]:
        return {"processed": 0, "findings": 0, "status": "idle"}
    groups = defaultdict(list)
    skipped = 0
    for row in page:
        key = (str(row.get("node_id") or ""), _runtime(row), str(row.get("session_id") or ""))
        if all(key):
            groups[key].append(row)
        else:
            skipped += 1
    disabled = guard_checks.disabled_kinds(settings)
    selected = SECURITY_KINDS.intersection(detectors.DETECTOR_KINDS)
    excluded = set(detectors.DETECTOR_KINDS).difference(selected) | disabled
    count = 0
    limitations = 0
    baselines = {}
    deliver = (lambda incident: store.enqueue_security_notification(incident=incident)) if deliver is None else deliver
    apply_policies = _policy if apply_policies is None else apply_policies
    for (node_id, runtime, sid), rows in groups.items():
        session = store.query_security_session(session_id=sid, node_id=node_id, runtime=runtime)
        facts = {"cwd": (session or {}).get("cwd") or ""}
        if runtime not in baselines:
            baselines[runtime] = store.query_guard_baseline("runtime:" + runtime) or {}
        baseline = baselines[runtime]
        for offset in range(0, len(rows), CHUNK_SIZE):
            chunk = rows[offset:offset + CHUNK_SIZE]
            anchor = chunk[-1]
            window = store.query_security_window(
                session_id=sid, node_id=node_id, runtime=runtime,
                position=anchor["position"], limit=200)
            if not window:
                raise RuntimeError("Committed security evidence is unavailable")
            inspection = {}
            incidents = detectors.run_all(window, sid, runtime, facts=facts,
                                          baseline=baseline, disabled=excluded, inspection=inspection)
            if any(value is False for value in inspection.values()):
                raise RuntimeError("Security detector inspection failed")
            # Each new committed event is in this window even when its source
            # timestamp is old. Evidence references never carry raw payloads.
            for incident in incidents:
                if incident.get("kind") == "inspection_incomplete":
                    limitations += 1
                from clawmetry import otlp_guard
                observation = otlp_guard.observation_label(window)
                if observation:
                    otlp_guard.label_incident(incident, observation)
                if not incident.get("evidence_refs"):
                    raise RuntimeError("Security finding lacks implicated evidence references")
                saved = store.record_incident_observation(incident=incident, node_id=node_id,
                                                           observed_at=now_ms)
                if not saved or not saved.get("incident_id"):
                    raise RuntimeError("Security finding persistence was not confirmed")
                incident["incident_id"] = saved["incident_id"]
                incident["incident_state"] = saved["state"]
                incident["first_seen_ms"] = saved["first_seen"]
                count += 1
            if incidents:
                apply_policies(store, incidents, session)
                for incident in incidents:
                    # This queues a durable reference only. The notification
                    # worker performs network I/O independently of inspection.
                    if incident.get("incident_state") == "active":
                        deliver(incident)
    cursor = {"version": 2, "position": journal["position"], "epoch": journal["epoch"]}
    encoded = json.dumps(cursor, sort_keys=True, separators=(",", ":"))
    history_gap = journal["history_gap"] or settings.get("guard.security.history_gap") == "true"
    status = {
        "last_pass_ms": now_ms, "processed": len(page), "findings": count,
        "unscoped": skipped, "limitations": limitations,
        "page_full": len(page) == max(1, min(PAGE_SIZE, int(limit))),
        "history_gap": history_gap,
        "status": "partial" if skipped or history_gap or limitations else "inspected"}
    store.commit_security_progress(cursor=encoded, status=status, history_gap=history_gap)
    if store.query_security_settings().get(CURSOR_KEY) != encoded:
        raise RuntimeError("Security cursor persistence was not confirmed")
    return {"processed": len(page), "findings": count, "status": status["status"]}


def start(store):
    """Start once in the daemon process, using its existing store handle."""
    global _THREAD
    with _START_LOCK:
        if _THREAD is not None and _THREAD.is_alive():
            return _THREAD
        def worker():
            captured_at = 0.0
            while True:
                _WAKE.wait(timeout=30)
                _WAKE.clear()
                cpu_started = time.process_time()
                work_started = time.monotonic()
                try:
                    if time.monotonic() - captured_at >= 60:
                        from clawmetry.protection_evidence import capture_and_store
                        capture_and_store(store)
                        captured_at = time.monotonic()
                except Exception:
                    log.exception("Protection configuration evidence unavailable")
                try:
                    result = process_batch(store)
                    if result["processed"]:
                        _WAKE.set()  # bounded backlog drain, one page per second
                except Exception:
                    log.exception("Incremental security inspection failed; cursor retained")
                    try:
                        store.set_node_setting(STATUS_KEY, json.dumps({
                            "last_pass_ms": int(time.time() * 1000), "status": "unavailable"}))
                    except Exception:
                        pass
                    _WAKE.set()
                # Cap busy drain/retry frequency; the heartbeat is independent.
                cpu_used = max(0.0, time.process_time() - cpu_started)
                wall_used = max(0.0, time.monotonic() - work_started)
                # At sustained load, budget this service to 7.5% of one core.
                # Quiet nodes wake on commits; backlog remains visible.
                time.sleep(max(1.0, min(60.0, cpu_used / 0.075 - wall_used)))
        def notifications():
            while True:
                try:
                    from clawmetry.incident_alerts import deliver_incident
                    store.drain_security_notifications(deliver=lambda inc, pid: deliver_incident(
                        store, inc, source="policy" if pid else "security", force=bool(pid), policy_id=pid))
                except Exception:
                    log.exception("Security notification queue unavailable")
                time.sleep(5)
        threading.Thread(target=notifications, daemon=True, name="security-notifications").start()
        _THREAD = threading.Thread(target=worker, daemon=True, name="security-ingest")
        _THREAD.start()
        _WAKE.set()
        return _THREAD
