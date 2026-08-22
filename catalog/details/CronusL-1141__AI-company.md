# CronusL-1141/AI-company

Multi-agent team operating system for Claude Code. 108 MCP tools, 40+ agent templates, 10 lifecycle hooks, 7 pipeline workflows. Persistent teams, structured meetings, task wall, real-time React dashb

## tools

A project-isolated **knowledge base** that accumulates research findings over time. Each repo progresses through 4 stages (a progressive funnel, since v1.5.0), with token-efficient triggers and append-only history:

- **Stage 0 — Auto shallow-summary on archive**: newly-archived repos automatically get a 200-400 char `ai-engineer` summary (core function / positioning / advantages). 8-class failure handling with **self-learning hooks** (3+ same-class fails surface through `self_learning_pending`; the queue exposes recorder/searcher injection points you can wire to your own lesson store)
- **Stage 1 — On-demand architecture analysis**: user picks research direction ("memory_system") → batch-dispatch `backend-architect` agents to read architecture key files
- **Stage 2 — Multi-perspective debate**: triggers existing `debate_start` (NOT a built-in debate engine — **reuses meeting system**)
- **Stage 3 — Reference / Integrate marking**: `mark_as_reference` adds tag for future quick recall; `start_integration` triggers existing `task_create` for actual implementation
- **Active vs Full dual-view**: data is **append-only forever**. Stars-falling repos kept (just `is_active=False`); stars climbing back auto-promotes + re-queues Stage 0
- **Dashboard `/ecosystem`**: list with stage badges + research timeline + project filter dropdown + candidate-filter page (`/ecosystem/research`) + per-project settings tab — the single largest tool family in the OS

## features

- **Failure Alchemy**: `failure_analysis` still runs as part of the loop subsystem — every failed task extracts root cause and produces *Antibody* (stored in team memory to prevent repeats) / *Vaccine* (high-frequency failures become pre-task warnings) / *Catalyst* (analysis injected into future Agent system prompts). No longer the headline, but defensive rules keep accruing.
- **AWARE loop memory · `find_skill` 3-layer discovery (skills + integration recipes) · Prompt Registry**: see the full tool table below. The scheduler and the loop state machine were retired in favour of CC-native `Cron*` and on-demand tools (CC-is-not-always-on principle); the `wake_agent` schedule kind survives for the fleet wake subsystem.

---

## installation

Tell Claude Code:
> "Read https://github.com/CronusL-1141/AI-company/blob/master/INSTALL.md and follow the instructions to install AI Team OS"

Claude Code will read the install guide and walk you through the setup automatically.

---

> **Important**: Install AI Team OS to your system Python, not inside a project virtual environment.
> If installed in a venv, AI Team OS will only work in that specific project.
> Run `deactivate` first if a venv is currently active, then install.

---

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
