# ww-w-ai/bkit-claude-code

bkit Vibecoding Kit - PDCA methodology + Claude Code mastery for AI-native development

## tools

| Command | When to use | What it spawns | Output |
|---|---|---|---|
| **`/sprint`** | Multi-feature release (quarter, milestone, multiple linked features) | `sprint-master-planner`, `sprint-orchestrator`, `sprint-qa-flow`, `sprint-report-writer` | Master plan + 8-phase per sprint + cumulative report |
| **`/pdca`** | A single feature (or runs inside a sprint per feature) | `pm-lead`, `cto-lead`, `gap-detector`, `pdca-iterator`, `qa-lead`, `report-generator` (any of 34 agents) | PRD + plan + design + code + analysis + report |
| **`/control`** | Anytime — set autonomy | — | Updates Trust Level scope; affects both `/sprint` and `/pdca` |

## How bkit closes the AI-coding gap — Context Engineering

bkit is more than commands. It is a **Context Engineering system** that solves the root cause of AI-coding failures: the AI doesn't have the right context.

| The AI coding problem | bkit's Context Engineering answer |
|---|---|
| AI hallucinates because it doesn't know your conventions | 44 skills (PDCA, Sprint, PM frameworks, …) auto-injected based on intent |
| AI loses focus as the session grows | Memory + Task Management resumes across sessions; Sprints are context-budgeted |
| AI ships code that drifts from the spec | 11 Quality Gates + `gap-detector` measurement + `pdca-iterator` auto-repair |
| You only catch bugs at PR review | Phase-by-phase gating: drift is caught at every transition, not at the end |
| You need to remember the right command | 8-language auto-trigger + intent-router; type *"login 만들어줘"* or *"build login"* and bkit picks the path |
| AI sessions are ephemeral; no audit trail | Audit log + Token Ledger + `Docs = Code` philosophy: every decision is on disk |

## bkit's three philosophies (from [`bkit-system/philosophy/core-mission.md`](bkit-system/philosophy/core-mission.md))

| Principle | What it means for you |
|---|---|
| **Automation First** | You don't need to know PDCA, Sprint, or any command. Type what you want; bkit picks the right workflow. The state machine + workflow engine drive the rest. |
| **No Guessing** | If bkit isn't sure, it checks the docs. If still unsure, it asks you. It never makes up an answer. `gap-detector`, `design-validator`, and 11 quality gates enforce this. |
| **Docs = Code** | Every feature produces docs (PRD + plan + design + analysis + report). The docs are the contract; bkit verifies that the code matches. `scripts/docs-code-sync.js` enforces 0 drift in CI. |

## installation

```bash
# 1. Install (one time)
claude plugin install bkit

# 2. Enable parallel team execution (optional, recommended)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

## features

/pdca pm my-feature        # Describes what you want; bkit handles the rest

# 4. When you're ready for a multi-feature release
/sprint master-plan my-release --name "Q2 Launch" --features auth, billing, reports
# (You approve the plan)
/sprint start my-release-s1
```

Recommended Claude Code runtime: **v2.1.220** (bkit explicitly handles v2.1.218's `context: fork` background-by-default change and v2.1.219's nested-subagent depth-3 default; Claude 5 alias resolution — `sonnet` → Sonnet 5 needs ≥ v2.1.197). Model floor: **v2.1.170+** required by the 6 Fable-pinned agents (below it they fail to spawn; bkit shows a SessionStart advisory with a workaround). Install minimum **v2.1.143**; runtime minimum **v2.1.78**.

**On Claude Code v2.1.232 and later**, fork mode is on by default in interactive
sessions: a subagent's result arrives as a notification on a *later* turn, and the
Agent tool no longer accepts `run_in_background`. bkit's skills are unaffected.
Sprint gates that measure through a subagent will report **"not measured"** rather
than a score, and name the cause — a missing number, never a wrong one. Set
`CLAUDE_CODE_FORK_SUBAGENT=0` to get in-turn results back. bkit shows this once at
SessionStart and does not block. Verified against v2.1.232; Breaking changes 0
across v2.1.228–v2.1.232 (171 consecutive compatible releases).

## Quality gates — the safety net explained

A "quality gate" is a hard stop that won't let the workflow advance until a measurable condition is true. bkit ships 11 of them. The ones that matter most for new users:

| Gate | What it measures | If it fails |
|---|---|---|
| **M1 matchRate** | How much of your design actually appears in the code, 0–100 % | Below 90 % → `pdca-iterator` automatically rewrites the code (up to 5 cycles) |
| **M3 critical issues** | Security or correctness bugs flagged by `code-analyzer` | Any critical → workflow pauses, you decide |
| **S1 dataFlow integrity** | 7-layer check: UI → Client → API → Validation → DB → Response → Client → UI | Below 85 % → 7 hops re-verified one by one |
| **qa gate** | QA pass rate ≥ 95 %, zero critical findings, zero runtime errors — from what `qa-lead` actually measured | Below 95 % → back to `act` for fixes, then QA re-runs (v2.1.38: the return path and its retry ceiling both work) |

Full M1–M10 + S1 catalog in [README-FULL.md §5](README-FULL.md#5-quality-gates--self-repair).

## Architecture at a glance

44 skills · 34 agents · 21 hook events / 24 blocks across 28 handlers · 2 MCP servers (19 tools) · 200 lib modules across 22 subdirs · 63 scripts · 40 templates · 385 test files (5,355 test cases). Clean Architecture 4-Layer · Defense-in-Depth 4-Layer · Invocation Contract L1–L6, where L6 is host integration: a real `claude -p --plugin-dir` run whose recorded evidence CI checks against the shipped `hooks.json`.

Agents run on a 4-tier role-based model matrix: **fable** (long-horizon orchestration — leads), **opus** (deep reasoning, security & high-frequency PDCA verifiers), **sonnet** (implementers), **haiku** (monitors). The repeated Check/iterate verifiers (gap-detector, design-validator, pdca-iterator) run on Opus 4.8 — strong verification at half Fable's cost.

Full architecture deep-dive: [README-FULL.md §9](README-FULL.md#9-architecture).

## Documentation

| Path | What's there |
|---|---|
| [README-FULL.md](README-FULL.md) | Full command reference, deep workflow internals, agent teams, architecture, Skill Evals |
| [CHANGELOG.md](CHANGELOG.md) | Release history (single source of truth — latest release: v2.1.38) |
| [CUSTOMIZATION-GUIDE.md](CUSTOMIZATION-GUIDE.md) | Override any bkit component in your `.claude/` directory |
| [AI-NATIVE-DEVELOPMENT.md](AI-NATIVE-DEVELOPMENT.md) | The 6 AI-Native principles and how bkit implements them |
| [`bkit-system/philosophy/`](bkit-system/philosophy/) | Core mission, Context Engineering, PDCA methodology, AI-Native principles |
| [`docs/06-guide/sprint-management.guide.md`](docs/06-guide/sprin
