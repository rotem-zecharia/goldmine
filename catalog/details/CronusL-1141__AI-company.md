# CronusL-1141/AI-company

Multi-agent team operating system for Claude Code. 108 MCP tools, 40+ agent templates, 10 lifecycle hooks, 7 pipeline workflows. Persistent teams, structured meetings, task wall, real-time React dashb

## features

### 1. Cross-Session Orchestration (new in v1.10.0)

A single CC session can now observe and drive its sibling sessions for one operational turn, instead of only being able to spawn brand-new ones:

- **Wake system v2**: the `/api/wake/actionable` single-source predicate feeds both the event watcher and the turn-end guard; SessionStart moves from a fixed 30-minute cron to dynamic `/loop` intervals; a Stop-hook turn-end guard always lets `decision:block` and user-stop keywords pass through; a session-scoped event watcher carries a 1-hour hard timeout. No resident daemons.
- **Fleet downlink primitive**: headless `claude -p --resume <session_id>` drives a target sibling session for one turn, reusing the existing wake machinery (semaphore, fuse, allowlist, per-session dedupe, full audit trail).
- **`agent_reuse_recommend` MCP tool**: a three-way reuse decision (reuse / slim-then-reuse / spawn-new) scored by domain match, reachability (live / resumable / cross-session / expired), and context watermark.
- **Context watermark ledger**: exact token usage read from the transcript tail (cheap-checks-first), surfaced as a three-color watermark bar on agent views and on the new fleet / worktree observability cards.
- **Compaction checkpoint** (v1.11.0): `PreCompact` freezes the OS-side operating picture — agents in flight, open tasks, decisions queued for you — and `SessionStart(source=compact)` hands it straight back. CC's own summary body is deliberately not stored: after compaction it is already in the model's context; what a compacted Leader loses is the OS-side state it no longer knows to ask about.
- **CC session registry as a second liveness track** (v1.11.0): `~/.claude/sessions/<pid>.json` carries a real pid and CC's own idle/busy state, which distinguishes "process gone" from "process alive but quiet" — a distinction transcript freshness cannot make. It runs alongside the existing verdict and only records where the two disagree; the verdict itself is unchanged until the divergence data says otherwise.
- **Background daemon sessions are visible** (v1.11.0): `GET /api/hooks/background-jobs` reads CC's own job state, so a `--bg` session that outlives its foreground window no longer looks like "nobody is working".

Usage guidance:
- A new session's SessionStart briefing already points you at running `/loop` once - follow it instead of guessing at intervals.
- Check the project detail page for the fleet card (per-session CEO / model / in-flight tasks / watermark) and the worktree card (branch ownership + unlanded-work status) before you act.
- Call `agent_reuse_recommend` before dispatching a follow-up agent - reusing a live or resumable sibling session beats spawning a fresh one.
- The S4 worktree teardown guard and per-template `isolation: worktree` defaults apply automatically; no configuration is needed.

### 2. Memory System v2 — two-layer memory, every Agent inherits at birth (new in v1.9.0)

The OS's signature differentiator: your team's preferences, corrections, and hard-won lessons flow automatically to every Agent it dispatches.

- **Direction layer** (user preferences / corrections / design intent, 4 kinds): resident injection via **both** the SessionStart and SubagentStart hooks — every sub-Agent inherits the team's values and red lines the moment it's born, so you don't repeat yourself. The size guardrail is a **single axis: storage cap = injection budget** (per-bucket character quotas, global 1200 + 1500 per project + user 300 = 3000 chars, <=400 chars per entry), so whatever fits is what actually ships; a full bucket hands back its complete contents and demands a cleanup before the retry. `supersedes` swap to prevent bloat, invalidate-never-delete for auditability. Writes are scanned for invisible Unicode, instruction-override phrasing, and credential shapes — the direction layer lands in every Agent's system prompt, which makes it an injection amplifier.
- **Episodic layer** (`task_memos` ledger): task-level executio

## tools

A project-isolated **knowledge base** that accumulates research findings over time. Each repo progresses through 4 stages (a progressive funnel, since v1.5.0), with token-efficient triggers and append-only history:

- **Stage 0 — Auto shallow-summary on archive**: newly-archived repos automatically get a 200-400 char `ai-engineer` summary (core function / positioning / advantages). 8-class failure handling with **self-learning hooks** (3+ same-class fails surface through `self_learning_pending`; the queue exposes recorder/searcher injection points you can wire to your own lesson store)
- **Stage 1 — On-demand architecture analysis**: user picks research direction ("memory_system") → batch-dispatch `backend-architect` agents to read architecture key files
- **Stage 2 — Multi-perspective debate**: triggers existing `debate_start` (NOT a built-in debate engine — **reuses meeting system**)
- **Stage 3 — Reference / Integrate marking**: `mark_as_reference` adds tag for future quick recall; `start_integration` triggers existing `task_create` for actual implementation
- **Active vs Full dual-view**: data is **append-only forever**. Stars-falling repos kept (just `is_active=False`); stars climbing back auto-promotes + re-queues Stage 0
- **Dashboard `/ecosystem`**: list with stage badges + research timeline + project filter dropdown + candidate-filter page (`/ecosystem/research`) + per-project settings tab — the single largest tool family in the OS

### 6. Knowledge Layer — Reference Graph + Unified Search (v1.8.0)

Everything the OS records — task memos, reports, tasks — becomes recallable knowledge:

- **Reference graph (P1a)**: a zero-LLM regex extractor mines OS-native ID references (wf_id / commit hash / task uuid / `[[memory]]`) out of memos and reports into an append-only `knowledge_links` table — the graph is a derived view, rebuildable from source text at any time
- **Unified search (P1b)**: `/api/search` fuses three arms via RRF — BM25 full-text (Chinese bigram native), knowledge-graph fanout (an ID query pulls in everything linked to it), and exact ID-prefix / title match
- **Global search box** in the Dashboard header, plus MCP tools `unified_search` / `link_query` / `link_trace` — recall past work by natural language ("how was the attribution fix done"), a `wf_` id, or a commit hash

> **Why zero-LLM?** The graph is a derived view: plain regexes extract the IDs, the whole graph can be rebuilt from source text at any time, and both extraction and retrieval cost zero tokens. Your recall pipeline never touches your model budget.

### 7. Task Wall · Meetings · 22-Page Dashboard

Governance ledger and panoramic visualization — everything leaves a trace:

- **Task wall**: a live board of pending / in-progress / done, event-driven + intelligent Agent matching + deadlock detection
- **8 structured meeting templates** (keyword auto-select, built on Six Thinking Hats / DACI / Design Sprint) — every meeting must produce an actionable conclusion; "we discussed but didn't decide" is not an outcome
- **22-page React 19 Dashboard**: Command Center / `/workflows` swimlane / decision timeline / meeting room / Ecosystem suite / Model Governance Settings

### 8. Autonomous Operation

The CEO never idles. It continuously advances work based on task wall priorities:

- Checks the task wall for the next highest-priority item when a task completes
- When blocked on something requiring your approval, parks that thread and switches to parallel workstreams
- Batches all strategic questions and reports them when you return — no interruptions for tactical decisions
- Deadlock detection: if the loop stalls, it surfaces the blocker rather than spinning

And it doesn't just execute — it evolves:

- **R&D cycle**: research agents scan competitors, new frameworks, and community tools; findings go to brainstorming meetings where agents challenge each other; conclusions become implementation plans on the task wall

### 9. File Truth as Source of Truth

Mos

## installation

Tell Claude Code:
> "Read https://github.com/CronusL-1141/AI-company/blob/master/INSTALL.md and follow the instructions to install AI Team OS"

Claude Code will read the install guide and walk you through the setup automatically.

---

> **Important**: Install AI Team OS to your system Python, not inside a project virtual environment.
> If installed in a venv, AI Team OS will only work in that specific project.
> Run `deactivate` first if a venv is currently active, then install.

---

## Quick Start

## requirements

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (`pip install uv`)
- Claude Code (MCP support required)
- Node.js >= 20 (Dashboard frontend, optional)

## configuration

By default the MCP server registers all **113 tools**. Two startup environment variables let you trim the surface for leaner sessions or non-CC clients with tool-count limits (e.g. Cursor only forwards the first 40 tools). Both are read once at server startup - no runtime state, no restart-on-change.

**`AITEAM_TOOLSETS`** - pick which capability-domain groups register:

- unset or `all` - full 113 (backward compatible)
- `default` - core groups only (`task,team,memory,infra,reports` = 29 tools, hard-capped at <=50)
- a comma list of group names, mixable with `default` for incremental loading, e.g. `AITEAM_TOOLSETS=default,ecosystem`
- unknown names are warned on stderr and ignored (a config typo never blocks server start)

**`AITEAM_READONLY=1`** - orthogonal overlay that strips every write tool (create/update/delete/apply/send/... plus `os_restart_api`) after registration, keeping only read tools. Handy for audit/observer sessions.

The 16 groups (default groups marked *):

| Group | Tools | Group | Tools | Group | Tools |
|---|---|---|---|---|---|
| task * | 8 | project | 6 | links | 3 |
| team * | 5 | agent | 7 | channels | 3 |
| memory * | 6 | meeting | 10 | task_analysis | 2 |
| infra * | 7 | briefing | 4 | watchdog | 1 |
| reports * | 3 | analytics | 2 | workflows | 3 |
| ecosystem | 42 | | | | |

```bash
# Example: lean core + ecosystem, read-only
AITEAM_TOOLSETS=default,ecosystem AITEAM_READONLY=1 <launch CC / MCP server>
```

## limitations

### Completed

- [x] Core Task Wall + Watchdog + Review (the loop state machine was retired in v1.10.x; scoring and the wall live on in `loop/task_wall_engine.py`)
- [x] Failure Alchemy (Antibody + Vaccine + Catalyst)
- [x] Decision Cockpit (Event stream + Timeline + Intent inspection)
- [x] Event-driven Task Wall 2.0 (Real-time push + Intelligent matching)
- [x] Living Team Memory (Knowledge query + Experience sharing)
- [x] What-If Analyzer (Multi-option comparison)
- [x] 8 structured meeting templates with keyword auto-select
- [x] 25 professional Agent templates (23 base + 2 debate roles) with recommendation engine
- [x] 4-layer defense rule system (48+ rules) + behavioral enforcement
- [x] Dashboard Command Center (React 19) — 23 pages including the `/workflows` swimlane, Workflow detail, the Ecosystem suite, `/usage` token attribution, and Settings with model governance
- [x] 113 MCP tools across 16 modules
- [x] CC Workflow observability layer (auto-tracking + /workflows dashboard + workflow_list / workflow_get / workflow_reconcile)
- [x] Knowledge layer — zero-LLM reference graph + unified 3-arm RRF search (v1.8.0)
- [x] Model governance — transcript-based model discovery + global default startup model (v1.8.1)
- [x] Machine-checked red-line invariants + one-command preflight (`scripts/preflight.sh`)
- [x] AWARE loop memory system
- [x] find_skill 3-layer progressive discovery
- [x] task_update API for programmatic task management
- [x] Workflow pipeline orchestration (7 templates + auto phase progression) — fully removed in v1.10.x, superseded by CC Workflow observability (`pipeline_stage_history` stays readable)
- [x] 2,307 automated tests, CI green
- [x] Prompt Registry (version tracking retired in v1.10.3 — nothing ever called `/track`, so every version column rendered "-"; effectiveness metrics live on, sourced from real agent activity)
- [x] BM25 as the main memory-retrieval chain (pure-Python Okapi BM25, Chinese bigram, recency-window recall + rerank)
- [x] Event log enhancement (entity_id / entity_type / state_snapshot fields)
- [x] CC Plugin Marketplace submission
- [x] File lock / workspace isolation (acquire/release/check/list + TTL=300s) — retired in v1.10.3; the lock file was empty in every real run, and hook-side edit-conflict warnings replaced it
- [x] Channel communication system (team:/project:/global + @mention)
- [x] Execution pattern memory (success/failure recording + BM25 retrieval) — retired in v1.10.3; the store never held a row, so the injected section was permanently blank
- [x] Guardrails L1 (7 dangerous patterns + PII warnings)
- [x] Alembic database migration system
- [x] Debate mode (4-round structured debate + code review)
- [x] Agent trust scoring system (auto-adjust on task success/failure) — scoring chain retired in v1.10.3 (no caller ever existed); the `trust_score` column stays and `auto_assign` still weights it
- [x] Tool tier draft (informational CORE/ADVANCED grouping — groundwork for context budgeting)
- [x] Agent Watchdog patrol (BUSY-timeout / stuck-task detection; the file-based heartbeat was retired in v1.10.x — CC subagents are one-shot and never polled)
- [x] SRE error budget model (GREEN/YELLOW/ORANGE/RED 4-level response) — retired in v1.10.3; its data directory sat empty for its entire lifetime
- [x] Completion verification protocol (anti-hallucination completion check)
- [x] Ecosystem integration recipes (GitHub/Slack/Linear/Full-stack presets, served by `find_skill`)
- [x] Session bootstrap rule compression (23 → 5 core rules, 60% context reduction)
- [x] Atomic API startup lock (multi-session port conflict prevention)
- [x] Auto port discovery (API finds available port, writes to `api_port.txt`)
- [x] MCP HTTP Streamable endpoint (`/mcp/` on FastAPI)
- [x] PyPI release - stopped at 1.3.4 (2026-04) and deprecated; the wheel ships without `plugin/` and config resources, so install via plugin or source instead
- [x] INSTALL.md CC-assisted installation guide

### In Progr
