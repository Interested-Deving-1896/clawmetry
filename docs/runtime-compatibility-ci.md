# Cross-platform runtime compatibility

`runtime-compatibility.yml` verifies the exact candidate of `clawmetry-pro`
against this OSS checkout on standard Linux, Windows and macOS runners. Runtime
IDs come from `SUPPORTED_RUNTIMES.txt`; the workflow does not carry another list.
It currently runs adapter unit and recorded-fixture suites, not live provider
turns. The existing private live-conformance workflow remains in place.

## Selection and reuse

Known adapter, adapter-test and runtime-fixture edits select their runtime on
all three operating systems. Shared code, dependencies, new runtime names and
unknown paths select the entire catalogue. Only README.md, CHANGELOG.md and
.gitignore are explicitly cosmetic. An unavailable comparison base selects all
runtimes. Missing suites and entirely skipped suites fail rather than claim
coverage. Each runtime has a five-minute execution limit.

Suite discovery recognizes `test_<runtime>_adapter*.py`,
`test_adapter_<runtime>.py` and `test_<runtime>_runtime_adapter.py` in both
test roots. OpenClaw additionally runs OSS `test_openclaw_list_events.py` and
`test_openclaw_replay_events.py`, matching its existing suite family. Candidate
preparation checks installed-wheel metadata, the extension entry point and
import location before testing. Private JUnit input is size-bounded, DTDs are
rejected across XML encodings, and malformed reports fail verification.

Successful results are keyed by both repositories' indexed file contents, the
selected runtimes, operating system and interpreter series. A partial success
cannot satisfy a full-catalogue run. Only a success marker is cached. Manual
dispatch accepts an exact `pro_sha` (or resolves `main` once) and `force: true`
bypasses result reuse for a fresh dependency/platform check.

## Authentication and confidentiality

The public workflow requires `PRO_REPO_READ_TOKEN` with Contents read on the
private Pro repository, and `PRO_STATUS_TOKEN` with Commit statuses write there
to report dispatched results. Existing `CLOUD_REPO_PAT` is a migration fallback;
dedicated fine-grained credentials are preferable. Provider keys are not used.

Private fetch output, build output, wheel files, fixtures and pytest output stay
on the ephemeral runner. Git authentication is transient environment
configuration, never persisted in the checkout. The wheel is installed and the
adjacent source package is moved aside before testing. Raw JUnit is parsed
privately. Public output contains runtime IDs and passed/failed/timed-out/
missing-coverage/unverified statuses only. The selection artifact contains IDs,
hashes and OS labels, expires after one day, and contains no private files.

Pull requests to this public workflow run only the secret-free orchestration
guards. Candidate execution uses the trusted default-branch workflow through
manual dispatch, relevant main pushes or `pro-runtime-compatibility` repository
dispatch. Never use pull_request_target to execute public PR code with tokens.

## Pro dispatch contract

The private dispatcher sends `pro_sha`, `base_sha` and the PR number to the
public repository. For PRs the candidate is the PR head SHA, not GitHub's
synthetic merge SHA. The public workflow resolves the candidate once and posts
the final `OSS runtime compatibility` status to that exact private commit.
Superseded candidates of the same Pro PR share a concurrency group.

Install the public workflow first, prove a manual three-OS run, then configure
the Pro `OSS_CI_DISPATCH_TOKEN` secret with Contents write limited to the public
OSS repository. Verify dispatch and callback before setting the private
`OSS_RUNTIME_CI_ENABLED=true` variable. Do not remove existing private coverage
before its replacement passes. This path-filtered check is continuous coverage;
it must not enter an always-required aggregate without a no-impact reporting
path on every PR.
