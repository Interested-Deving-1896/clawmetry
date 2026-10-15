"""Public orchestration for private runtime wheels. Never print private test output.

The catalogue determines coverage. Path selection may narrow known adapter edits;
unknown changes always select the complete catalogue. No provider keys are used.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from xml.parsers import expat

OPERATING_SYSTEMS = ('ubuntu-latest', 'windows-latest', 'macos-latest')


def checkout_private(pro: Path, sha: str, private_logs: Path) -> dict:
    """Fetch a fixed repository without exposing private commit titles or auth."""
    if not re.fullmatch('[0-9a-f]{40}', sha):
        raise ValueError('An exact candidate SHA is required')
    token = os.environ.get('PRO_REPO_READ_TOKEN', '')
    if not token:
        raise ValueError('Private candidate read credentials are required')
    pro.mkdir(parents=True, exist_ok=False)
    private_logs.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    # Transient environment configuration is not written to .git/config.
    env.update(GIT_CONFIG_COUNT='1',
               GIT_CONFIG_KEY_0='http.https://github.com/vivekchand/clawmetry-pro.extraheader',
               GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + base64.b64encode(
                   ('x-access-token:' + token).encode()).decode(),
               GIT_TERMINAL_PROMPT='0')
    commands = [
        ['git', 'init', str(pro)],
        ['git', '-C', str(pro), 'remote', 'add', 'origin',
         'https://github.com/vivekchand/clawmetry-pro.git'],
        ['git', '-C', str(pro), 'fetch', '--no-tags', 'origin', sha],
        ['git', '-C', str(pro), 'checkout', '--detach', sha],
    ]
    with (private_logs / 'checkout.log').open('wb') as log:
        for command in commands:
            result = subprocess.run(command, env=env, stdout=log,
                                    stderr=subprocess.STDOUT, timeout=180)
            if result.returncode:
                raise ValueError('Private candidate checkout failed; raw output is withheld')
    return {'candidate_sha': sha}


def catalogue(path: Path) -> dict:
    result = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#') or '\t' not in line:
            continue
        name, label, tier, *_ = line.split('\t')
        if not re.fullmatch(r'[a-z][a-z0-9_]*', name) or tier not in {'free', 'paid'}:
            raise ValueError('Invalid runtime catalogue entry')
        if name in result:
            raise ValueError('Duplicate runtime catalogue entry')
        result[name] = {'label': label, 'tier': tier}
    if not result:
        raise ValueError('Empty runtime catalogue')
    return result


def affected_runtimes(paths: list, runtimes: dict) -> list:
    """Only explicitly recognized leaf edits may narrow coverage."""
    selected = set()
    for raw in paths:
        path = PurePosixPath(raw)
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('Invalid changed path')
        if str(path) in {'README.md', 'CHANGELOG.md', '.gitignore'}:
            continue
        found = set()
        for runtime in runtimes:
            if (str(path) == f'clawmetry_pro/adapters/{runtime}.py'
                    or str(path) == f'clawmetry/adapters/{runtime}.py'
                    or str(path).startswith(f'tests/fixtures/runtimes/{runtime}/')
                    or (path.parent == PurePosixPath('tests') and
                        (path.name == f'test_adapter_{runtime}.py'
                         or path.name == f'test_{runtime}_runtime_adapter.py'
                         or path.name.startswith(f'test_{runtime}_adapter')))):
                found.add(runtime)
        if not found:
            return sorted(runtimes)
        selected.update(found)
    return sorted(selected)


def git_index(root: Path) -> list:
    # Index blob identities are stable across Windows checkout line endings.
    # All unknown files are included: a new shared helper must invalidate a hit.
    data = subprocess.check_output(['git', '-C', str(root), 'ls-files', '--stage', '-z'])
    return [x.decode('utf-8') for x in data.split(b'\0') if x]


def fingerprint(oss: Path, pro: Path) -> str:
    """Content identity excludes cosmetic docs, commit messages and build clocks."""
    digest = hashlib.sha256()
    for label, root in [('oss', oss), ('pro', pro)]:
        for entry in sorted(git_index(root)):
            identity, name = entry.split('\t', 1)
            if name in {'README.md', 'CHANGELOG.md', '.gitignore'}:
                continue
            digest.update(label.encode() + b'\0' + name.encode() + b'\0' + identity.encode() + b'\0')
    return digest.hexdigest()


def runtime_tests(root: Path, runtime: str) -> list:
    tests = root / 'tests'
    return sorted({str(p) for pattern in
                   (f'test_{runtime}_adapter*.py', f'test_adapter_{runtime}.py',
                    f'test_{runtime}_runtime_adapter.py')
                   for p in tests.glob(pattern) if p.is_file()})


def executed_cases(path: Path) -> int:
    """Count unskipped JUnit cases with bounded input and no DTD support."""
    if path.stat().st_size > 10 * 1024 * 1024:
        raise ValueError('JUnit report exceeds the private parser limit')
    parser = expat.ParserCreate()
    active = skipped = False
    count = 0

    def reject_doctype(*args):
        raise ValueError('DTD declarations are not permitted in JUnit reports')

    def start(name, attrs):
        nonlocal active, skipped
        if name == 'testcase':
            if active:
                raise ValueError('Nested JUnit testcases are not permitted')
            active, skipped = True, False
        elif name == 'skipped' and active:
            skipped = True

    def end(name):
        nonlocal active, count
        if name == 'testcase':
            count += int(not skipped)
            active = False

    parser.StartDoctypeDeclHandler = reject_doctype
    parser.StartElementHandler = start
    parser.EndElementHandler = end
    with path.open('rb') as stream:
        parser.ParseFile(stream)
    return count


def run_runtime(oss: Path, pro: Path, runtime: str, private_logs: Path) -> dict:
    """Run one suite in a fresh process, retaining raw output only on the runner."""
    tests = runtime_tests(pro, runtime) + runtime_tests(oss, runtime)
    # OpenClaw uses a wider OSS family rather than test_openclaw_adapter.py.
    if runtime == 'openclaw':
        tests += [str(oss / 'tests' / name) for name in
                  ('test_openclaw_list_events.py', 'test_openclaw_replay_events.py')]
    if not tests:
        return {'runtime': runtime, 'mode': 'fixture/unit', 'status': 'missing-coverage'}
    private_logs.mkdir(parents=True, exist_ok=True)
    log = private_logs / f'{runtime}.log'
    junit = private_logs / f'{runtime}.xml'
    # Avoid putting credentials into subprocess environments even if a caller
    # accidentally supplied them to orchestration. These suites use local stores.
    env = {k: v for k, v in os.environ.items()
           if not any(x in k.upper() for x in ('TOKEN', 'SECRET', 'API_KEY', 'PASSWORD'))}
    env['CM_CONFORMANCE_RUNTIME'] = runtime
    with log.open('wb') as output:
        try:
            process = subprocess.run(
                [sys.executable, '-m', 'pytest', *tests, '--tb=no', '-q', '--import-mode=importlib',
                 f'--junitxml={junit}'],
                cwd=pro, env=env, stdout=output, stderr=subprocess.STDOUT, timeout=300)
            status = 'failed'
            if process.returncode == 0 and junit.exists():
                try:
                    status = 'passed' if executed_cases(junit) else 'unverified'
                except (ValueError, expat.ExpatError):
                    status = 'failed'
        except subprocess.TimeoutExpired:
            status = 'timed-out'
    # Do not publish node ids, assertion strings, traceback locals or fixture text.
    return {'runtime': runtime, 'mode': 'fixture/unit', 'status': status}


def prepare(oss: Path, pro: Path, private_logs: Path) -> dict:
    private_logs.mkdir(parents=True, exist_ok=True)
    wheel_dir = private_logs / 'wheels'
    wheel_dir.mkdir(exist_ok=True)
    with (private_logs / 'installation.log').open('wb') as log:
        commands = [
            [sys.executable, '-m', 'pip', 'install', 'setuptools', 'wheel', 'pytest',
             'requests', 'psutil', 'msgpack', 'pyyaml', 'pyserial', 'psycopg2-binary',
             'langgraph-checkpoint', 'langchain-core'],
            [sys.executable, '-m', 'pip', 'install', str(oss)],
            [sys.executable, '-m', 'pip', 'wheel', '--no-deps', str(pro), '-w', str(wheel_dir)],
        ]
        for command in commands:
            subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=600)
        wheels = list(wheel_dir.glob('clawmetry_pro-*.whl'))
        if len(wheels) != 1:
            raise ValueError('Candidate build did not produce exactly one Pro wheel')
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--no-deps', str(wheels[0])],
                       stdout=log, stderr=subprocess.STDOUT, check=True, timeout=120)
    # Pytest must exercise the installed wheel, not an implicit source import
    # from the private checkout that happens to sit beside its tests.
    (pro / 'clawmetry_pro').rename(pro / '_candidate_source_not_importable')
    with (private_logs / 'installation.log').open('ab') as log:
        subprocess.run([sys.executable, '-c', (
            'import importlib.metadata as m; from pathlib import Path; '
            'import clawmetry_pro as p; '
            'assert not Path(p.__file__).resolve().is_relative_to(Path.cwd()); '
            'assert p.__version__ == m.version("clawmetry-pro"); '
            'assert any(e.name == "clawmetry_pro" and callable(e.load()) '
            'for e in m.entry_points(group="clawmetry.extensions"))'
        )], cwd=pro, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=60)
    return {'wheel_sha256': hashlib.sha256(wheels[0].read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['checkout', 'plan', 'prepare', 'run'])
    parser.add_argument('--sha')
    parser.add_argument('--oss', type=Path, required=True)
    parser.add_argument('--pro', type=Path, required=True)
    parser.add_argument('--changed', type=Path)
    parser.add_argument('--selection', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--private-logs', type=Path)
    args = parser.parse_args()
    args.oss = args.oss.resolve()
    args.pro = args.pro.resolve()
    if args.private_logs:
        args.private_logs = args.private_logs.resolve()
    if args.command == 'checkout':
        result = checkout_private(args.pro, args.sha or '', args.private_logs)
        args.output.write_text(json.dumps(result), encoding='utf-8')
        return
    if args.command == 'prepare':
        result = prepare(args.oss, args.pro, args.private_logs)
        args.output.write_text(json.dumps(result), encoding='utf-8')
        return
    runtimes = catalogue(args.oss / 'SUPPORTED_RUNTIMES.txt')
    if args.command == 'plan':
        changed = json.loads(args.changed.read_text()) if args.changed else None
        selected = sorted(runtimes) if changed is None else affected_runtimes(changed, runtimes)
        identity = fingerprint(args.oss, args.pro) + '\n' + json.dumps(selected)
        result = {'runtimes': selected, 'fingerprint': hashlib.sha256(identity.encode()).hexdigest(),
                  'operating_systems': list(OPERATING_SYSTEMS), 'catalogue_count': len(runtimes)}
        args.output.write_text(json.dumps(result, sort_keys=True), encoding='utf-8')
        return
    selected = json.loads(args.selection.read_text())['runtimes']
    if not selected or any(x not in runtimes for x in selected):
        raise ValueError('Invalid runtime selection')
    results = [run_runtime(args.oss, args.pro, name, args.private_logs) for name in selected]
    args.output.write_text(json.dumps(results, sort_keys=True), encoding='utf-8')
    for result in results:
        print(f"{result['runtime']}: {result['status']} ({result['mode']})")
    if any(x['status'] != 'passed' for x in results):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
