# Arch1eSUN/Arcgentic

Mechanical plan/dev/self-audit/external-audit gates for AI coding agents, with a configurable role-routing topology engine, an MCP-UI live status panel, and native-tooling Claude Code V2 dispatch. Cla

## installation

### Codex local install

```bash
git clone https://github.com/Arch1eSUN/Arcgentic.git arcgentic
cd arcgentic
bash scripts/install-codex-local.sh --plugin-root .
```

Then start in a saved project workspace and ask:

```text
Use Arcgentic to build this idea: <your idea>
```

### npm bundle install

Use this if you want the Arcgentic plugin assets through npm:

```bash
npm install -g arcgentic
arcgentic install-codex-local
```

The npm package is a zero-dependency plugin bundle and Codex local install
helper. It includes the skills, agents, scripts, schemas, templates, and
platform manifests. The Python CLI is still published separately on PyPI.

### Claude Code install

```text
/plugin marketplace add Arch1eSUN/Arcgentic
/plugin install arcgentic@arc-studio
```

Then start inside your project:

```text
Use Arcgentic to build this idea: <your idea>
```

For Claude Code V2 experimental workflow setup:

If your Claude Code session's own tool list already includes `Agent`,
`SendMessage`, and `ListAgents` (native tooling / "tier 0"), no setup step
is needed — the session broker uses those tools directly and this is the
preferred, dogfood-verified path (see "Platform status" above). Only run
`install-hooks` below as a fallback, for sessions that lack those three
tools:

```bash
arcgentic claude-code-broker install-hooks \
  --settings .claude/settings.local.json \
  --state .agentic-rounds/state.yaml
```

### CLI install

Use this if you only need the command-line helper:

```bash
pipx install arcgentic
arcgentic --help
```

## Minimal example

Without Arcgentic:

```text
User: Build a small expense splitter.
AI: writes code
AI: says it is done
User: later discovers missing edge cases, unclear scope, no audit trail
```

With Arcgentic:

```text
User idea
-> current conversation becomes Orchestrator
-> Orchestrator creates or reuses Planner and sends the planning prompt
-> Planner returns the plan to Orchestrator
-> Orchestrator creates or reuses Developer and sends the dev prompt
-> Developer implements and returns a self-audit
-> Orchestrator dispatches optional Test only if realistic use needs it
-> Orchestrator creates or reuses Auditor and sends the audit prompt
-> Auditor returns PASS / NEEDS_FIX / AUDIT_INCOMPLETE
-> Orchestrator routes the next step
```

The important difference is not that the AI writes more text. The important
difference is that each role has a job, each stage has a stop condition, and
"done" is not accepted until the workflow can explain why.

## Arcgentic recommends a mode first

When you start Arcgentic with a new idea, the current session becomes
`Orchestrator`. Before it plans or builds, it should judge whether the idea is a
small fast project or a larger project that needs stronger review. Then it
recommends one project-level mode and asks you to confirm or override it:

| Mode | Choose it when | Tradeoff |
|---|---|---|
| **Single session, multiple agents** | You want the fastest run and a smaller demo surface. | Faster completion, weaker audit isolation. Planner, Developer, Test, and Auditor run inside the current Orchestrator session as fixed named role agents and are reused across rounds. |
| **Multiple sessions, multiple threads** | You want stronger separation between planning, development, testing, and audit. | Slower completion, stronger audit discipline. Planner, Developer, Test, and Auditor use fixed project threads. |

The choice is made once for the project. Arcgentic should not ask again every
round unless you start a new project or intentionally reset the workflow.

## What changes in real use

### Before

- One long AI coding session tries to remember everything.
- The assistant mixes planning, coding, review, and closeout in one context.
- Fixes are sometimes treated as audit work.
- The next session has to reconstruct what happened.
- "Pass" often means the assistant felt confident.

### After

- The current session is the Orchestrator.
- Planner, Developer, Test, and Auditor are separ

## tools

Current evidence:

- Codex V2 has been exercised in a real project workflow.
- V2 completion evidence is recorded in the repository.
- Simulated user workflow evidence is recorded in the repository.

Planned adoption assets:

- short Codex demo;
- example project with before/after comparison;
- Claude Code experimental run notes for `multi-session-subthread` mode and
  the hook-backed fallback path, after those are verified in a real session
  (`single-session-subagent` mode's run notes already exist at
  `tests/dogfood/gate-3-claude-code-native-broker/RESULT.md`).

## Troubleshooting

### It starts creating too many sessions

Arcgentic V2 should reuse fixed role sessions. You should see only:

```text
Orchestrator
Planner
Developer
Test
Auditor
```

If you see `R1 Developer`, `R2 Auditor`, or similar names, that is not the
intended V2 behavior.

### The Orchestrator keeps acting after dispatch

The Orchestrator should stop after dispatching a role. It should resume only
when the role returns information. If it keeps dispatching while a role is still
working, the workflow is not following V2.

### Audit keeps looping

Audit should not loop forever. Auditor decides `PASS`, `NEEDS_FIX`, or
`AUDIT_INCOMPLETE`. If the evidence is missing and Developer can repair it, the
workflow should go back to Developer. If the same audit gap cannot be resolved
by another audit pass, it should stop instead of creating another auditor loop.

### Test runs every round

Test is optional. Planner decides whether the current round needs realistic
user/session testing. Many small rounds should go directly from
Developer self-audit to Auditor.

## Status

| Area | Status |
|---|---|
| Codex V2 | Complete and real-workflow verified. |
| Claude Code V2 | Complete experimental version; `single-session-subagent` mode has real-session dogfood evidence via a foreground `Agent` tier-0 broker dispatch, `multi-session-subthread` mode and the hook-backed fallback path are still pending. |
| Fixed roles | Complete. |
| Optional Test role | Complete. |
| Developer self-audit | Complete. |
| External audit | Complete. |
| Closed-project status no-op | Complete. |
| README onboarding | Updated for adoption-first use. |
| npm bundle | Published as `arcgentic@2.2.0`. |
| Custom role/state topology | Complete. Zero-config behavior unchanged; custom topologies validated at parse time. |
| MCP-UI status panel | Complete, optional (`pip install arcgentic[mcp]`). Depends on host MCP Apps support. |

## limitations

Near-term:

- verify Claude Code V2's `multi-session-subthread` mode, the
  `SendMessage`-based reuse-dispatch path, and the hook-backed fallback path
  in a real Claude Code session (`single-session-subagent` mode's
  first-dispatch/`create` path is verified; repeat dispatch via `SendMessage`
  is implemented but not yet dogfooded);
- publish a small example project;
- add a short demo walkthrough;
- collect issue-template feedback from first users.

Longer-term:

- harden V2 across more project types;
- improve example libraries for common workflows;
- keep the README focused on adoption and first-run clarity.

## Feedback

Open an issue if:

- install failed;
- the workflow was confusing;
- a role did the wrong job;
- your project did not fit the workflow;
- Claude Code experimental mode behaved differently from the docs.

Useful feedback includes:

- which platform you used: Codex or Claude Code;
- what you asked Arcgentic to build;
- where the workflow got stuck;
- whether the issue was planning, development, test, audit, or closeout.

## License

[MIT](./LICENSE) - Copyright (c) 2026 Arc Studio
