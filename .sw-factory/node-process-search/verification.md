# Candidate verification

The implementation uses the existing local API and encrypted nodeActivity snapshot. It adds no endpoint, timer or dependency. Own-process observations are sampled before bounded enumeration and use the existing PID/start-time CPU comparison. Software labels do not change actor attribution.

## Evidence

- Focused unit, store, wiring and JavaScript lifecycle suite: 113 passed, one real listener test excluded after its owned socket could not start in this sandbox.
- Regression proof against original source: 17 new collector/recognition cases failed and the new JS pagination/result-count assertion failed. Restored candidate passes.
- Live Jinja template renders the search controls, pagination and monitoring-usage section with unique element IDs.
- JavaScript syntax, whitespace, English mechanical check and acceptance traceability pass. Coverage is 436/504, with the existing 68 uncovered unchanged.
- New isolated browser tests cover widths 320 and 1280, role visibility, search beyond the first hundred rows, PID/name/role search, refresh preservation, clear, escaping, page navigation and no search-triggered fetch. Execution awaits an environment that can launch Chromium.
- New Python has no added Ruff findings. Seven existing BLE001 findings in the collector remain unchanged.

## Delivery limits

macOS denies this session access to process enumeration (sysctl) and the owned socket listener. The browser subprocess fails with MachPortRendezvousServer permission denial. The connected browser can inspect the installed Node page, which still shows the old capped list, but its security policy rejects local file preview URLs. No attempt was made to bypass that restriction.

The local requirements and blueprint were written before source implementation. Hosted Factory publication is pending because the configured keychain API credential was unavailable on the subsequent request. New manifest entries explicitly identify their local source.

This candidate is not merged, released, installed or verified live. Do not claim production completion. Before merge, run the browser and real-process checks with permitted host access, publish the Factory records, and verify the encrypted hosted path. Then follow FLYWHEEL.md for green CI, release, cloud pin and served-artifact verification.

## Publication attempts

The local Git add/commit attempt failed because this session cannot create .git/worktrees/process-search/index.lock. The GitHub connector also refused branch creation with HTTP 403, Resource not accessible by integration. No remote branch or pull request was created. Changes remain in the isolated worktree, on feat/process-search-self-usage, without a new local commit.

## Permissions restored and release validation

The earlier sandbox/publication limitations are resolved for this continuation. All 117 focused tests now pass, including the real process/listener check and both browser viewport tests. The actual installed dashboard and collector are identified by the new recognizer. Hosted Factory requirement 29fd5189-7479-4259-8b97-2f74a5d4031b and blueprint 2dffd534-2073-4af2-b943-d6dbed701ee1 version 8 are published and verified. Manifest entries now cite the hosted requirement. Git commit and push succeeded, and release delivery is in progress. Earlier limitations remain here as historical evidence only.

## Live cadence acceptance

The user requested htop-like behavior after seeing a 139-second CPU comparison gap. Tried the installed htop with a one-second refresh. The expanded requirement and blueprint were published before the cadence correction. One independent worker now samples live resource frames every two seconds during a bounded viewer lease, with full observations every 30 seconds. The ingest-loop trigger was removed. The first installed test exposed a startup proxy handle; the worker now reacquires the writer after the local service marks ownership, and refuses read-only proxies.

Actual installed API frames advanced by 1.941 and 1.890 seconds. The live local browser displayed measured collector/dashboard CPU, changing resident memory and CPU bars while preserving the ClawMetry search. Browser live state reads Live, every 2 seconds. CPU gap rejection and PID/start-time checks remain intact. Targeted tests cover blocked ingest, lease expiry, slow-source exclusion, private RPC auth, live JS updates and ephemeral sealed viewing requests. Cloud tests cover sealed leases, encrypted frames, owner/node binding and no repeated full snapshot fetch.
