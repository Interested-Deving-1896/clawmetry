# Process search and ClawMetry resource visibility

## Feature Summary

Implements [the process search requirements](https://factory.8090.ai/project/b415065f-ab2f-4f53-8864-0c009fd098cb/requirements/29fd5189-7479-4259-8b97-2f74a5d4031b). Users search all retained processes and inspect identified monitoring processes with the same evidence limits as the existing Node view.

## Component Blueprint Composition

The existing node activity pipeline remains collector -> daemon-owned DuckDB -> local API / encrypted nodeActivity snapshot -> browser. Source contracts are in clawmetry/node_activity.py, clawmetry/node_activity_store.py, routes/node_activity.py and clawmetry/sync.py. No request handler reads host processes.

## Feature-Specific Components

No new runtime component is introduced. Extend the existing `#NodeActivityCollector` in clawmetry/node_activity.py and `#NodeActivityView` in clawmetry/static/js/node-activity.js, composed through `#NodeActivityStore` and `#NodeActivityService`. The existing feature and composition blueprints define these components.

## System Contracts

clawmetry/node_activity.py adds optional clawmetry_role to recognized process rows. The collector samples its own process before bounded enumeration and deduplicates by PID/start-time identity. Roles never alter actor attribution. Existing CPU deltas and RSS measurements retain unknown, zero and stale distinctions. Current identified processes are retained before the general inventory cap. The store persists additive public fields unchanged and the existing encrypted nodeActivity snapshot carries them.

clawmetry/static/js/node-activity.js filters before slicing to a page of 100. Search, clear, previous and next operate on cached data. Search state survives data refresh and resets on node change. The dedicated section renders identified rows independently of the main search/page, explains RSS, and labels the observed subset rather than claiming total overhead. Older snapshots display guidance when role metadata is absent. The live template and feature stylesheet own accessible controls, status text and responsive layout.

## Architecture Decision Records

### ADR-001: Reuse cross-platform psutil

Context: OS names can identify Python rather than its application. Decision: reuse psutil Process metadata on macOS, Linux and Windows. Read arguments transiently only for plausible Python/ClawMetry processes; never serialize them. Use self PID to avoid relying on a guessed collector name. Consequences: inaccessible/unknown launches remain unlabeled; no new dependency or per-request collection.

### ADR-002: Per-process measurements

Context: partial collection and shared RSS make a single total misleading. Decision: show each observed monitoring process and state the subset and measurement semantics. Consequences: users can assess collector/dashboard costs without an invented total.

## Visual plan and review

Preserve the Node screen's existing dark/light theme tokens, type scale and mint accent. Add a restrained full-width ClawMetry section above the two inventory columns. Keep controls left aligned: labeled search input, clear button, result count, then previous/next. Use existing panel and table styling; focus uses the existing accent. On narrow screens the input and controls wrap without horizontal page overflow. No new decoration, animation, font or branding palette is needed for this task. The unique hierarchy is the direct view of monitoring cost, while the rest stays visually quiet.

Reference: https://psutil.io/ documents Process name, cmdline, cpu_times and memory_info across supported OSes. RSS is resident memory; process CPU uses elapsed counter deltas with one core equal to 100 percent.

## Live cadence addition

The hosted blueprint now also covers the htop-like resource view, two-second frames during bounded viewing leases, independent daemon worker, daemon-writer startup ownership, slow-source separation and encrypted cloud cache delivery. The 30-second history cadence is separate from live process metrics. The implementation remains on the existing Node components and HTTP routes.
