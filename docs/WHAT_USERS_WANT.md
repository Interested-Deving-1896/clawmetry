# What Users Want — September 2026 Edition

*Auto-generated weekly by the roadmap synthesis bot. Last updated: 2026-09-25 09:00 UTC. Aggregates signal across both `vivekchand/clawmetry` (OSS) and `vivekchand/clawmetry-cloud` (cloud).*

> **Cloud data note:** Cloud repo inaccessible this run (GitHub session scope limited to OSS repo). Open cloud issues and cloud PRs are carried forward from the 2026-09-18 synthesis. Only OSS-visible changes are new this week.

---

## TL;DR (this week)

This week shipped meaningful usability wins — Qwen Code moved to the free tier, the dashboard opens on the Agents roster by default, and OpenClaw native approvals reached the Approvals tab. Guard got a correctness fix (a secret read and then sent out in one command now correctly surfaces as critical). On the uncomfortable side: **the two OTLP correctness bugs (#5938, #5949) are now entering their second week open with no PR.** Every enterprise OTel user is still sending span tool calls that Guard never sees, stored unredacted. A second week without a fix is the point at which this stops being a new bug and starts being a shipping gap.

---

## Hot themes (build these next)

### 1. OTLP Telemetry Correctness — Spans Bypass Guard and Durability Broken

- **Demand**: 2 open `bug` issues (P0 + P1), 7 open `enhancement` issues on schema completeness; 18+ comments across the bugs. Filed 2026-09-13–17.
- **Representative quotes**:
  - *"Guard reads `store.query_events`, but spans go to a separate spans table via `put_span`. No detector ever sees them. [...] Redaction runs only in `LocalStore.ingest`. Span input/output/attributes are stored as received."* — `clawmetry#5938` (P0, 13 comments)
  - *"Never return an unqualified success after silently losing accepted records; follow OTLP partial-success/retry semantics and document rejected counts."* — `clawmetry#5949` (P1, 5 comments)
  - *"Extend existing spans storage to composite identity, resource/scope/schema provenance, links, events, status, timestamps and content policy; migrate existing rows safely."* — `clawmetry#6071` (schema completeness)
- **Why it matters**: The enterprise readiness push shipped LiteLLM, CI/CD provenance, and self-hosted signed images. Every enterprise customer integrating via OTel — LangGraph, Azure AI Foundry, AWS AgentCore — is sending telemetry into a layer that (a) never routes their span tool calls to Guard and (b) stores prompt text unredacted. This week's Guard fix (#6161/#6162) shows the detector path is actively maintained — the span normalization fix belongs on the same track. A partial fix shipped (#6009) but the P0 bug (#5938) remains: the canonical test (canary command through the normalized span path) has not landed. The durability bug (#5949) means a restart after accepting valid items loses those items.
- **Linked issues**: `clawmetry#5938` (P0), `clawmetry#5949` (P1), `clawmetry#6071`, `clawmetry#6072`, `clawmetry#6073`, `clawmetry#6074`, `clawmetry#6075`, `clawmetry#6077`
- **Likely scope**: OSS — `clawmetry/sync.py`, `clawmetry/local_store.py`, Guard detector path
- **Suggested first step**: Close `clawmetry#5938` first: normalize tool-call spans into the existing event contract so Guard evaluates them, and run redaction before storage. The test requirement is a canary that does not execute a destructive command — this is a one-PR scope.
- **Weeks open**: **2** ⚠️ (P0 entering second week without a PR)

---

### 2. Session Replay — Runtime-Aware Transcript Viewer

- **Demand**: 3 open OSS issues (`clawmetry#4814`, `#4815`, `#4816`), first filed 2026-08-14. No external user reactions (early signal, but architecture-level: the current viewer is demonstrably broken for multi-agent sessions).
- **Representative quotes**:
  - *"Claude Code is the highest-fanout runtime we support — sessions with 20+ Agent/Task calls. Today the transcript viewer shows the parent turn with a single collapsed 'Task' tool chip — the child's actual work is never inlined."* — `clawmetry#4815`
  - *"Today the session UI shows nothing about how a session ran: Auto vs interactive vs plan vs `--dangerously-skip-permissions`. Approvals asked count is stored but the transcript viewer never fetches it."* — `clawmetry#4814`
  - *"OpenClaw has the richest on-disk trace of any runtime we support — a purpose-built `acp_replay_events` stream, plus normalized tables. We ignore all of it and render the flat JSONL."* — `clawmetry#4816`
- **Why it matters**: ClawMetry's core claim is "observe what your agent actually did." The transcript viewer is where that claim is either demonstrated or disproved. For any Claude Code session with subagents, it disproves it: sub-agent trees collapse to a single chip, permission mode is invisible, workflow fanouts vanish. The Dashboard-opens-on-Agents (#6105) shipped this week — users now land directly on their agents list and click through to the transcript. The transcript view they land on is still in 2023 architecture. The gap between the improved entry point and the broken destination is now more visible, not less.
- **Linked issues**: `clawmetry#4814`, `clawmetry#4815`, `clawmetry#4816`
- **Likely scope**: OSS — `routes/sessions.py`, `clawmetry/local_store.py`, `replay_events` table
- **Suggested first step**: The canonical schema and `replay_events` table design (from `clawmetry#4813`'s architectural write-up) is the dependency. Ship it first, then the runtime-specific mappers (#4814–#4816) stack on it.
- **Weeks open without a PR**: **6** ⚠️

---

### 3. Cost Enforcement — Budget Alerts and Spend Digest

- **Demand**: 9+ open issues across both repos (3 OSS proxy issues + 6+ cloud intel issues carried from 2026-07-31). *[Cloud intel signals carried — unverified against current open issues.]*
- **Representative quotes** *(carried; cloud issues inaccessible)*:
  - *"Just a number climbing in silence while five engineers stared at dashboards that gave us totals and nothing else."* — `clawmetry-cloud#1683`
  - *"I use LLMs daily… I just can't figure how to burn that much money a month responsibly."* — `clawmetry-cloud#653` (HN 474-comment thread)
  - *"By step nine you have a context window the size of a small novel and a per-call cost that has tripled because cache writes accumulated."* — `clawmetry-cloud#655` ($47K retroactive bill)
- **Why it matters**: Significant progress shipped in prior weeks: per-project attribution and budgets (#5968 OSS), project cost report + finance reader + CSV export (cloud), cost basis labels everywhere (#5975, #6000), contract-rate price book (#6008). These cover the "visibility" half. The "enforcement" half — graduated budget alerts (50%/80%/95%), weekly spend digest to Slack/email, hard caps before the limit — remains unshipped. Nothing in the last 30 days of merged PRs touched the alert path. A budget row with no alert is an accounting record, not a control.
- **Linked issues**: `clawmetry-cloud#1683` *[carried]*, `clawmetry-cloud#653` *[carried]*, `clawmetry-cloud#655` *[carried]*, `clawmetry#2816`, `clawmetry#2817`, `clawmetry#2818`
- **Likely scope**: Both — OSS proxy gets enforcement rules; cloud gets alert delivery + digest
- **Suggested first step**: Graduated budget alerts at 50%/80%/95% of the per-project budget already stored in `clawmetry#5968`. The budget row exists; the alert evaluation path does not.
- **Weeks unaddressed (alert/digest half)**: **15+** ⚠️

---

### 4. P0 Security — Plaintext API Keys in Production DB ⚠️ *[carried, 23+ weeks]*

- **Demand**: 1 issue (`clawmetry-cloud#315`, labeled `bug`, filed **2026-04-14**). Cannot be verified closed — cloud issues inaccessible. No cloud PRs this week with explicit API key migration.
- **What it says**: `users.api_key` stores raw `cm_*` tokens in cleartext in the production database. Anyone with database read access — backup access, GCP logs, support tooling, a developer credential — can impersonate any user.
- **Why it matters**: 23 weeks open through active paying customer growth. Estimated fix: 1 day (bcrypt stored keys, one-time migration). Carrying forward until cloud issues are readable and this can be confirmed closed.
- **Linked issues**: `clawmetry-cloud#315` *[carried — status unverifiable]*
- **Likely scope**: Cloud only
- **Suggested first step**: Bcrypt stored keys with a one-time migration.
- **Weeks open (if still open)**: **23+**

---

## Warm themes (worth tracking)

- **Jev evaluator integration** (`clawmetry#6121`, `clawmetry#6122`): **New this week (Sep 20).** Two planning issues filed: observe Jev decision requests with accurate usage/attribution, and versioned advisory assessment contracts + encrypted snapshot support. `bot-plan-only`, unassigned. No reactions, no external user demand yet — internal scope expansion from the WO-MON planning series. Worth watching: if Jev is a near-term release, these need PRs within 2 weeks.

- **Agent Kill-Switch / Guard Control** (`clawmetry-cloud#4`): Substantially addressed in prior weeks (Cloud Guard lists sessions and supports Pause/Stop/Kill). This week's Guard fix (#6161) improved correctness. Remaining: proxy enforcement at port 4100. If `clawmetry-cloud#4` was satisfied by the control landing, close it.

- **Evals — LLM-as-judge** (`clawmetry#1619`): **18+ weeks open, 0 PRs.** Score-first reordering and session drill-down shipped in August. The original ask — auto-scoring with configurable rubric, local, on every completed session — remains unbuilt. The UI shell exists; the evaluator doesn't. At 18 weeks without a PR, a decision is warranted: first PR or explicit close.

- **ClawMetry Dives — AI SQL→Chart** (`clawmetry#999`): **19+ weeks open, 0 PRs.** NL question → SQL → chart over local DuckDB. No movement. DuckDB is more established than ever; the backend endpoint is the missing piece. Same situation as Evals.

- **Outcome Provenance / Delayed Feedback** (`clawmetry#6077`): **1 week old.** Extend `git_outcomes` and cohort infrastructure with explicit outcome/feedback records, attribution confidence, revision, delay and missingness. Enterprise-relevant; depends on OTLP schema completeness.

- **Off-box Ingest SDK** (`clawmetry#4779`, `clawmetry#5679`): Partial ship. Ingest key + generated contract + setup prompt + live status landed. The full SDK and auto-detection remain open.

- **Windows daemon stall on Python 3.13** (`clawmetry#5932`): Still open. Note: the Windows uninstall fix (#6138/#6151) this week addressed a *different* stall (per-file UI logging during uninstall). The `daemon_ingest_stalled` on Python 3.13 at runtime is a separate issue with 14 comments.

---

## Closed-loop themes (we shipped this)

**New since 2026-09-18 (this week's substantive merges):**

- **Qwen Code free tier** (`clawmetry#6110`, `clawmetry#6112`, merged Sep 2026): Qwen Code moved from paid to free and its reader shipped in the OSS package. Meaningful competitive positioning.

- **Dashboard opens on Agents roster** (`clawmetry#6105`, `clawmetry#6106`, merged Sep 2026): Default landing page changed from Sessions list to Agents roster. Direct response to the core use case: users run agents, not individual sessions.

- **OpenClaw native approvals** (`clawmetry#6102`, `clawmetry#6123`, merged Sep 2026): OpenClaw's pending approvals now surface in the Approvals tab.

- **Guard correctness: secret read + egress = critical** (`clawmetry#6161`, `clawmetry#6162`, merged Sep 2026): A credential exfiltration pattern (read a secret, send it out in one command) now correctly surfaces as `critical`. Also: env dump naming other services' tokens is now `warning` not `critical` (reduced noise).

- **Windows uninstall fix** (`clawmetry#6138`, `clawmetry#6149`, `clawmetry#6151`, merged Sep 2026): Per-file UI logging no longer stalls the Windows uninstaller on large runtime folders.

- **First-install screen fixes** (`clawmetry#6099`, `clawmetry#6101`, `clawmetry#6111`, `clawmetry#6113`): Dashboard no longer shows a blocking setup screen when there is already data to display.

**Carried from prior weeks (see 2026-09-18 synthesis for full list):**

- Enterprise readiness batches 1–5, hosted Guard/Signals parity, cost basis labels everywhere, cloud project cost report + finance reader, privacy/security hardening, auth fix, DPA first draft.

---

## Quiet noise (likely not signal)

- **WO-MON OTLP schema completeness series** (`clawmetry#6071`–`#6077`, filed Sep 17): Seven work-order tracking issues for OTLP schema completeness. Real features, but self-generated internal scope. The two *bugs* in this cluster (#5938, #5949) are signal; the enhancement trackers are backlog.

- **Bot-plan-only tracking issues** (~18+ of 33 enhancement issues carry `bot-plan-only`): Claude-generated architectural plans waiting for a PR. Real features, not validated external user asks. Implementation backlog.

- **CI hardening PRs** (~15 merged PRs this week): Hash-pinned pip bootstraps, supply-chain hardening, bandit triages. Healthy hygiene; not user feature signal.

- **Version-bump + RELEASE + i18n + deps PRs**: ~50–60% of merged PRs. Automation working correctly.

---

## Velocity check

| Metric | Value |
|--------|-------|
| OSS PRs merged (this week, excl. bumps/RELEASE/i18n/deps) | ~12 substantive |
| Cloud PRs merged (this week) | *not accessible this run* |
| User-signal themes shipped (this week) | **4** (Qwen Code free, Agents default, OpenClaw approvals, Guard correctness) |
| **Largest PR cluster (this week)** | CI hardening (~6 PRs) |
| **OTLP P0 bug `clawmetry#5938`** | **2nd week open, 0 PRs** ⚠️ |
| **OTLP P1 bug `clawmetry#5949`** | **2nd week open, 0 PRs** ⚠️ |
| Session Replay EPIC: PRs shipped | **0 (6 weeks open)** |
| Cost enforcement alerts/digest: PRs shipped | **0 (15+ weeks)** |
| P0 Security `clawmetry-cloud#315`: PRs shipped | **0 (23+ weeks, status unverifiable)** |
| Evals EPIC (`clawmetry#1619`): PRs shipped | **0 (18+ weeks)** |
| Dives EPIC (`clawmetry#999`): PRs shipped | **0 (19+ weeks)** |
| React v2 EPIC (`clawmetry#1492`): PRs shipped | **0 (18+ weeks)** |
| Themes HOT for 2+ weeks without action | OTLP P0/P1 bugs (entering week 2), Session Replay (6 wks), cost enforcement alerts (15+ wks) |
| Cloud repo accessible this run | **No** (OSS scope only) |

**Uncomfortable truths this week:**

1. **OTLP P0/P1 are entering their second week without a PR.** The same Guard fix track that landed `clawmetry#6161` this week has the context to close `clawmetry#5938`. A partial fix shipped in week 1; the canonical test has not. At week 2, this is a scheduling decision, not an engineering ambiguity.

2. **Dashboard opens on Agents, but Agents leads to a broken transcript viewer.** Shipping the Agents-first default (#6105) improved the product's entry experience. But the first thing a user does after landing on their agents is click through to a transcript — and for any multi-agent Claude Code session, that transcript still collapses subagent trees to a single chip. The new entry point raises the stakes for the Session Replay fix.

3. **Three epics are now 18–19 weeks old with zero PRs.** React v2 (#1492), Evals (#1619), and Dives (#999). Each has a defined first step and no design ambiguity. Open issues at this age without movement are either implicitly deprioritized (in which case close them) or stuck on something specific (in which case write that in the issue). Silent staleness helps no one.

4. **Cost enforcement alerts remain 15+ weeks unshipped.** Budget visibility is excellent now. The alert path is the gap. A dial with no alarm is not control.

5. **Cloud issues remain inaccessible for this run.** The plaintext API key bug, cost enforcement intel signals, and Guard cloud issues are carried from 2026-07-31 data. This is the second run in a row with partial cloud visibility.

---

## How this list is built

Reads every open `intel-feedback` / `intel-pain` / `bug` / `enhancement` issue across BOTH repos (`vivekchand/clawmetry` and `vivekchand/clawmetry-cloud`), clusters semantically, ranks by reaction count + recency. Cross-references the last 30 days of merged PRs in both repos to detect what's already addressed — in either repo.

This run: **35 open OSS issues analyzed** (3 `bug` + 32 `enhancement`; 0 `intel-feedback` / 0 `intel-pain` in OSS — all OSS issue signal is bot-generated or founder-initiated). **Cloud issues inaccessible this run** — carried from 2026-09-18. **~12 substantive merged OSS PRs** in the 7-day window. Cloud repo out of session GitHub scope this run.
