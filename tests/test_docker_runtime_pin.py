"""The root Dockerfile's hash-pinned runtime set must still match requirements.txt.

`Dockerfile` no longer installs `-r requirements.txt` directly: it installs
`.github/requirements/docker-runtime.txt` with `--require-hashes`, so the image
gets artifacts whose sha256 is declared rather than whatever the index serves at
build time.

That pin buys reproducibility and costs a second file that can drift. The
failure mode is silent and one-directional: add a dependency to
requirements.txt, and the image simply does not get it -- `docker build` still
succeeds, and nothing else in CI builds this image (only
deploy/self-hosted/Dockerfile.release is built, by container-image.yml). The
same class of drift already bit clawmetry-cloud, whose production image and
requirements.txt disagreed on a gevent floor until someone noticed by hand.

So this is the guard that makes the pin honest. It is pure parsing -- no
network, no pip -- so it runs in the Syntax & Lint job on Python 3.9 alongside
the other drift guards.

Named explicitly in .github/workflows/ci.yml because this repo's CI runs FILE
LISTS, not `pytest tests/`: a guard added without a line there runs in no job
at all.
"""
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIREMENTS = os.path.join(REPO_ROOT, "requirements.txt")
PINNED = os.path.join(REPO_ROOT, ".github", "requirements", "docker-runtime.txt")
DOCKERFILE = os.path.join(REPO_ROOT, "Dockerfile")

# `name>=1.2,<2 ; marker  # comment`
_REQ = re.compile(
    r"^(?P<name>[A-Za-z0-9._-]+)"
    r"(?P<specs>(?:\s*[<>=!~]=?\s*[^,;#\s]+\s*,?)*)"
    r"(?:;\s*(?P<marker>[^#]+?))?\s*(?:#.*)?$"
)
_SPEC = re.compile(r"(?P<op>[<>=!~]=?)\s*(?P<version>[^,\s]+)")
_PIN = re.compile(r"^(?P<name>[A-Za-z0-9._-]+)==(?P<version>[^\s\\]+)\s*\\?\s*$")
_PY_MARKER = re.compile(
    r"""python_version\s*(?P<op>[<>=!]=?)\s*['"](?P<version>[0-9.]+)['"]"""
)


def _normalize(name):
    """PEP 503 normalisation, so Flask/flask and typing_extensions match."""
    return re.sub(r"[-_.]+", "-", name).lower()


def _release(version):
    """The numeric release tuple. Fails loudly on anything it cannot compare."""
    core = version.split("+", 1)[0]
    parts = core.split(".")
    out = []
    for part in parts:
        if not part.isdigit():
            # A pre/post/dev segment would need real PEP 440 handling. Nothing
            # in this closure has one; refuse rather than compare it wrongly.
            raise AssertionError(
                "cannot compare non-numeric version segment %r in %r; this "
                "guard needs extending before such a pin lands" % (part, version)
            )
        out.append(int(part))
    return tuple(out)


def _pad(left, right):
    width = max(len(left), len(right))
    return left + (0,) * (width - len(left)), right + (0,) * (width - len(right))


def _satisfies(version, op, bound):
    got, want = _pad(_release(version), _release(bound))
    if op == ">=":
        return got >= want
    if op == ">":
        return got > want
    if op == "<=":
        return got <= want
    if op == "<":
        return got < want
    if op == "==":
        return got == want
    if op == "!=":
        return got != want
    raise AssertionError("unhandled specifier operator %r" % op)


def image_python_version():
    """The interpreter the image runs, read from the Dockerfile's FROM line.

    Read rather than hardcoded so that a base-image bump moves this guard's
    marker evaluation with it instead of leaving it asserting about 3.14
    forever.
    """
    with open(DOCKERFILE, encoding="utf-8") as handle:
        for line in handle:
            match = re.match(r"^FROM\s+python:(?P<version>[0-9]+\.[0-9]+)", line)
            if match:
                return match.group("version")
    raise AssertionError("no `FROM python:<major>.<minor>` line in Dockerfile")


def _marker_applies(marker, py_version):
    """True when a `python_version` marker holds for the image interpreter.

    Only `python_version` markers appear in requirements.txt. Any other marker
    is treated as applying, which is the safe direction: it can only demand
    that a package be pinned, never excuse one.
    """
    if not marker:
        return True
    match = _PY_MARKER.search(marker)
    if not match:
        return True
    return _satisfies(py_version, match.group("op"), match.group("version"))


def parse_requirements():
    """[(name, [(op, version)], marker)] for every real line in requirements.txt."""
    entries = []
    with open(REQUIREMENTS, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith("-"):
                continue
            match = _REQ.match(line)
            assert match, "unparsed requirements.txt line: %r" % line
            specs = _SPEC.findall(match.group("specs") or "")
            entries.append(
                (match.group("name"), specs, (match.group("marker") or "").strip())
            )
    return entries


def parse_pinned():
    """{normalized name: version} plus the hash count for each pin."""
    pins = {}
    hashes = {}
    current = None
    with open(PINNED, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("--hash="):
                assert current, "--hash line before any pin: %r" % line
                hashes[current] = hashes.get(current, 0) + 1
                continue
            match = _PIN.match(line)
            assert match, "unparsed docker-runtime.txt line: %r" % line
            current = _normalize(match.group("name"))
            assert current not in pins, "%s pinned twice" % current
            pins[current] = match.group("version")
    return pins, hashes


def test_every_requirement_is_pinned_and_satisfied():
    """Each requirements.txt entry that applies on the image's interpreter is pinned."""
    py_version = image_python_version()
    pins, _ = parse_pinned()
    missing = []
    violated = []
    for name, specs, marker in parse_requirements():
        if not _marker_applies(marker, py_version):
            continue
        key = _normalize(name)
        if key not in pins:
            missing.append(name)
            continue
        for op, bound in specs:
            if not _satisfies(pins[key], op, bound):
                violated.append(
                    "%s is pinned at %s, which does not satisfy %s%s"
                    % (name, pins[key], op, bound)
                )
    assert not missing, (
        "requirements.txt names %s, which .github/requirements/docker-runtime.txt "
        "does not pin, so the image would not install it. Regenerate the set "
        "(see that file's header)." % ", ".join(sorted(missing))
    )
    assert not violated, (
        "the pinned set no longer satisfies requirements.txt:\n  "
        + "\n  ".join(sorted(violated))
    )


def test_every_pin_is_exact_and_carries_a_hash():
    """--require-hashes is only worth as much as the hashes actually present."""
    pins, hashes = parse_pinned()
    assert pins, "docker-runtime.txt pins nothing"
    unhashed = sorted(name for name in pins if not hashes.get(name))
    assert not unhashed, (
        "pinned with no --hash line, which --require-hashes would reject at "
        "build time: %s" % ", ".join(unhashed)
    )


def test_dockerfile_installs_the_pinned_set_with_require_hashes():
    """The wiring is the point; a pin no layer installs is decoration."""
    with open(DOCKERFILE, encoding="utf-8") as handle:
        dockerfile = handle.read()
    assert ".github/requirements/docker-runtime.txt" in dockerfile, (
        "Dockerfile does not COPY the pinned runtime set"
    )
    assert re.search(
        r"pip install[^\n]*--require-hashes[^\n]*docker-runtime\.txt", dockerfile
    ), "Dockerfile does not install docker-runtime.txt with --require-hashes"
    assert not re.search(
        r"^RUN pip install[^\n]*-r requirements\.txt", dockerfile, re.M
    ), (
        "the Dockerfile installs requirements.txt directly again, which "
        "re-introduces the unpinned resolve docker-runtime.txt replaced"
    )
