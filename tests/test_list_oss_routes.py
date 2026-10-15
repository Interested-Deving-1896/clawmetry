"""The pin PR must name the routes a release adds.

**Why this exists.** clawmetry-cloud's enforcer refuses to boot when an
installed OSS route has no ``cloud_route_policy`` entry. That is the right
design — an unclassified route might serve a tenant data it should not — but
it means an OSS release that ADDS a route deadlocks the two cloud pull
requests against each other: the auto-pin PR is red on every check that
constructs the app, and a PR carrying the policy entry is red against the old
pin. Neither can be green alone, and the fix is one line of process.

Burned 2026-10-15 on 0.12.917 (``/api/delivery``). The failure presents as ~18
red checks on a PR that changed a version string, so it reads as a
catastrophe. ``scripts/list_oss_routes.py`` lets the pin PR say what is
actually going on, and these tests pin the two ways the message could lie: by
missing a route that was added, and by inventing routes that were not.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "list_oss_routes.py"

sys.path.insert(0, str(REPO / "scripts"))
import list_oss_routes as lor  # noqa: E402


def _run(*args):
    done = subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True, cwd=REPO)
    return done


def test_the_route_table_is_not_empty():
    """A silent empty list would report every release as route-free, which is
    the failure mode that leaves the deadlock unannounced."""
    routes = lor.routes_at()
    assert len(routes) > 100, len(routes)
    assert "/api/delivery" in routes
    assert all(r.startswith("/") for r in routes)


def test_a_decorator_argument_is_read_from_the_tree_not_the_text():
    """A regex over source text mis-reads a multi-line or computed
    decorator; ``ast`` sees the literal or nothing."""
    rules = lor._rules_from_source(
        "\n".join([
            "@bp.route('/api/plain', methods=['GET'])",
            "def a(): pass",
            "@bp.route(",
            "    '/api/wrapped',",
            "    methods=['POST'])",
            "def b(): pass",
            "@bp.route(f'/api/{computed}')",   # not a literal: must be skipped
            "def c(): pass",
            "app.add_url_rule('/api/added', view_func=d)",
            "@bp.route('relative-not-a-route')",
            "def e(): pass",
        ]), "<test>")
    assert rules == {"/api/plain", "/api/wrapped", "/api/added"}


def test_broken_source_warns_instead_of_raising():
    """A release workflow must never fail with a traceback: the message IS
    the deliverable here."""
    assert lor._rules_from_source("def oops(:\n", "<test>") == set()


@pytest.mark.skipif(
    not (REPO / ".git").exists(), reason="needs the git history")
def test_the_release_that_caused_the_deadlock_reports_its_routes():
    """0.12.917 added ``/api/delivery``; #6409 after it added nothing.

    Two real commits, so this cannot pass against a stub: ``cce45bf8ba`` is
    the Delivered tab and ``d7b3ddc3b9`` is the fix that followed it.
    """
    added = _run("--ref", "cce45bf8ba", "--added-since", "cce45bf8ba^")
    if added.returncode != 0:
        pytest.skip(f"shallow clone: {added.stderr.strip()[:120]}")
    assert added.stdout.split() == [
        "/api/delivery", "/api/delivery/session/<path:session_id>"]

    quiet = _run("--ref", "d7b3ddc3b9", "--added-since", "d7b3ddc3b9^")
    assert quiet.returncode == 0, quiet.stderr
    assert quiet.stdout.strip() == "", quiet.stdout


def test_an_unreachable_base_is_loud_not_plausible():
    """An unresolvable ref must not read as "this release added 537 routes".

    That is the specific lie this guard exists for: the pin PR would tell the
    next reader to go and classify the entire API.
    """
    done = _run("--added-since", "no-such-ref-abcdef")
    assert done.returncode == 2, done
    assert done.stdout.strip() == ""
    assert "no routes found" in done.stderr
