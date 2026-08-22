# shareAI-lab/learn-claude-code

Bash is all you need - A nano claude code–like 「agent harness」, built from 0 to 1

## features

Because Claude Code is the most elegant, most complete agent harness implementation we have seen. Not because of any clever trick, but because of what it *does not* do: it does not try to be the agent. It does not impose rigid workflows. It does not substitute hand-crafted decision trees for the model's own judgment. It gives the model tools, knowledge, context management, and permission boundaries -- then gets out of the way.

Strip Claude Code down to its essence:

```
Claude Code = one agent loop
            + tools (bash, read, write, edit, glob, grep, browser...)
            + on-demand skill loading
            + context compaction
            + subagent spawning
            + task system with dependency graphs
            + async mailbox team coordination
            + task-bound worktrees for parallel edits
            + permission governance
            + hooks extension system
            + memory persistence
            + MCP external capability routing
```

That is it. The agent itself? Claude. A model. Trained by Anthropic on the full breadth of human reasoning and code. The harness did not make Claude smart. Claude was already smart. The harness gave Claude hands, eyes, and a workspace.

The takeaway is not "copy Claude Code." The takeaway is: **the best agent products come from engineers who understand that their job is the harness, not the intelligence.**

---

```
                    THE AGENT PATTERN
                    =================

    User --> messages[] --> LLM --> response
                                      |
                              contains tool_use block?
                           /                          \
                         yes                           no
                          |                             |
                    execute tools                    return text
                    append results
                    loop back -----------------> messages[]


    The model decides when to call tools and when to stop.
    The code just executes what the model asks for.
    This repo teaches you to build everything around this loop --
    the harness that makes the agent effective in a specific domain.
```
