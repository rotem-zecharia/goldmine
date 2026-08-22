# infinri/Writ

Governance runtime for Claude Code. Enforces workflow gates at tool time, delivers the engineering rules relevant to the work, and preserves decision provenance across sessions.

## installation

**You do not have to install this yourself.** If you are reading this you already use Claude Code, which means you already have something that reads instructions and runs commands. Point it at this page and ask it to install Writ. It handles the setup; the one piece you may need to do by hand is installing Docker, the same way you would install any other application.

**You will need:** Python 3.11 or newer and Docker (the graph database runs in a container). That is the whole list. `jq` and `curl` are used when present and fall back to Python when absent, so a machine without them installs fine.

```shell
claude plugin marketplace add infinri/Writ
claude plugin install writ@writ
```

Open Claude Code once. It detects the un-bootstrapped install and prints one absolute command on its own line, ready to paste:

```shell
bash /path/it/prints/scripts/bootstrap-plugin.sh
```

Run it and restart Claude Code. That one script does everything: environment, database, rules, background service, permissions, and workflow instructions. It is idempotent, and re-running it after an update is the whole update procedure. Check it worked with `curl http://localhost:8765/health`.

Nothing breaks while you are partway through setup. Hooks stay out of the way until the install finishes, sessions are never blocked, and the startup hook prints exactly what is still missing. Full install detail, the manual path, and troubleshooting live in [`docs/install.md`](docs/install.md). Once it is running, [`HANDBOOK.md`](HANDBOOK.md) is the operator manual: modes, gates, helper AIs, the rulebook, and the command line.

## features

For a small number of behaviors, you probably should. [Anthropic's Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) are simple, portable, and useful. If all you need is a handful of reusable instructions, Writ is unnecessary.

But Skills and governance are not the same mechanism, and the distinction is not something Anthropic's own engineering material leaves obscure.

Anthropic documents that every installed skill contributes metadata to the system prompt, then **Claude decides whether the skill is relevant** before loading its full `SKILL.md` into context. Anthropic also documents the cost of that design in its own [context-engineering guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): context is finite, recall degrades as context grows, every added token consumes part of the model's attention budget, and good context engineering means finding the smallest high-signal set of tokens that produces the desired behavior.

Anthropic documents the other half of the distinction too. In the Agent Skills article, it notes that some operations need the deterministic reliability of code rather than model generation. Claude Code's own [hooks documentation](https://code.claude.com/docs/en/hooks-guide) exposes `PreToolUse`, which runs before a tool executes and can deny the action outright. A denying hook still blocks the action even when Claude Code is running in a permission-bypass mode.

So the primitives already exist, and the tradeoff is already understood.

A Skill can say:

> Write the test first.

A tool-time gate can say:

> No. This write does not run until the test gate is open.

Those are different guarantees.
