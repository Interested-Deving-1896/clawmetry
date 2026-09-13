"""The Cost Optimizer opens quickly, labels every figure and advises only on
what was recorded (REQ-OBS-CEA-023, vivekchand/clawmetry#5934).

Measured on 0.12.876: a cold dashboard showed "Analyzing costs..." for ~33s
(the endpoint answers in ~1s; the wait was the browser's startup pile-up),
then a leftover ``[prod]`` label, unlabelled Today/Month figures, rows reading
"unknown tokens", a fixed "60-80%" savings claim, hardcoded recommendations
(one naming a personal agent), Ollama/llmfit advice to a team on a cloud
provider, "Historical cost analysis coming soon" in time travel, and a 402
parsed as data ("not available" instead of an upgrade prompt).

Acceptance criteria and the tests that hold them:

  AC-OBS-CEA-023.1  bounded wait, readable failure, retry
                    -> test_modal_timeout_is_a_sentence_with_retry,
                       test_modal_server_failure_is_a_sentence_not_a_code
  AC-OBS-CEA-023.2  402 renders the upgrade prompt
                    -> test_modal_402_renders_upgrade_prompt
  AC-OBS-CEA-023.3  every figure carries its basis; unknown is not zero
                    -> test_route_labels_figures_with_their_basis,
                       test_route_with_nothing_recorded_is_unknown_not_zero,
                       test_modal_renders_basis_and_no_debug_label
  AC-OBS-CEA-023.4  no unmeasured savings; recommendations are experiments
                    citing recorded usage
                    -> test_experiments_cite_usage_and_carry_no_savings,
                       test_route_has_no_fixed_savings_or_hardcoded_recs,
                       test_modal_skips_recommendations_without_evidence
  AC-OBS-CEA-023.5  no local-model advice for managed-provider traffic
                    -> test_provider_routes, test_local_advice_follows_traffic,
                       test_route_hides_local_advice_for_bedrock_traffic,
                       test_modal_renders_basis_and_no_debug_label
  AC-OBS-CEA-023.6  reachable from the Usage tab above the fold
                    -> test_usage_tab_opens_the_optimizer_above_the_cards
  AC-OBS-CEA-023.7  time travel states what the optimizer covers
                    -> test_modal_time_travel_is_not_a_placeholder
  AC-OBS-CEA-023.8  unrecorded tokens are "not recorded", not "unknown tokens"
                    -> test_route_reports_unrecorded_tokens_as_none,
                       test_modal_renders_basis_and_no_debug_label
"""

from __future__ import annotations

import importlib
import json
import re
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import pytest
from flask import Flask

from clawmetry import cost_optimizer_advice as adv

REPO = Path(__file__).resolve().parents[1]
APP_JS = (REPO / "clawmetry" / "static" / "js" / "app.js").read_text(encoding="utf-8")
PROV_JS = (REPO / "clawmetry" / "static" / "js" / "provenance.js").read_text(encoding="utf-8")
USAGE_HTML = (REPO / "clawmetry" / "templates" / "tabs" / "usage.html").read_text(encoding="utf-8")
EN_JSON = json.loads((REPO / "clawmetry" / "static" / "locales" / "en.json").read_text(encoding="utf-8"))

BEDROCK = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"


# ── pure rules ──────────────────────────────────────────────────────────────

@pytest.mark.parametrize("model,route", [
    (BEDROCK, "bedrock"),
    ("anthropic.claude-3-haiku-20240307-v1:0", "bedrock"),
    ("azure/gpt-4o", "azure"),
    ("vertex_ai/claude-3-5-sonnet@20240620", "vertex"),
    ("claude-opus-4-7", "anthropic"),
    ("gpt-5", "openai"),
    ("qwen3:4b", "local"),
    ("ollama/llama3", "local"),
    # A hosted open-weights deployment must not be guessed local.
    ("meta-llama/Llama-3.3-70B-Instruct", "unrecognised"),
    ("my-prod-deployment", "unrecognised"),
    ("", "unrecognised"),
    (None, "unrecognised"),
])
def test_provider_routes(model, route):
    assert adv.provider_route(model) == route


def _rows(model, n, cost=0.2, tokens=100):
    return [{"model": model, "cost_usd": cost, "token_count": tokens,
             "session_id": "s", "ts": "2026-09-14T10:00:%02d" % i} for i in range(n)]


def test_local_advice_follows_traffic():
    managed = adv.local_advice(adv.observed_usage(_rows(BEDROCK, 4)))
    assert managed["show"] is False
    assert "AWS Bedrock" in managed["reason"]

    unrec = adv.local_advice(adv.observed_usage(_rows("my-prod-deployment", 4)))
    assert unrec["show"] is False and "could not be recognised" in unrec["reason"]

    nothing = adv.local_advice(adv.observed_usage([]))
    assert nothing["show"] is False and nothing["reason"]

    local = adv.local_advice(adv.observed_usage(_rows("qwen3:4b", 2, cost=0) + _rows(BEDROCK, 4)))
    assert local["show"] is True


def test_observed_usage_dedupes_sibling_rows_and_keeps_unknown_cost_unknown():
    rows = _rows(BEDROCK, 3)
    rows += [dict(r) for r in rows]  # assistant + model.completed siblings
    rows += _rows("claude-opus-4-7", 2, cost=None, tokens=50)
    usage = {u["model"]: u for u in adv.observed_usage(rows)}
    assert usage[BEDROCK]["events"] == 3
    assert abs(usage[BEDROCK]["costUsd"] - 0.6) < 1e-9
    assert usage["claude-opus-4-7"]["costUsd"] is None  # no cost recorded != $0


def test_experiments_cite_usage_and_carry_no_savings():
    usage = adv.observed_usage(_rows(BEDROCK, 5) + _rows("claude-opus-4-7", 1))
    recs = adv.experiments(usage, "the most recent 200 events in the local store")
    assert len(recs) == 1, "a model with fewer than 3 recorded events is not evidence"
    rec = recs[0]
    assert rec["evidence"]["events"] == 5
    assert rec["evidence"]["window"]
    assert "acceptance checks" in rec["experiment"]
    blob = json.dumps(recs).lower()
    for banned in ("savings", "~$", "%", "/month", "/day"):
        assert banned not in blob, banned
    assert adv.recommendations_note(usage, recs) is None
    assert adv.recommendations_note(adv.observed_usage(_rows(BEDROCK, 1)), [])


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


# ── the Usage tab entry point ───────────────────────────────────────────────

def test_usage_tab_opens_the_optimizer_above_the_cards():
    m = re.search(r'<button[^>]*id="usage-open-cost-optimizer"[^>]*>', USAGE_HTML)
    assert m, "no Cost Optimizer button on the Usage tab"
    assert "openCompModal('node-cost-optimizer')" in m.group(0)
    bar = USAGE_HTML.index('class="refresh-bar"')
    first_card = USAGE_HTML.index('class="card"')
    assert bar < m.start() < first_card, "the button must sit in the refresh bar, above the first card"
    assert EN_JSON.get("usage.open_cost_optimizer") == "Cost Optimizer"


# ── the shipped renderer, executed ──────────────────────────────────────────

def _js_function(name):
    i = APP_JS.index("function %s(" % name)
    j = APP_JS.index("{", i)
    depth, k = 0, j
    while True:
        ch = APP_JS[k]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return APP_JS[i:k + 1]
        k += 1


_HARNESS = r"""
const vm = require('vm');
const fs = require('fs');
const input = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const els = {};
function el(id) { return els[id] || (els[id] = {innerHTML: '', textContent: ''}); }
const ctx = {
  console, setTimeout, clearTimeout, AbortController, JSON, Number, String, Math, Date,
  document: {getElementById: el},
  t: function(k, n, f) { return f; },
  escapeHtml: function(s) { return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); },
  isCompModalActive: function() { return true; },
  visibilitySetInterval: function() { return 1; },
  clearInterval: function() {},
  _costOptimizerRefreshTimer: 1,
  _currentTimeContext: input.timeContext || null,
};
ctx.window = ctx;
ctx.fetch = function(url, opts) {
  const sc = input.scenario;
  if (sc === 'hang') {
    return new Promise(function(_res, rej) {
      opts.signal.addEventListener('abort', function() { rej(new Error('AbortError')); });
    });
  }
  if (sc === '402') return Promise.resolve({status: 402, ok: false, json: () => Promise.resolve({error: 'upgrade_required'})});
  if (sc === '500') return Promise.resolve({status: 500, ok: false, json: () => Promise.resolve({})});
  return Promise.resolve({status: 200, ok: true, json: () => Promise.resolve(input.payload)});
};
vm.createContext(ctx);
vm.runInContext(input.provenance, ctx);
vm.runInContext(input.source + '\n_COST_OPT_TIMEOUT_MS = 60;', ctx);
if (input.scenario === 'time') vm.runInContext('loadCostOptimizerDataWithTime()', ctx);
else vm.runInContext('loadCostOptimizerData(false)', ctx);
setTimeout(function() {
  process.stdout.write(JSON.stringify({body: el('comp-modal-body').innerHTML, footer: el('comp-modal-footer').textContent}));
}, 250);
"""


def _render(tmp_path, scenario, payload=None, time_context=None):
    if shutil.which("node") is None:
        pytest.skip("node not on PATH")
    src = "\n".join([
        "var _COST_OPT_TIMEOUT_MS = 12000;",
        _js_function("_costOptFailureHtml"),
        _js_function("_costOptLockedHtml"),
        _js_function("loadCostOptimizerData"),
        _js_function("loadCostOptimizerDataWithTime"),
    ])
    inp = tmp_path / ("in-%s.json" % scenario)
    inp.write_text(json.dumps({
        "scenario": scenario, "payload": payload, "timeContext": time_context,
        "source": src, "provenance": PROV_JS,
    }), encoding="utf-8")
    harness = tmp_path / "harness.js"
    harness.write_text(_HARNESS, encoding="utf-8")
    proc = subprocess.run(["node", str(harness), str(inp)], capture_output=True, text=True, timeout=30)
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def test_modal_402_renders_upgrade_prompt(tmp_path):
    out = _render(tmp_path, "402")
    assert "paid feature" in out["body"] and "See pricing" in out["body"]
    assert "not available" not in out["body"]


def test_modal_timeout_is_a_sentence_with_retry(tmp_path):
    out = _render(tmp_path, "hang")
    assert "did not answer within 12 seconds" in out["body"]
    assert "loadCostOptimizerData(false)" in out["body"]
    assert "Analyzing" not in out["body"]


def test_modal_server_failure_is_a_sentence_not_a_code(tmp_path):
    out = _render(tmp_path, "500")
    assert "could not be loaded right now" in out["body"]
    assert "500" not in out["body"] and "HTTP" not in out["body"]


def _bedrock_payload():
    prov = adv.cost_provenance("local_store")
    usage = adv.observed_usage(_rows(BEDROCK, 4))
    recs = adv.experiments(usage, adv.LOCAL_STORE_WINDOW)
    return {
        "scope": "all runtimes on this computer",
        "todayCost": 1.25,
        "projectedMonthlyCost": None,
        "expensiveOps": [{"model": BEDROCK, "cost": 0.5, "tokens": None, "timeAgo": "10:00"}],
        "modelUsage": usage,
        "taskRecommendations": recs + [{
            "task": "Heartbeat / periodic checks", "currentModel": "claude-sonnet-4-6",
            "suggestedLocal": "qwen3:4b", "estimatedSavings": "~$2-5/month",
        }],
        "localAdvice": adv.local_advice(usage),
        "localModels": [{"name": "should-not-render"}],
        "potentialSavings": "60-80% with local models for crons/heartbeats",
        "provenance": dict(prov, projectedMonthlyCost={"basis": "unknown", "reason": "test"}),
    }


def test_modal_renders_basis_and_no_debug_label(tmp_path):
    body = _render(tmp_path, "ok", payload=_bedrock_payload())["body"]
    assert "[prod]" not in body
    assert "60-80%" not in body
    assert 'data-basis="derived"' in body, "Today renders without its basis"
    assert "not available" in body, "an unknown projection must not render as a figure"
    assert "unlabelled" not in body
    assert "tokens not recorded" in body and "unknown tokens" not in body
    assert "AWS Bedrock" in body
    lowered = body.lower()
    assert "ollama" not in lowered and "llmfit" not in lowered and "should-not-render" not in body


def test_modal_skips_recommendations_without_evidence(tmp_path):
    body = _render(tmp_path, "ok", payload=_bedrock_payload())["body"]
    assert "Experiments worth trying" in body
    assert "4 recorded model events" in body
    assert "Heartbeat / periodic checks" not in body
    assert "~$2-5/month" not in body


def test_modal_time_travel_is_not_a_placeholder(tmp_path):
    out = _render(tmp_path, "time", time_context={"date": "2026-09-01", "hour": None})
    assert "coming soon" not in out["body"].lower()
    assert "Back to live" in out["body"] and "switchTab('usage')" in out["body"]
    assert "analyses current spend" in out["body"]
