# gotalab/goal-setter-skill

Shape rough requests into evidence-backed /goal completion contracts — an Agent Skill for Claude Code and Codex

## features

- Reconstructs the intended result before drafting.
- Adds only clauses that change the result, evidence, boundary, risk, or stop
  decision.
- Interviews one material question at a time when the request is too ambiguous
  for an honest Goal and each answer determines the next question; bundles
  independent blockers.
- Keeps Goal intake focused and requires only delegation that can improve the
  completion decision. Existing agents continue related work; new agents handle
  independent work or independent verification. Separate tasks remain
  user-directed.

Details live in [docs/RUNTIME.md](docs/RUNTIME.md). Examples live in
[docs/EXAMPLES.md](docs/EXAMPLES.md).

## installation

Pick one install path:

| If you use | Install | Invoke with |
| --- | --- | --- |
| Codex App `/plugins` | Codex App Plugin | `$goal-setter:goal-setter ...` |
| Codex local skills | Codex Skill | `$goal-setter ...` |
| Claude Code | Claude Code marketplace | `/goal-setter:goal-setter ...` |
| Another agent with Skills CLI support | Skills CLI | the agent's skill invocation syntax |

Most Codex App users should install only the **Codex App Plugin**.

## tools

Draft a goal without activating it:

```text
$goal-setter draft a goal for migrating our API client to v2
```

Shape and activate a goal:

```text
$goal-setter set a goal: all checkout tests pass after the refactor
```

goal-setter sets the Goal through Codex's native Goal mechanism. When delegated
work can materially improve Done, the Goal names the work and evidence without
embedding agent counts, models, tool arguments, or a fixed sequence. During the
run, related follow-up stays with the agent that already has the context; a new
agent is used for independent work or a clean independent review. The lead keeps
integration, important decisions, final verification, and Done. `create_thread`
creates separate user-owned tasks, so it is used only when the user explicitly
requests separate tasks, threads, or worktrees.
