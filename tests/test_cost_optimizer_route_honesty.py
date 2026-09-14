"""/api/cost-optimizer over a real local store (REQ-OBS-CEA-023, #5934).

The route half of tests/test_cost_optimizer_demo_honesty.py, split out
because it needs duckdb (MOAT Verifier job) while the renderer half runs in
the lint job with flask and node only.

  AC-OBS-CEA-023.3  -> test_route_labels_figures_with_their_basis,
                       test_route_with_nothing_recorded_is_unknown_not_zero
  AC-OBS-CEA-023.4  -> test_route_has_no_fixed_savings_or_hardcoded_recs
  AC-OBS-CEA-023.5  -> test_route_hides_local_advice_for_bedrock_traffic
  AC-OBS-CEA-023.8  -> test_route_reports_unrecorded_tokens_as_none
"""

from __future__ import annotations

import importlib
import json
import time
from datetime import datetime, timezone

import pytest
from flask import Flask

BEDROCK = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"


# ── the route, over a real local store ──────────────────────────────────────

def _today():
    return datetime.now(timezone.utc).date().isoformat()


@pytest.fixture
def store_app(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAWMETRY_LOCAL_STORE_PATH", str(tmp_path / "events.duckdb"))
    monkeypatch.setenv("CLAWMETRY_LOCAL_FLUSH_SECS", "0.05")
    monkeypatch.setenv("CLAWMETRY_LOCAL_FLUSH_BATCH", "5")
    monkeypatch.setenv("CLAWMETRY_LOCAL_STORE_READ", "1")
    import clawmetry.local_store as ls
    importlib.reload(ls)
    import routes.local_query as lq
    monkeypatch.setattr(lq, "_DISCOVERY_PATH", str(tmp_path / "no-such-discovery.json"))
    lq._invalidate_daemon_cache()
    import routes.sessions as sessions_mod
    importlib.reload(sessions_mod)
    import routes.infra as infra_mod
    importlib.reload(infra_mod)

    llmfit_calls = []
    real_run = infra_mod.subprocess.run

    def _run(cmd, *a, **kw):
        if cmd and cmd[0] == "llmfit":
            llmfit_calls.append(cmd)
            raise FileNotFoundError("llmfit disabled in tests")
        return real_run(cmd, *a, **kw)

    monkeypatch.setattr(infra_mod.subprocess, "run", _run)
    app = Flask(__name__)
    app.register_blueprint(infra_mod.bp_config)
    yield app, ls.get_store(), llmfit_calls
    try:
        ls.get_store().stop(flush=True)
    except Exception:
        pass


def _ingest(store, ev_id, model, cost, tokens, second):
    store.ingest({
        "id": ev_id, "node_id": "agent+test", "agent_id": "main",
        "session_id": "sess-" + ev_id, "event_type": "assistant",
        "ts": "%sT10:00:%02d+00:00" % (_today(), second),
        "data": {"type": "assistant", "message": {"role": "assistant", "model": model}},
        "cost_usd": cost, "token_count": tokens, "model": model,
    })


def _flush(store, timeout=2.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if store.health()["ring_depth"] == 0:
            return
        time.sleep(0.02)


def _get(app):
    r = app.test_client().get("/api/cost-optimizer")
    assert r.status_code == 200, r.get_data(as_text=True)
    return r.get_json()


def test_route_hides_local_advice_for_bedrock_traffic(store_app):
    app, store, llmfit_calls = store_app
    for i in range(4):
        _ingest(store, "b%d" % i, BEDROCK, 0.25, 1200, i)
    _flush(store)
    body = _get(app)
    assert body["localAdvice"]["show"] is False
    assert "AWS Bedrock" in body["localAdvice"]["reason"]
    assert body["localModels"] == []
    assert llmfit_calls == [], "llmfit ran for a team whose traffic is on Bedrock"


def test_route_has_no_fixed_savings_or_hardcoded_recs(store_app):
    app, store, _ = store_app
    for i in range(4):
        _ingest(store, "h%d" % i, BEDROCK, 0.25, 1200, i)
    _flush(store)
    body = _get(app)
    assert "potentialSavings" not in body
    blob = json.dumps(body)
    for banned in ("60-80%", "Diya", "savingsEstimate", "estimatedSavings", "~$"):
        assert banned not in blob, banned
    recs = body["taskRecommendations"]
    assert recs and all(r.get("evidence") for r in recs)
    assert recs[0]["model"] == BEDROCK and recs[0]["evidence"]["events"] == 4


def test_route_labels_figures_with_their_basis(store_app):
    app, store, _ = store_app
    _ingest(store, "p0", BEDROCK, 1.0, 900, 0)
    _flush(store)
    body = _get(app)
    prov = body["provenance"]
    assert prov["todayCost"]["basis"] == "derived"
    assert prov["projectedMonthlyCost"]["basis"] == "estimated"
    assert prov["expensiveOps"]["basis"] == "derived"
    assert abs(body["todayCost"] - 1.0) < 0.01


def test_route_with_nothing_recorded_is_unknown_not_zero(store_app):
    app, store, _ = store_app
    _flush(store)
    body = _get(app)
    assert body["todayCost"] is None and body["projectedMonthlyCost"] is None
    assert body["provenance"]["todayCost"]["basis"] == "unknown"
    assert body["provenance"]["todayCost"].get("reason")
    assert body["recommendationsNote"]


def test_route_reports_unrecorded_tokens_as_none(store_app):
    app, store, _ = store_app
    _ingest(store, "t0", BEDROCK, 0.5, 0, 0)
    _flush(store)
    ops = _get(app)["expensiveOps"]
    assert ops and all(op["tokens"] is None for op in ops), ops
