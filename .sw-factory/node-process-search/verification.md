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
