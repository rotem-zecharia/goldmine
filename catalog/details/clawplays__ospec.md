# clawplays/ospec

Spec-driven, agentic workflow framework for AI coding agents. Turn a request into a verifiable goal loop — plan, act, verify — with durable specs and evidence in your repo. Works with Claude Code, Cod

## features

AI coding assistants are powerful, but requirements that live only in chat history are hard to inspect, review, and close out cleanly. OSpec adds a lightweight workflow layer so the repository can hold the change context before code is written and after the work ships.

- **Spec-driven work, saved to your repo** — OSpec turns a request into files (proposal, design, plan, tasks, reviews, verification evidence) that live in your repo instead of in chat history, so any assistant (Codex/GPT, Claude Code, Gemini, OpenCode, or plain CLI) can pick up exactly where the last one stopped.
- **`ospec change` — the everyday fast flow** — one requirement becomes one active change on a short `init -> change -> verify/finalize` path, kept lightweight and easy to review.
- **`ospec goal` for larger or riskier work** — describe the result you need; the AI asks important questions, writes an inspectable plan, implements the work, runs tests, requests an independent review, updates project docs, and continues until the result is proven.
- **One predictable Goal workflow** — every Goal uses the same fast quality path, pauses for material user decisions, and saves progress in the repository so a later session can resume it.

## installation

```bash
npm install -g @clawplays/ospec-cli
```

Official package: `@clawplays/ospec-cli`  
Command: `ospec`  
Verify install: `ospec --help`

## Quick Start

OSpec only takes 3 steps:

1. initialize OSpec in your project directory
2. create and advance one change for a requirement, document update, or bug fix
3. archive the accepted change after deployment and validation are complete

### 1. Initialize OSpec In Your Project Directory

Recommended prompt:

```text
OSpec, initialize this project.
```

Claude / Codex skill mode:

```text
/ospec initialize this project.
```

<details>
<summary>Command line</summary>

```bash
ospec init .
ospec init . --summary "Internal admin portal for operations"
ospec init . --summary "Internal admin portal for operations" --tech-stack node,react,postgres
ospec init . --architecture "Single web app with API and shared auth" --document-language en-US
```

CLI notes:

- `--summary`: project overview text written into the generated docs
- `--tech-stack`: comma-separated stack list such as `node,react,postgres`
- `--architecture`: short architecture description
- `--document-language`: generated doc language, choose from `en-US`, `zh-CN`, `ja-JP`, or `ar`
- AI-first language resolution order: explicit language request in the conversation -> current conversation language -> persisted project language in `.skillrc`
- CLI language resolution order: explicit `--document-language` -> persisted project language in `.skillrc` -> existing project docs / managed `for-ai/*` guidance / asset manifest -> fallback `en-US`
- OSpec persists the chosen project document language in `.skillrc` and reuses it for `for-ai` guidance, `ospec change`, and `ospec update`
- new projects initialized by `ospec init` default to the nested layout: root `.skillrc` and `README.md`, with OSpec-managed files under `.ospec/`
- plain init does not create optional knowledge maps such as `.ospec/knowledge/src/` or `.ospec/knowledge/tests/`; those appear only when a project already has legacy knowledge content to migrate or when future explicit knowledge-generation flows create them
- CLI commands still accept shorthand like `changes/active/<change-name>`, but the physical path in nested projects is `.ospec/changes/active/<change-name>`
- if you pass these values, OSpec uses them directly when generating project docs
- if you do not pass them, OSpec reuses existing docs when possible and otherwise creates placeholder docs first

</details>

### 2. Create And Advance A Change

Use this for requirement delivery, documentation updates, refactors, and bug fixes.

Recommended prompt:

```text
OSpec, create and advance a change for this requirement.
```

Claude / Codex skill mode:

```text
/ospec-change create and advance a change for this requirement.
/ospec-goal create and advance a full goal for this requirement.
```

<details>
<summary>Command line</summary>

```bash
ospec change docs-homepage-refresh .
ospec change fix-login-timeout .
ospec change update-billing-copy .
```

</details>

### Agent Execution (Goal Workflow)

The classic change flow above stays simple: `proposal.md` → `tasks.md` → implement → `verification.md` → `review.md`, with no controller layer. The agent controller layer — parallel worker dispatch, reviewer gates, and durable evidence — belongs to the full goal workflow. Use it with `ospec goal`, or on a single change only when you explicitly opt into agent/worker execution. OSpec keeps the controller state in repo artifacts, and the current AI harness starts native worker agents when available.

```bash
ospec session .
ospec execute bootstrap changes/active/<goal-name>
ospec execute workspace changes/active/<goal-name>
ospec execute status changes/active/<goal-name>
ospec execute dispatch changes/active/<goal-name> --limit 3
ospec execute launch changes/active/<goal-name> --task <task-id> --target codex
ospec execute complete <task-id> changes/active/<goal-name> --status DONE --summary "..."
ospec loop tick changes/a
