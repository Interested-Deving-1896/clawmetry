"""Process discovery and monitoring cost retain their evidence limits.

AC-OBS-NODE-SEARCH-001.1
AC-OBS-NODE-SEARCH-001.2
AC-OBS-NODE-SEARCH-001.3
AC-OBS-NODE-SEARCH-002.1
AC-OBS-NODE-SEARCH-002.2
AC-OBS-NODE-SEARCH-002.3
AC-OBS-NODE-SEARCH-002.4
"""
import json
from pathlib import Path
from types import SimpleNamespace as Obj

import pytest

from clawmetry import node_activity as collector
from tests.test_node_activity_collector_clarity import Sensor


@pytest.mark.parametrize("argv,role", [
    (["/usr/bin/python3", "-m", "clawmetry", "sync"], "collector"),
    (["python", "-u", "-m", "clawmetry.sync"], "collector"),
    (["python", "/venv/bin/clawmetry", "--port", "8900"], "dashboard"),
    ([r"C:\venv\Scripts\clawmetry.exe", "sync"], "collector"),
    (["python", "-m", "clawmetry", "--port", "8900"], "dashboard"),
    (["python", str(Path(collector.__file__).resolve().parents[1] / "dashboard.py")], "dashboard"),
    (["python", "other.py", "clawmetry", "sync"], None),
    (["python", "-c", "import clawmetry; print('sync')"], None),
    (["python", "-m", "unrelated", "clawmetry"], None),
    (["python", "/tmp/dashboard.py"], None),
    (["python", "-m", "clawmetry", "status"], "cli"),
    (["sh", "-c", "clawmetry sync"], None),
])
def test_exact_launch_roles(argv, role):
    assert collector._clawmetry_launch_role(argv) == role


def test_self_is_collected_before_enumeration_and_survives_cap(tmp_path, monkeypatch):
    from tests.test_node_activity import Store
    monkeypatch.setattr(collector, "MAX_PROCESSES", 2)
    monkeypatch.setattr(collector.os, "getpid", lambda: 10)
    clock = Obj(now=100.0)
    monkeypatch.setattr(collector.time, "monotonic", lambda: clock.now)
    sensor = Sensor()
    base = dict(sensor.processes[0].info)
    self_process = Obj(as_dict=lambda **kwargs: dict(base))
    sensor.Process = lambda pid: self_process if pid == 10 else None
    # The collector is absent from the bounded enumeration entirely.
    sensor.processes = [Obj(info=dict(base, pid=pid, create_time=pid)) for pid in range(20, 30)]
    sensor.error = None

    def scan():
        return collector.collect_node_activity(psutil_module=sensor, home=tmp_path,
                                               fingerprint_key=b"k" * 32, node_id="test")

    store = Store()
    try:
        first = store.record_node_activity(scan())
        row = next(row for row in first["processes"] if row["pid"] == 10)
        assert row["clawmetry_role"] == "collector" and row["cpu_percent"] is None
        assert len(first["processes"]) == 2 and first["coverage"]["processes"]["truncated"]
        clock.now += 30
        measured = store.record_node_activity(scan())
        row = next(row for row in measured["processes"] if row["pid"] == 10)
        assert row["cpu_percent"] == 0 and row["cpu_interval_seconds"] == 30
        assert row["memory_bytes"] == 40 and not row["stale"]
        assert row["actor"]["kind"] == "unknown"
        assert len(collector._PROCESS_CPU_SAMPLES[sensor]["samples"]) == 2
        disabled = collector.collect_node_activity(
            psutil_module=sensor, preferences={"processes": False}, home=tmp_path)
        assert disabled["public"]["processes"] == []
        assert disabled["public"]["coverage"]["processes"]["state"] == "disabled"
    finally:
        store._conn.close()


def test_role_survives_storage_without_arguments_or_false_attribution(tmp_path):
    from tests.test_node_activity import Store
    sensor = Sensor()
    sensor.error = None
    proc = sensor.processes[0]
    proc.info["name"] = "python3.12"
    proc.cmdline = lambda: ["python3", "-m", "clawmetry", "--token", "private-secret"]
    store = Store()
    try:
        observation = collector.collect_node_activity(psutil_module=sensor, home=tmp_path)
        data = store.record_node_activity(observation)
        row = next(row for row in data["processes"] if row["pid"] == 10)
        assert row["name"] == "python3.12" and row["clawmetry_role"] == "dashboard"
        assert row["actor"]["kind"] == "unknown"
        assert "private-secret" not in json.dumps(observation)
        assert "cmdline" not in json.dumps(data)
    finally:
        store._conn.close()


def test_unreadable_launch_does_not_drop_resource_observation(tmp_path):
    sensor = Sensor()
    sensor.error = None
    sensor.processes[0].info["name"] = "python3.12"
    def denied():
        raise PermissionError()
    sensor.processes[0].cmdline = denied
    result = collector.collect_node_activity(psutil_module=sensor, home=tmp_path)
    row = result["public"]["processes"][0]
    assert "clawmetry_role" not in row and row["memory_bytes"] == 40


def test_relative_dashboard_requires_matching_working_directory():
    root = Path(collector.__file__).resolve().parents[1]
    assert collector._clawmetry_launch_role(["python", "dashboard.py"], cwd=root) == "dashboard"
    assert collector._clawmetry_launch_role(["python", "dashboard.py"], cwd="/tmp") is None


@pytest.mark.parametrize("enumeration_denied", [False, True])
def test_self_is_deduplicated_and_preserved_when_enumeration_fails(tmp_path, monkeypatch, enumeration_denied):
    sensor = Sensor()
    sensor.error = None
    monkeypatch.setattr(collector.os, "getpid", lambda: 10)
    sensor.Process = lambda pid: Obj(as_dict=lambda **kwargs: dict(sensor.processes[0].info))
    if enumeration_denied:
        def denied(*args, **kwargs):
            raise PermissionError()
        sensor.process_iter = denied
    result = collector.collect_node_activity(psutil_module=sensor, home=tmp_path)["public"]
    assert len(result["processes"]) == 1
    assert result["processes"][0]["clawmetry_role"] == "collector"
    assert result["coverage"]["processes"]["state"] == ("partial" if enumeration_denied else "complete")
