## Feature Summary

This correctness addendum implements [@Node activity current rows and partial positive sightings](https://factory.8090.ai/project/b415065f-ab2f-4f53-8864-0c009fd098cb/requirements/d33e1d0b-43c1-4d3f-8d0d-8de6628d0583). It fixes permanently capped inventories without treating incomplete observations as complete comparisons. It adds no OT integration, native execution sensor or process control.

### Cloud live viewing wake hint

The live cache read itself records bounded authenticated interest for the owning node. The existing wake response carries remaining node_activity_live_ttl to the independent delivery worker, which only renews the resource viewing lease. It executes no generic action on that thread. This avoids waiting for the main ingest heartbeat to deliver a viewing request. Presence expires within 40 seconds and contains no process details; measurements remain encrypted. Reuse both normal and Assistant-capable wake responses, preserving identity, epoch, command and stale-capability checks. Older collectors fall back to recorded snapshots rather than displaying a permanent live-starting state. The earlier sealed viewing operation remains compatible, but the fast browser read path needs no queued command or additional HTTP request.

## Live process measurement correction

Implements REQ-OBS-NODE-SEARCH-003 in the linked process search requirement. The user's live test found that a long ingest pass prevented timely CPU samples. Replace the ingest-loop-triggered Node collector with one idempotent daemon worker started after the writer is available and before cloud I/O/backfill, with bounded shutdown. Reuse the existing collector, writer, source caps, CPU identity checks and 120-second gap rejection. This corrects sampling rather than accepting stale CPU intervals.

clawmetry/node_activity_service.py owns a 30-second full observation cadence and a two-second resource/process cadence while an ephemeral viewer lease is active. Only the same daemon writer persists the latest frame, through additive methods in clawmetry/node_activity_store.py. These frames do not run event-history diffs or listener/settings collection. The stored API in routes/node_activity.py accepts a live query parameter and reads the persisted frame through the authenticated private method allowlist in routes/local_query.py. Requests renew a bounded viewing lease but never read host processes.

clawmetry/static/js/node-activity.js uses one active-tab request loop: bounded live frames about every two seconds and full history about every 30 seconds. It preserves search, pagination and event selection, presents live/sampling/delayed/snapshot state, and stops on hidden/off-tab/node changes. CPU bars represent measured usage, not synthetic motion. Initial warm-up and inaccessible measurements remain explicit; a healthy second sample produces actual CPU rates.

Hosted views reuse routes/node_activity_bridge.py in clawmetry-cloud: an authenticated sealed live-view operation renews the owning node's ephemeral remote lease. Live frames are AES-GCM encrypted on the node and published to the existing owner-bound cache via /ingest/cache, with bounded TTL and a one-frame queue. The browser decrypts /api/cloud/cache reads locally and checks node identity. There is no faster full-snapshot build or server-side decryption. No new public HTTP endpoint is required. Idle/off-tab leases expire after 40 seconds.

One independent worker replaces the prior ingest-loop poller; full expensive collection stays at 30 seconds. The two-second path is active-view only. The existing opaque action transport carries an observation lease, not an agent control or a persisted monitoring preference. Rollback stops the worker and restores the previous files; no schema migration is needed.

## Process search and ClawMetry resource visibility

Implements [@the process search requirements](https://factory.8090.ai/project/b415065f-ab2f-4f53-8864-0c009fd098cb/requirements/29fd5189-7479-4259-8b97-2f74a5d4031b). Users search all retained processes and inspect identified monitoring processes with the same evidence limits as the existing Node view.

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

## Node Evidence Clarity Design Addition: Approved Contract

Approved addition, with implementation and verification pending, to the existing collector -> daemon-owned DuckDB -> encrypted snapshot -> local/hosted view composition. Reuse existing routes, active-tab lifecycle, service cadence, source coverage, bounded inventories, private storage and encrypted mutation contracts. No new runtime service, dependency, polling timer, native sensor or privileged command. Earlier contracts and ADRs remain unchanged.

* Counts: retain nullable exact totals. Prefer explicit current observed counts from coverage/collector metadata; never count retained stale rows as current positives. Render an observed count even when an exact total is unknown. A partial source with zero accessible rows remains incomplete, while a complete measured zero can be stated as zero. Use existing `coverage.processes.count` and `coverage.listeners.count` as the authoritative current positive counts; existing nullable `summary.process_count` and `summary.listening_port_count` remain exact-total fields. Add no duplicate summary count fields. Old snapshots fall back only to evidence that distinguishes current rows from stale/unknown-age rows.
* CPU: use bounded daemon-lifetime sampling of cumulative user+system process CPU counters keyed by existing measured PID+start identity and source identity. Derive a rate over actual monotonic elapsed time, with explicit interval and denominator metadata; do not use a blocking sampling sleep. Clear or reject comparison after restart, identity change, omitted/unreadable prior sample or declared gap. Stale row timestamps and stale rate intervals remain historical. Use `100 * delta(user + system) / monotonic_elapsed`: 100% is one logical CPU and multithreaded work may exceed 100%. Add `cpu_interval_seconds` for a measured rate and `cpu_reason` for unavailable rates. Keep at most 512 retained process samples per sensor/source; reject elapsed intervals below 0.1 seconds or over 120 seconds, regressed/missing counters and disabled/source-change baselines. Retain process_iter.cache_clear for PID reuse; no priming or sleep.
* macOS listeners: only after primary permission failure or unsupported collection, use the platform's documented lsof machine-readable TCP LISTEN output through a fixed argument vector and absolute known binary, no shell or sudo. Apply strict subprocess deadline, bounded captured output and existing row cap; disable DNS/service-name lookups. Parse only required PID, numeric endpoint, protocol and LISTEN state; do not publish command arguments or infer actor identity. Use the fixed command `/usr/sbin/lsof -nP -a -iTCP -sTCP:LISTEN -F0pftnT`, bounded to 256 KiB, 0.75 seconds and the remaining shared budget/file-source reserve, with at most 256 listener rows. Report `coverage.listeners.method=lsof_polling` and a listener-only method-qualified source identity; a method transition starts a quiet comparison baseline. Stable endpoint/PID identities are scoped to that method/source. Leave process_id null unless independently verified, and wildcard exposure unknown. Fallback coverage remains partial, with explicit unavailable reason if the binary, permissions or budget prevents observations. It must never produce negative comparisons or actor claims.
* Event story: replace the generic Human/Agent/Unattributed-to-node category map with a selected-event narrative anchored to its original event ID/time/target. Explain observations and unknown identity plainly, preserve informational first-observed qualification, and keep before/after, process IDs and source evidence in progressively disclosed detail. Replay selects the same event/evidence/resource measurement. Keep current reduced-motion, keyboard, mobile and escaped-content guarantees; add no speculative actor attribution.
* Empty-source reasons: inventory components use the existing source coverage reason/state/method and an explicit coverage navigation action. Disabled/unavailable/partial-empty and genuine complete zero have different text. No privileged-install instruction or promise of permission that the account does not have.
* Validation: focused rate/identity/gap/first/restart tests; bounded machine-readable lsof parser/deadline/truncation/permission cases; no false negative event regressions; old/new snapshot UI contracts and rendered human-readable stories. Final owned harmless process/listener validation must pass the actual writer and local plus encrypted hosted path. Record official package and served-asset proof separately; component fixtures alone are not live delivery proof.

### ADR-NODE-PART-004: Prefer measured evidence and a plain event story

Context: A capped inventory can contain useful observations even when an exact total is unknown. Hardcoded unavailable process CPU and account-restricted socket reads leave observable activity unexplained. A category diagram can obscure the selected event and imply relationships the evidence does not establish.

Decision: Use existing source coverage counts for current observed rows, retain nullable exact totals, measure process CPU only over comparable identity-bound intervals, and permit only a bounded documented nonprivileged macOS listener fallback. Explain the selected original event in a plain story with progressive technical details and explicit missing attribution; keep replay and evidence selection synchronized.

Consequences: Counts, rates and empty lists carry their actual scope and measurement limits. CPU warm-up, gaps and denied listener sources remain unavailable when evidence is absent. No privileged probes, native execution sensor, new polling loop or external/OT integration is introduced. Harmless owned process/listener verification must cross the actual writer, local view and encrypted hosted path before delivery is claimed.

## Hosted Action Acknowledgement Ownership Addendum

**Status: approved minimal design; implementation, release and hosted verification pending.** This section addresses REQ-GOV-NODE-ACK-001 in the linked correctness requirement. The prior merged-main references above describe the partial-observation correction; they are not evidence that this acknowledgement correction has shipped.

### Observed failure and required ownership

A single hosted Govern save arrived through both durable PostgreSQL delivery and the fast relay approximately 0.66 seconds apart. The original delivery claimed the nonce and applied the requested state. A later duplicate returned a failure and posted it under the same action acknowledgement key, replacing the original result. The browser correctly required confirmation and reported the save as unconfirmed; this design changes the duplicate execution/result path, not that browser standard.

Only the execution that originally claims a nonce owns its action result. An already-claimed delivery must stop without mutation and without publishing a replacement acknowledgement, including a duplicate-failure or expiry-failure acknowledgement. Duplicate recognition must take precedence over an expired-envelope failure while the existing retained nonce claim still provides valid duplicate evidence. The original claimant's success or failure result remains stable against later duplicate delivery.

### Minimal integration and failure boundaries

Reuse the current bounded nonce claim tracking, existing action-result cache and encrypted acknowledgement transport. Preserve the 512-nonce bound and existing TTL/cache retention; add no receipt table, service or unbounded history. Perform duplicate classification within the existing claim ownership boundary before any duplicate path can manufacture a posted error result. Retain ordinary validation and expiry rejection for a genuinely unclaimed action. No secrets, decrypted action payloads or new plaintext cloud metadata are introduced.

An original claimant that crashes, fails application or cannot publish a confirmed persisted result leaves the browser unconfirmed. A duplicate is not an automatic recovery executor and cannot publish a substitute result. The operator must refresh/check the node and issue a fresh request when needed; the system must not silently retry the claimed action or claim that aborting confirmation undid it. This is bounded within-retention duplicate suppression and result ownership, not perpetual exactly-once execution or a new durable receipt guarantee.

### Focused validation

Exercise one nonce delivered through both relay paths and prove one mutation plus one original-owner result. Deliver further duplicates after a confirmed original success and after an original failure; prove no mutation and no replacement acknowledgement in either case. Deliver an expired duplicate while its nonce claim is valid and prove the cached original result is unchanged. Simulate an original crash/apply failure/result-publication failure and prove that duplicate delivery cannot retry, manufacture confirmation or replace the original result. Keep the existing nonce bound and retention tests. Harmless integration verification must distinguish a confirmed persisted result from pending/unconfirmed delivery; no live completion is claimed by this design record.

### ADR-NODE-PART-003: Original nonce claimant owns acknowledgement

Context: Two legitimate transport paths can deliver the same hosted action. Suppressing a second mutation is insufficient if the duplicate can overwrite the action's cached result and turn an applied save into an unconfirmed one.

Decision: Keep the original nonce claimant as the sole result owner. Suppress already-claimed duplicates before expiry/error publication, within the existing bounded nonce-claim retention. Do not introduce durable receipts or automatic replay.

Consequences: Duplicate delivery cannot replace a valid original result. A failed or crashed original attempt can remain unconfirmed and needs a fresh operator request; the existing UI must continue to report that uncertainty honestly. The original process-observation contracts and both earlier architecture decisions are unchanged.

## Component Blueprint Composition

This addendum extends the existing [@Node activity composition](https://factory.8090.ai/project/b415065f-ab2f-4f53-8864-0c009fd098cb/blueprints/72d9ec38-2671-4258-a5ad-ffe36c84b27c) and [@feature blueprint](https://factory.8090.ai/project/b415065f-ab2f-4f53-8864-0c009fd098cb/blueprints/30fa3bd8-d322-4b39-8674-6a86d73fb229). Their contracts for process identity, unknown attribution, private persistence, encrypted synchronization and complete-comparison gap handling remain in force. In particular, the existing ban on inferred removals or recovery from incomplete scans is unchanged.

`#NodeActivityCollector` continues to send a bounded source-qualified batch to `#NodeActivityStore`. No collection cap or process candidate budget increases. `#NodeActivityStore` prioritizes the current batch in the public inventory and separately tracks positive process sightings. `#NodeActivityView` presents the resulting row times, first-observed evidence and coverage limits using the existing stored API response.

## Feature-Specific Components

No new runtime component is introduced. The existing `NodeActivityStoreMixin` gains private durable process-sighting state that is independent from the complete-comparison `source_state`. Existing metadata helpers or a bounded private table remain within the same daemon-owned DuckDB writer boundary; no new persistence service or dependency is needed.

### Public inventory merge

For every partial entity source, deduplicate and place incoming rows first, stamp `observed_at` from the source scan and set `stale=false`. Append only prior rows not in the current batch, preserving their last `observed_at` and setting `stale=true`; legacy times remain null rather than being replaced with the current scan time. Apply that source's public row cap after the merge. Existing partial/unknown aggregate semantics remain unchanged.

### Private process-sighting ledger

Keep source identity, quiet initialization state, sticky `history_limited` state, and a bounded mapping from stable process identity to its last positive observation time. The identity includes the existing PID plus measured start identity and source identity. Update last-positive time for observed known identities. Prune records outside the event-retention window, normally 24 hours, and cap the ledger at 16,384 identities.

A first readable data-bearing scan is a quiet positive baseline, including migration from an install without the new ledger. Later partial scans can emit a first-observed event only for an identity that can be durably retained in the active history context. Persist the ledger atomically with observations and events so restart cannot replay an already recorded sighting. The complete source-comparison baseline remains separate and is discarded/re-established according to the existing gap contract.

An unavailable, disabled, unsupported or empty partial scan resets positive initialization so the next readable scan is quiet. For the same source identity, preserve all unexpired known dedup keys across this reset, restart and monitoring disable/re-enable. A genuinely changed source identity establishes a separate quiet current epoch. Partial/complete transitions do not erase unexpired identity knowledge.

### Saturation and safe reset

At capacity, retain all unexpired known identities and suppress positive events for unknown identities that cannot be retained. Incoming public rows still remain fresh and visible. Set `sighting_history_limited=true` and add an explicit coverage reason that positive-sighting history is incomplete.

This limit is sticky. Pruning, temporary free capacity, a same-source gap, restart or re-enable cannot clear it or cause an untracked saturated identity to masquerade as a new first sighting. Clear the limited state only through a quiet complete scan whose full comparison/dedup set fits the ledger, or a genuinely new source identity with its own quiet epoch. A quiet reset records no retrospective removals, recovery or first-observed events.

### Positive event contract

Use `kind=process_observed`, title `A process was first observed`, severity `info`, `finding=false` and unknown actor unless independently supported attribution exists under the unchanged parent contract. Detail and evidence must say first observed within retained history under partial collection, not lifetime first appearance or a proven process start. Preserve the positively measured process row as evidence; no absent prior row is proof that the process was absent. The existing event list, replay and encrypted snapshot can carry this informational event without inventing sessions or exposing arbitrary PID controls.

### Visible age and coverage

Use inventory headings that describe observations rather than promising that every row is current. Processes, listeners, selected settings and login evidence show their row observation time or an explicit unknown-time state when stale; a fresh current batch does not refresh the age of an old retained row. Existing coverage rendering must show the reported positive-history limit. No new browser clock or poller is needed.

## System Contracts

### Key Contracts

* Current positive rows take priority over stale history within every source's existing cap.
* First-observed sightings are positive evidence only. They do not assert actual starts, complete inventories, removals, recovery, trusted human identity or attacker intent.
* Same-source retained identity knowledge survives cap rotation, restart, gaps and re-enable; quiet initialization is a separate flag.
* Identity state is bounded by the retained-history window and a 16,384-record capacity. Saturation fails closed for new positive events and remains visible until a safe quiet reset.
* A partial scan never becomes a negative comparison. The next complete scan after a partial/gap re-establishes the complete baseline quietly under the existing contract.
* Internal identity ledgers and source-comparison state remain private DuckDB data. Public rows and events contain no command arguments, environment values, secret contents or reusable file fingerprints.
* This is a correction to stored evidence semantics. Existing daemon cadence, route read-only collection boundary, authentication and encrypted cloud path remain unchanged.

### Integration Contracts

* Public entity rows add `observed_at` and explicit `stale` state without changing the existing API endpoint.
* Process coverage adds `sighting_history_limited` plus a factual reason; complete/partial/unavailable state still describes collection coverage independently.
* The event stream accepts `process_observed` through existing generic evidence/replay rendering. Positive-sighting identities and event dedup are persisted within the writer transaction.
* No live host collection is added to Flask routes and no new cloud plaintext metadata or action endpoint is introduced.

### Validation

Use focused tests for a full stale public cap followed by a new partial incoming process, per-source row caps and legacy unknown row times; quiet initial/migrated partial baseline; later first positive sighting; cap rotation, restart and same-source gap/re-enable dedup; source change quiet baseline; PID reuse under the existing identity contract; sticky capacity exhaustion and safe complete rebaseline; unchanged no-removal/no-recovery semantics; and stored UI row-time/coverage-limit rendering. Verify a harmless real process is visible and produces an informational positive sighting on an already-capped monitored node without using a synthetic seed as release proof.

## Architecture Decision Records

### ADR-NODE-PART-001: Separate positive sightings from complete comparisons

Context: A host can remain over the process cap indefinitely. Waiting for complete scans discards useful positive evidence, while treating partial absence as a change creates false events.

Decision: Maintain a separate bounded durable positive-sighting ledger and incoming-first public inventory. Keep the existing complete-comparison state machine unchanged.

Consequences: Operators can see observed work on capped hosts. Events explicitly describe retained-history sightings, while negative conclusions still require complete comparable evidence.

### ADR-NODE-PART-002: Keep incomplete history explicit at capacity

Context: Evicting an unexpired dedup key to admit a new one can replay an old process as a first sighting during cap rotation or restart.

Decision: Preserve known identities and suppress untrackable positive events. Retain a sticky history-limit indication until a safe quiet complete rebaseline or a genuinely new source identity.

Consequences: The system may omit positive events while history is limited. It states this gap rather than fabricate novelty or expand storage without a bound.

## Merged Code References

Implementation merged through [PR 6419](https://github.com/vivekchand/clawmetry/pull/6419) as [commit 1b5861720024](https://github.com/vivekchand/clawmetry/commit/1b586172002466aa6f992f9131950e1f08e188cd). These links resolve to the merged main implementation; line anchors were checked against that merge commit. This section records implementation traceability only. Release publication and hosted verification for this correction remain pending; merge and passing CI do not establish either result. The contracts and architecture decisions above remain unchanged.

| Concern | Merged main reference |
| --- | --- |
| Incoming-first inventory and per-row age | [Current-first public projection](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/node_activity_store.py#L36) |
| Qualified partial positive and bounded durable identity state | [First-observed event](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/node_activity_store.py#L47); [Readable-source boundary](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/node_activity_store.py#L62); [Private sightings and sticky limit](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/node_activity_store.py#L67) |
| Atomic writer integration | [Persisted observation transaction](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/node_activity_store.py#L193) |
| Inventory, positive-event and gap regressions | [Each-source cap priority](https://github.com/vivekchand/clawmetry/blob/main/tests/test_node_activity.py#L377); [Qualified private sightings](https://github.com/vivekchand/clawmetry/blob/main/tests/test_node_activity.py#L403); [Restart, gap and re-enable dedup](https://github.com/vivekchand/clawmetry/blob/main/tests/test_node_activity.py#L425) |
| Saturation and actual disabled-collector boundary | [Sticky saturation and quiet reset](https://github.com/vivekchand/clawmetry/blob/main/tests/test_node_activity.py#L456); [Real disabled-batch regression](https://github.com/vivekchand/clawmetry/blob/main/tests/test_node_activity.py#L577) |
| Visible row time and incomplete history | [Inventory row ages](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/static/js/node-activity.js#L131); [Independent coverage-limit presentation](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/static/js/node-activity.js#L139); [Observed inventory headings](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/templates/tabs/node-activity.html#L16) |
| Actor map correction | [Actor slot without a connection and qualified map caption](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/templates/tabs/node-activity.html#L14); [Invisible actor gap](https://github.com/vivekchand/clawmetry/blob/main/clawmetry/static/css/node-activity.css#L42) |
| Executed UI evidence | [Fresh, stale, legacy and limited-history render assertions](https://github.com/vivekchand/clawmetry/blob/main/tests/test_node_activity_js.js#L185); [Rendered unknown, Human and Agent map guard](https://github.com/vivekchand/clawmetry/blob/main/tests/test_node_activity_browser.py#L78) |

## Final Delivery Evidence: Official 0.12.921 and Hosted Revision Verified

Recorded 15 October 2026. This dated delivery entry supersedes earlier pending delivery statuses for the implemented node-observation and acknowledgement corrections. All existing acceptance criteria, contracts, architecture decisions and code references remain unchanged. The separate external/OT/native-sensor proposal remains research-only. Verification succeeded with the unresolved first-attempt confirmation limitation below; this is not a claim that every attempted save confirmed successfully.

### Merged implementation and immutable acknowledgement references

The acknowledgement correction merged in [OSS PR 6426](https://github.com/vivekchand/clawmetry/pull/6426) as [5572ebc083cf](https://github.com/vivekchand/clawmetry/commit/5572ebc083cf3be437b34bea46f6f600a3abc5b8). The following immutable line references were checked against that commit; the retained nonce claim, not an independently longer-lived acknowledgement cache, remains the duplicate-recognition boundary.

* [Original-claimant execution and acknowledgement ownership](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/clawmetry/sync.py#L11175)
* [Duplicate keeps the original persisted confirmation](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L229)
* [Changed-body and expired retained duplicate](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L246)
* [Restart duplicate suppression](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L267)
* [Original failure and incomplete claim remain unconfirmed](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L278)
* [Lost publication cannot be replaced by a duplicate](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L303)
* [Concurrent deliveries apply and acknowledge once](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L317)
* [Review duplicate preserves one review](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L334)
* [Retained-claim boundary preserves unclaimed expiry](https://github.com/vivekchand/clawmetry/blob/5572ebc083cf3be437b34bea46f6f600a3abc5b8/tests/test_node_activity_wiring.py#L348)

### Official package and installed node

* Release [PR 6429](https://github.com/vivekchand/clawmetry/pull/6429) merged at [a19bbff136ba](https://github.com/vivekchand/clawmetry/commit/a19bbff136babaf5715bedac99f78b41f2c181c3), with 45 successful active checks and one intentional OpenSSF skip reported by root. The publisher was [run 38757308656](https://github.com/vivekchand/clawmetry/actions/runs/38757308656).
* The inspected official package is `clawmetry==0.12.921`, wheel `clawmetry-0.12.921-py3-none-any.whl`, SHA256 `65b8dfc4a2135c56c3b0979256aac4d92fb4e1428bdaec9ff9c25f2170423406`. The official PyPI index entry and psutil dependency were verified. Seven feature assets and eight marker files were inspected; the store, Node JavaScript, Node CSS, Node template and sync relay matched the five reviewed file hashes. The Factory reviewer independently recomputed the wheel and these content hashes.
* Root installed the official package, restarted both sync daemon and dashboard, and reverified installed metadata `0.12.921` and all five file hashes. Actual fresh encrypted observations retained one owned positive process sighting and its owned historical review. Attribution remained unknown; no seeded telemetry was used as release proof.

### Cloud pin, deployment and served artifact

* Automatic cloud [PR 2624](https://github.com/vivekchand/clawmetry-cloud/pull/2624), reviewed head `aadd025683d4897a96e6b30d7192649a37756582`, changed only the Dockerfile pin from `0.12.920` to inspected `0.12.921`. Independent exact-head review approved it; 97 independently executed compatibility tests and 132 cloud-author focused tests passed. Route audit reported zero errors, with one existing stale onboarding-readiness warning.
* All 55 cloud PR checks passed. Merge commit is `4ef7ea6e67d192be5b7ebbda9794fd98e60c9533`. [Deployment run 38760731274](https://github.com/vivekchand/clawmetry-cloud/actions/runs/38760731274) completed successfully through its candidate gates. Root verified revision `clawmetry-cloud-03922-rer` receives actual 100% traffic.
* Deployed image: `gcr.io/openclaw-mc/clawmetry-cloud@sha256:057d3571a8c1166a99db8993b01ebdacb9b4642d640811e07209f7487cb6176d`. Root fetched the production Node JavaScript; its SHA256 `7016b1ac674cebc74da498212a83f20d04e3361c848cb01b2ee4d383fc5d78d4` matches the inspected wheel. The reviewer independently checked that artifact equality from the proof and wheel.

### Actual hosted verification and retained limitation

Root reloaded the actual hosted tab at the promoted revision and verified Observe, the owned review in Govern, Guard findings and navigation to the existing Guard checks. Replay advanced through actual recorded events. The unknown-actor connector stayed hidden. A screenshot was emitted and the hosted tab marked deliverable; the final browser check recorded zero new console errors.

The first post-promotion save was unconfirmed in the browser although its encrypted node result had succeeded after two deliveries. The exact cancellation or confirmation-loss trigger remains unestablished. This attempt is retained as a verification limitation; it was not erased, treated as an undone mutation or claimed to have succeeded in the browser.

After an explicit Refresh, root issued a fresh same-values save. The browser showed `Saved on this node`. Its encrypted persisted acknowledgement still reported `ok=true`, `saved=true` and `applied=true` after two deliveries, with the correct node binding and all six monitoring preferences unchanged. A fresh encrypted snapshot retained the owned sighting/review. This confirms the new request and duplicate-result ownership path; it does not explain or retroactively confirm the earlier browser attempt. No product edit was made to manufacture this result.

The underlying sanitized verification artifacts are `published-wheel-proof.json`, `official-hosted-proof.json` and `cloud-deployment-proof.json`; browser screenshots remain with root. No credentials, raw node telemetry or decrypted snapshot contents are reproduced here. Evidence was supplied by root for actual production interactions; the Factory reviewer checked artifact hashes, immutable code anchors, proof consistency and the exact pin, rather than claiming to have operated root's browser.

## Current frontend implementation contracts

The proposed implementation in OSS PR 6519 delegates inventory rendering into named functions. In clawmetry/static/js/node-activity.js, renderInventory(data) calls renderProcesses(data) and renderClawmetry(data). renderProcesses filters every retained row by state.processQuery before sorting and slicing by state.processPage, and updates the result count and navigation controls. renderClawmetry filters rows through processRole and populates na-clawmetry-processes. Those contracts satisfy AC-OBS-NODE-SEARCH-001.1 and AC-OBS-NODE-SEARCH-002.2. They are not implemented inline in renderInventory.

The same file's schedule() runs one active-view timer at 2000 milliseconds while live updates are supported. load(force, live) adds ?live=1 on that timer's lightweight reads; a full history refresh is requested every 30 seconds. The ten/fifteen second interval is only the compatibility fallback for an older collector after five live misses. New collector capabilities.live_metrics prevents that downgrade. These contracts satisfy AC-OBS-NODE-SEARCH-003.1 and preserve explicit snapshot fallback.

Cloud viewing presence uses the existing authenticated encrypted-cache read, not a queued command: routes/node_activity_bridge.py:liveRead reads node_activity_live:owner:node, routes/heartbeat_relay.py:read_cache invokes touch_node_live_view after exact owner/node checks, and the existing wake response carries bounded node_activity_live_ttl. clawmetry/assistant_relay.py applies only that bounded observation hint on its wake worker. This is independent of the slow ingest loop; no generic action runs on the wake worker.

