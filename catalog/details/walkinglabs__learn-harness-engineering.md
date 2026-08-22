# walkinglabs/learn-harness-engineering

Harness engineering beginner tutorial, from 0 to 1

## features

The question isn't "can models write code?" They can. The question is: **can they reliably complete real engineering tasks inside real repositories, over multiple sessions, without constant human supervision?**

Right now, the answer is: not without a harness.

```text
    WITHOUT HARNESS                            WITH HARNESS
    ==============                             ============

    Session 1: agent writes code               Session 1: agent reads instructions
               agent breaks tests                         agent runs init.sh
               agent says "done"                          agent works on one feature
               you fix it manually                        agent verifies before claiming done
                                                          agent updates progress log
    Session 2: agent starts fresh                         agent commits clean state
               agent has no memory
               of what happened before         Session 2: agent reads progress log
               agent re-does work                         agent picks up exactly where it left off
               or does something else entirely            agent continues the unfinished feature
               you fix it again                           you review, not rescue

    Result: you spend more time                Result: agent does the work,
            cleaning up than if you                    you verify the result
            did it yourself
```

The questions this course actually cares about:

- Which harness designs improve task completion rates?
- Which designs reduce rework and incorrect completions?
- Which mechanisms keep long-running tasks progressing steadily?
- Which structures keep the system maintainable after multiple agent runs?

---

## installation

You don't need to read all 14 lectures before you start getting value. If you're already using a coding agent on a real project, here's how to improve it right now.

The idea is simple: instead of just writing prompts, give your agent a set of structured files that define what to do, what's been done, and how to verify the work. These files live inside your repo, so every session starts from the same state.

```text
    YOUR PROJECT ROOT
    ├── AGENTS.md              <-- the agent's operating manual
    ├── CLAUDE.md              <-- (alternative, if using Claude Code)
    ├── init.sh                <-- runs install + verify + start
    ├── feature_list.json      <-- what features exist, which are done
    ├── claude-progress.md     <-- session progress (historical filename; agent-agnostic)
    └── src/                   <-- your actual code
```

Grab the starter templates from the [Resource Library](https://walkinglabs.github.io/learn-harness-engineering/en/resources/) and drop them into your project. That's it. Four files, and your agent sessions will already be significantly more stable than running on prompts alone.

`claude-progress.md` is a generic, repository-local session progress log; the
name is retained for compatibility with the course examples. It is not tied to
Claude Code and is not updated automatically by any agent. Codex, OpenHands,
Antigravity, and other coding agents can use the same file when their root
instructions tell them to read it at startup and update it before handoff.

---

## requirements

This is a course where you actually run coding agents.

You need at least one of these tools:

- Claude Code
- Codex
- Another IDE or CLI coding agent that supports file editing, command execution, and multi-step tasks

The course assumes you can:

- Open a local repository
- Allow the agent to edit files
- Allow the agent to run commands
- Inspect output and re-run tasks

If you don't have such a tool, you can still read the course content, but you won't be able to complete the projects as intended.

---

## tools

Zero-dependency utilities you can run without installing Node.js.

- [**audit-harness.sh**](./tools/audit-harness.sh): A shell-based audit script that checks an existing repo against all five harness subsystems (L03–L12). Exits 0 when all CRITICAL items pass. No Node.js required — complements `harness-creator`'s `validate-harness.mjs`.

```bash
