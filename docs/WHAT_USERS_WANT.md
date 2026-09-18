# What Users Want — September 2026 Edition

*Auto-generated weekly by the roadmap synthesis bot. Last updated: 2026-09-18 09:00 UTC. Aggregates signal across both `vivekchand/clawmetry` (OSS) and `vivekchand/clawmetry-cloud` (cloud).*

> **Cloud data note:** Cloud repo accessible this run — first time since the 2026-07-31 synthesis (17-week gap). Open issues were not retrievable (GitHub session scope partial — issues returned access denied, PRs succeeded). 50+ merged cloud PRs from the last 30 days are included. Cloud open issues are still carried from 2026-07-31 where they cannot be verified closed.

---

## TL;DR (this week)

The last three weeks delivered the largest feature batch in recent memory: enterprise readiness batches 1–5 shipped LiteLLM, fleet install, project attribution and budgets, price book, framework IDs, signed self-hosted image, hosted Guard + Cost Optimizer parity, and prompt injection detection. That's a clean, coherent enterprise push and it is real. The uncomfortable part: every one of the user-filed long-running epics — Session Replay (5 weeks, 0 PRs), Evals (17 weeks), Dives (18 weeks) — entered this week exactly where they entered last week. More urgently, **two correctness bugs in OTLP telemetry are now open at P0 and P1**: spans bypass Guard entirely and durability receipts are broken. Enterprise customers integrating LiteLLM and LangGraph over OTel are shipping into a broken observation layer.

---

## Hot themes (build these next)

### 1. OTLP Telemetry Correctness — Spans Bypass Guard and Durability Broken

- **Demand**: 2 open `bug` issues (P0 + P1), 7 open `enhancement` issues on schema completeness; 18 comments across the bugs. All filed 2026-09-13–17.
- **Representative quotes**:
  - *"Guard reads `store.query_events`, but spans go to a separate spans table via `put_span`. No detector ever sees them. [...] Redaction runs only in `LocalStore.ingest`. Span input/output/attributes are stored as received."* — `clawmetry#5938` (P0, 13 comments)
  - *"Never return an unqualified success after silently losing accepted records; follow OTLP partial-success/retry semantics and document rejected counts."* — `clawmetry#5949` (P1, 5 comments)
  - *"Extend existing spans storage to composite identity, resource/scope/schema provenance, links, events, status, timestamps and content policy; migrate existing rows safely."* — `clawmetry#6071` (schema completeness, 1 comment)
- **Why it matters**: The enterprise readiness push just shipped LiteLLM (#5965) and CI/CD provenance (#5974). Every enterprise customer integrating via OTel — LangGraph, Azure AI Foundry, AWS AgentCore — is sending telemetry into a layer that (a) never routes their span tool calls to Guard and (b) stores prompt text unredacted. Partial fixes shipped (#5953, #5963, #6009) but the P0 bug (#5938) remains open: a harmless-command canary test through the normalized span path has not landed. The durability bug (#5949) means a restart after accepting valid items loses those items. These are correctness failures, not quality-of-life gaps.
- **Linked issues**: `clawmetry#5938` (P0), `clawmetry#5949` (P1), `clawmetry#6071`, `clawmetry#6072`, `clawmetry#6073`, `clawmetry#6074`, `clawmetry#6075`, `clawmetry#6077`
- **Likely scope**: OSS — `clawmetry/sync.py`, `clawmetry/local_store.py`, Guard detector path
- **Suggested first step**: Close `clawmetry#5938` first: normalize tool-call spans into the existing event contract so Guard evaluates them, and run redaction before storage. The test requirement is a canary that does not execute a destructive command — this is a one-PR scope.
- **Weeks open**: **1** (P0, but severity = now, not backlog)

---

### 2. Session Replay — Runtime-Aware Transcript Viewer

- **Demand**: 3 open OSS issues (`clawmetry#4814`, `#4815`, `#4816`), first filed 2026-08-14. No external user reactions (early signal, but architecture-level: the current viewer is demonstrably broken for multi-agent sessions).
- **Representative quotes**:
  - *"Claude Code is the highest-fanout runtime we support — sessions with 20+ Agent/Task calls. Today the transcript viewer shows the parent turn with a single collapsed 'Task' tool chip — the child's actual work is never inlined."* — `clawmetry#4815`
  - *"Today the session UI shows nothing about how a session ran: Auto vs interactive vs plan vs `--dangerously-skip-permissions`. Approvals asked count is stored but the transcript viewer never fetches it."* — `clawmetry#4814`
  - *"OpenClaw has the richest on-disk trace of any runtime we support — a purpose-built `acp_replay_events` stream, plus normalized tables. We ignore all of it and render the flat JSONL."* — `clawmetry#4816`
- **Why it matters**: ClawMetry's core claim is "observe what your agent actually did." The transcript viewer is where that claim is either demonstrated or disproved. For any Claude Code session with subagents, it disproves it: sub-agent trees collapse to a single chip, permission mode is invisible, workflow fanouts vanish. OpenClaw's replay stream — the richest trace of any supported runtime — is unused. The OTLP tracing tab and Guard tab both landed this period with live data; the transcript viewer remains in 2023 architecture.
- **Linked issues**: `clawmetry#4814`, `clawmetry#4815`, `clawmetry#4816`
- **Likely scope**: OSS — `routes/sessions.py`, `clawmetry/local_store.py`, `replay_events` table
- **Suggested first step**: The canonical schema and `replay_events` table design (from `clawmetry#4813`'s architectural write-up, which predates all three) is the dependency. Ship it first, then the runtime-specific mappers (#4814–#4816) can stack on it. This is a sequencing issue, not a design gap.
- **Weeks open without a PR**: **5**

---

### 3. Cost Enforcement — Budget Alerts and Spend Digest (Still Partially Open)

- **Demand**: 9+ open issues across both repos (3 OSS proxy issues + 6+ cloud intel issues from 2026-07-31). *[Cloud intel signals carried — unverified against current open issues.]*
- **Representative quotes** *(carried; cloud issues inaccessible)*:
  - *"Just a number climbing in silence while five engineers stared at dashboards that gave us totals and nothing else."* — `clawmetry-cloud#1683`
  - *"I use LLMs daily… I just can't figure how to burn that much money a month responsibly."* — `clawmetry-cloud#653` (HN 474-comment thread)
  - *"By step nine you have a context window the size of a small novel and a per-call cost that has tripled because cache writes accumulated."* — `clawmetry-cloud#655` ($47K retroactive bill)
- **Why it matters**: Significant progress shipped this period: per-project attribution and budgets (#5968 OSS), project cost report + finance reader + CSV export (#2452, #2440 cloud), cost basis labels everywhere (#5975, #6000), contract-rate price book (#6008). These cover the "visibility" half. The "enforcement" half — graduated budget alerts (50%/80%/95%), weekly spend digest to Slack/email, hard caps before the limit — is still unshipped. Visibility without alerts is a dial with no alarm.
- **Linked issues**: `clawmetry-cloud#1683` *[carried]*, `clawmetry-cloud#653` *[carried]*, `clawmetry-cloud#655` *[carried]*, `clawmetry#2816`, `clawmetry#2817`, `clawmetry#2818`
- **Likely scope**: Both — OSS proxy gets enforcement rules; cloud gets alert delivery + digest
- **Suggested first step**: Graduated budget alerts at 50%/80%/95% of the per-project budget already stored in `clawmetry#5968`. The budget row exists; the alert evaluation path does not.
- **Weeks unaddressed (alert/digest half)**: **14+**

---

### 4. P0 Security — Plaintext API Keys in Production DB ⚠️ *[carried, 22+ weeks]*

- **Demand**: 1 issue (`clawmetry-cloud#315`, labeled `bug`, filed **2026-04-14**). Cannot be verified closed — cloud issues inaccessible. Cloud security PRs shipped (#2447 admin hardening, #2443 constant-time fleet key compare) but none explicitly address bcrypt-stored user keys.
- **What it says**: `users.api_key` stores raw `cm_*` tokens in cleartext in the production database. Anyone with database read access — backup access, GCP logs, support tooling, a developer credential — can impersonate any user.
- **Why it matters**: This has been open through 22 weeks of paying customer growth. The estimated fix is 1 day (bcrypt stored keys, one-time migration script). Two security PRs landed this period that did not address this. Carrying forward until cloud issues are readable and this can be confirmed closed.
- **Linked issues**: `clawmetry-cloud#315` *[carried — status unverifiable]*
- **Likely scope**: Cloud only
- **Suggested first step**: Bcrypt stored keys with a one-time migration.
- **Weeks open (if still open)**: **22+**

---

## Warm themes (worth tracking)

- **Agent Kill-Switch / Guard Control** (`clawmetry-cloud#4`, `clawmetry#2816–#2818`): **Substantially shipped this period.** Cloud Guard now lists running sessions and controls them (#2444 cloud). OSS Guard tab is simplified and check visibility improved (#6043). What remains open: `proxy.py` enforcement at port 4100 — a rule you can define but the proxy doesn't enforce is a database row, not a kill-switch. `clawmetry-cloud#4` (~196 days) is the oldest HOT issue across both repos; if the cloud Guard control landing satisfied it, close it.

- **Evals — LLM-as-judge** (`clawmetry#1619`): **17+ weeks open, 0 PRs.** Score-first reordering and session drill-down shipped in August. The original ask — auto-scoring with configurable rubric, local, on every completed session — remains unbuilt. The UI shell exists; the evaluator doesn't. If this isn't building soon, close the issue.

- **ClawMetry Dives — AI SQL→Chart** (`clawmetry#999`): **18+ weeks open, 0 PRs.** NL question → SQL → chart over local DuckDB. No new movement. DuckDB is more established than ever; the backend endpoint is the missing piece.

- **Outcome Provenance / Delayed Feedback** (`clawmetry#6077`): **New this week (Sep 17).** Extend `git_outcomes` and cohort infrastructure with explicit app outcome/feedback records, attribution confidence, revision, delay and missingness. Filed as part of the WO-MON series. Enterprise-relevant; depends on the OTLP schema completeness work also filed Sep 17.

- **Off-box Ingest SDK** (`clawmetry#4779`, `clawmetry#5679`): **Partial ship.** Ingest key + generated contract + setup prompt + live status all landed (#5684). The full SDK and auto-detection remain open. The front door is open; the SDK isn't.

- **Windows bootstrap** (`clawmetry#5794`, field-failure `clawmetry#5932`): `daemon_ingest_stalled` on Windows/Python 3.13 filed Sep 13 (1 distinct install). Also the conformance heartbeat failure filed Sep 17 (#6068) is a P0: `pip install clawmetry` + import may be broken for a class of users **right now** on the published artifact.

---

## Closed-loop themes (we shipped this)

**New since 2026-09-11 (this week's substantive merges):**

- **Populated dashboard UX fix** (`clawmetry#6069`, `clawmetry#6076`, merged Sep 17–18): Populated dashboards were blocked by a malformed setup status check. Users with data were seeing a first-install wait screen. Fixed.

- **Enterprise readiness batch 5** (`clawmetry#6053`, merged Sep 15): Agent supply-chain inventory (what MCP servers, skills, plugins, and instruction files an agent loads, with Guard flagging new/changed items) and hosted parity for trace incidents.

- **Hosted Guard and Signals list real sessions** (`clawmetry#5994`, `clawmetry-cloud#2444`, merged Sep 2026): Cloud Guard tab now lists running sessions and supports Pause/Stop/Kill. Signals drill-down lists sessions, not phrases.

**From the period starting 2026-08-18 (since last synthesis):**

- **Enterprise readiness batches 1–4**: LiteLLM gateway (`clawmetry#5965`), fleet install for VDI/virtual desktops (`clawmetry#5950`), per-project attribution + budgets (`clawmetry#5968`), price book with contract rates (`clawmetry#6008`/`clawmetry#5959`), OWASP/MITRE ATLAS framework IDs (`clawmetry#5952`), prompt injection detector (`clawmetry#5962`), self-hosted signed image (`clawmetry#5970`), CI/CD SARIF provenance (`clawmetry#5974`), ATLAS case-study scorecard (`clawmetry#5961`).

- **Hosted dashboard parity** (`clawmetry#6062`, `clawmetry#6057`, `clawmetry#6058`, `clawmetry-cloud#2450`, `clawmetry-cloud#2457`, `clawmetry-cloud#2458`): Hosted Guard tab stops asking for local inventory. Cost Optimizer shows evidence-backed data. First-install screen no longer traps cloud accounts. Runtime switcher followed on Overview and Cost Optimizer in both repos.

- **Cost basis everywhere** (`clawmetry#6000`, `clawmetry#5975`): Cost basis labels on Usage cards, Overview hero chip, and Sessions transcript chips. Subscription vs metered spend distinguished.

- **Cloud project cost report + finance reader** (`clawmetry-cloud#2452`, `clawmetry-cloud#2440`): Organization project cost report with authorised attribution, reconciled totals, and CSV export. A finance reader role can see costs without seeing member emails.

- **Privacy/security hardening (cloud)** (`clawmetry-cloud#2449`, `clawmetry-cloud#2447`, `clawmetry-cloud#2443`, `clawmetry-cloud#2448`): Stop BCC'ing customer emails to internal mailboxes; account purge + cancel-after-30-days; admin access log scrub + constant-time secret compares; fleet key constant-time compare.

- **DPA first draft** (`clawmetry-cloud#2445`): Counsel brief and incident runbook filed; blockers tracked.

- **Auth fix** (`clawmetry#6019`): Return 200 instead of 404 when no gateway token configured — was silently breaking new installs.

---

## Quiet noise (likely not signal)

- **WO-MON OTLP schema completeness series** (`clawmetry#6071`–`#6077`, filed Sep 17): Seven work-order tracking issues for OTLP schema completeness. Real features, but they are self-generated product scope from an internal planning session, not external user demand. The two bugs in this cluster (#5938, #5949) *are* signal; the WO-MON enhancement trackers are backlog.

- **Bot-plan-only tracking issues** (~18 of 30 enhancement issues carry `bot-plan-only`): Claude-generated architectural plans waiting for a PR. Real features, not validated user asks. Treat as implementation backlog.

- **CI hardening PRs** (~15–20 merged PRs): Hash-pinned pip bootstraps, bandit triages, workflow_run trigger declarations. Healthy supply-chain hygiene; not user feature signal.

- **Version-bump + RELEASE + i18n + deps PRs**: ~50–60% of merged PRs in both repos. Automation working correctly.

- **Field-failure telemetry issues** (auto-filed): `clawmetry#5932` (Windows/py3.13 stall) and `clawmetry#6068` (conformance heartbeat failure) are real bugs auto-filed by CI. #6068 is actionable now (published product verification failing).

---

## Velocity check

| Metric | Value |
|--------|-------|
| OSS PRs merged (last 30d, excl. bumps/RELEASE/i18n/deps) | ~90–110 substantive |
| Cloud PRs merged (last 30d, excl. bumps) | ~35–40 substantive |
| User-signal themes shipped (last 30d) | **5–6** (cost enforcement visibility, hosted Guard/Control, hosted parity, project cost report, privacy hardening, first-install UX) |
| **Largest PR cluster (last 30d)** | Enterprise readiness batches (~35 PRs) — driven by enterprise sales pipeline, not OSS issue signal |
| **2nd largest cluster** | Hosted dashboard parity (~12 PRs) — driven by cloud customer pain |
| Session Replay EPIC: PRs shipped | **0 (5 weeks open)** |
| Cost enforcement alerts/digest: PRs shipped | **0 (14+ weeks — visibility shipped, enforcement not)** |
| P0 Security `clawmetry-cloud#315`: PRs shipped | **0 (22+ weeks, status unverifiable)** |
| Evals EPIC (`clawmetry#1619`): PRs shipped | **0 (17+ weeks)** |
| Dives EPIC (`clawmetry#999`): PRs shipped | **0 (18+ weeks)** |
| React v2 EPIC (`clawmetry#1492`): PRs shipped | **0 (17+ weeks)** |
| Themes HOT for 2+ weeks without action | Session Replay (5 wks), cost enforcement alerts (14+ wks) |
| OTLP P0/P1 bugs open | **2 (#5938, #5949) — both < 1 week** |
| Conformance heartbeat failure | **1 (#6068, filed Sep 17 — published product possibly broken now)** |
| Cloud repo accessible this run | **Yes (first time since 2026-07-31 synthesis)** |

**Uncomfortable truths this week:**

1. **The conformance heartbeat is failing against the published artifact right now.** `clawmetry#6068` (filed Sep 17) means `pip install clawmetry` + import may be broken for a class of users on the currently-published wheel. This is not a backlog item. Triage order: is pip install + import broken? If yes, yank or hotfix first.

2. **OTLP telemetry has two correctness bugs open at P0 and P1.** The enterprise push just shipped LiteLLM and CI/CD provenance. Enterprise OTel users integrating today are sending span tool calls that Guard never sees and that are stored unredacted. Partial fixes landed (#5953, #5963, #6009) but the canonical test (canary command through the normalized span path) has not been written, which is how we know the path isn't confirmed closed.

3. **Session Replay is now 5 weeks open with zero PRs.** The transcript viewer is ClawMetry's moment of truth for multi-agent sessions. For Claude Code with subagents, that moment currently fails. The four-issue EPIC has a defined starting point and no design ambiguity. The only missing thing is a PR.

4. **The enterprise push is coherent but not user-signal-driven.** Five batches of enterprise readiness features in three weeks is a real achievement. But the source is a sales pipeline, not OSS/cloud issue signal. The ratio of user-signal→shipped sits at roughly 3 of ~12 distinct feature themes in the last 30 days.

5. **Three epics have been open 17–18 weeks with zero PRs.** React v2 (#1492), Evals (#1619), and Dives (#999). Each has a defined architecture and a clear first step. At this age, a decision — first PR or explicit close — is more honest than continued open status.

6. **Cost enforcement alerts are 14+ weeks unshipped.** The visibility half (budgets, project costs, price book) shipped this period and is substantial. The alert/enforcement half (graduated alerts, weekly digest, hard caps) remains untouched. A budget row with no alert path is an accounting record, not a control.

---

## How this list is built

Reads every open `intel-feedback` / `intel-pain` / `bug` / `enhancement` issue across BOTH repos (`vivekchand/clawmetry` and `vivekchand/clawmetry-cloud`), clusters semantically, ranks by reaction count + recency. Cross-references the last 30 days of merged PRs in both repos to detect what's already addressed — in either repo.

This run: **34 open OSS issues analyzed** (4 `bug` + 30 `enhancement`; 0 `intel-feedback` / 0 `intel-pain` in OSS — all OSS issue signal is bot-generated or founder-initiated). **50+ cloud PRs** from the last 30 days analyzed (cloud issues inaccessible — `bug`/`intel` signals carried from 2026-07-31). **~90–110 substantive merged OSS PRs** in the 30-day window. Cloud repo accessible for PR data this run for the first time since 2026-07-31.
