"""Dashboard cold load: no startup storm, no duplicate requests (#5935).

On a cold start the dashboard's own startup requests timed out
(``Initial load failed timeout``, ``System health load failed timeout``,
``loadCrons failed timeout``) and their tiles rendered empty. Measured in a
headless browser against a scratch install: 121 API requests in one page load,
103 in the first 10 s, 22 in flight at the peak, against the browser's six
connections per origin. Requests spent 66 s combined in the browser's own queue
while the server answered most of them in milliseconds.

Behaviour of the startup path is pinned in ``test_cold_load_boot_js.js``
against shipped source. The checks below pin the seams that are not worth
running in a VM: that opening Overview loads what startup no longer preloads,
that the Flow tool prefetch waits for a screen that uses it, and that the
duplicate ``/api/overview`` callers share one in-flight request.

Factory requirement 08aff8e1-2a68-41c2-8052-da53bbbdd749 (AC 2, 3, 5).
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
_JS_TEST = os.path.join(_HERE, "test_cold_load_boot_js.js")
_APP_JS = os.path.join(_HERE, "..", "clawmetry", "static", "js", "app.js")
_OVERVIEW_HTML = os.path.join(_HERE, "..", "clawmetry", "templates", "tabs", "overview.html")


def _src() -> str:
    with open(_APP_JS, encoding="utf-8") as fh:
        return fh.read()


def _function(name: str, is_async: bool = False) -> str:
    prefix = "async " if is_async else ""
    m = re.search(r"^" + prefix + r"function " + name + r"\b[\s\S]*?^\}", _src(), re.M)
    assert m, f"{name} not found in app.js"
    return m.group(0)


@pytest.mark.skipif(
    shutil.which("node") is None,
    reason="node not on PATH; JS unit tests only run when Node is available",
)
def test_cold_load_boot_unit_suite() -> None:
    proc = subprocess.run(["node", _JS_TEST], capture_output=True, text=True, timeout=60)
    output = (proc.stdout or "") + (proc.stderr or "")
    assert proc.returncode == 0, "cold-load boot tests failed:\n" + output
    assert "PASS" in output, "no PASS line in output:\n" + output


def test_opening_overview_loads_what_startup_no_longer_preloads() -> None:
    """Startup skips system health and tasks off-Overview, so the first visit
    must load them at once rather than on the next 10-30 s refresh tick."""
    body = _function("switchTab")
    assert re.search(r"_cmLoadedWithin\('systemHealth',\s*\d+\)\)\s*loadSystemHealth\(\)", body), (
        "switchTab('overview') does not load system health on the first visit"
    )
    assert re.search(r"_cmLoadedWithin\('overviewTasks',\s*\d+\)\)\s*loadOverviewTasks\(\)", body), (
        "switchTab('overview') does not load Overview tasks on the first visit"
    )


def test_loads_record_success_so_starters_do_not_repeat_them() -> None:
    assert "_cmMarkLoaded('systemHealth')" in _function("loadSystemHealth", is_async=True)
    assert "_cmMarkLoaded('overviewTasks')" in _function("loadOverviewTasks", is_async=True)


def test_flow_tool_prefetch_waits_for_a_screen_that_uses_it() -> None:
    """Twelve /api/component/tool/* requests fired 2 s into every page load,
    whatever screen it landed on."""
    src = _src()
    assert "setTimeout(_prefetchToolData, 2000)" not in src, (
        "the Flow tool-detail prefetch still fires unconditionally at startup"
    )
    assert re.search(r"function _prefetchToolDataIfVisible\b", src), (
        "no tab-gated wrapper around the Flow tool-detail prefetch"
    )


def test_duplicate_overview_callers_share_one_request() -> None:
    body = _function("_cmLoadDetectedRuntimes", is_async=True)
    assert "fetchJsonWithTimeout('/api/overview'" in body, (
        "_cmLoadDetectedRuntimes sends its own /api/overview beside loadAll's"
    )
    with open(_OVERVIEW_HTML, encoding="utf-8") as fh:
        html = fh.read()
    assert "fetchJsonWithTimeout('/api/overview'" in html, (
        "the Overview heartbeat card sends its own /api/overview beside loadAll's"
    )


def test_slow_usage_never_draws_measured_looking_zeros() -> None:
    """AC 5: when /api/usage was slow on a cold start, loadAll drew $0.00 and
    0 tokens into the Overview tiles, which read as 'no spend on this machine'."""
    body = _function("loadAll", is_async=True).replace(" ", "")
    assert "todayCost:0" not in body, "loadAll still renders zero usage it never measured"
    assert "_cmUsageTilesStillLoading" in body, (
        "loadAll does not put the usage tiles back on their loading placeholders"
    )


def test_failures_read_as_sentences_not_raw_error_codes() -> None:
    """AC 5: a busy server is not 'Failed to load: timeout'."""
    for name in ("loadSystemHealth", "loadCrons"):
        body = _function(name, is_async=True)
        catch = body[body.rindex("catch") :]
        assert "e.message" not in catch and "String(e" not in catch, (
            f"{name} still renders the raw error text to the user"
        )
