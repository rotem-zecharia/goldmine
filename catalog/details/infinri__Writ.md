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

## Enforcement

You have probably watched this happen. You tell the AI how you want things done: write the test first, follow the pattern already in the file, ask before touching the database. It agrees. It works that way for a while. Then somewhere in a long session it stops, and nothing announces that it stopped. You find out in review, or you find out in production, or you do not find out.

That is not the AI being careless. An instruction in context is still an instruction: it can be compacted away, diluted by newer context, misapplied, or simply ignored, and nothing about putting a rule in the prompt makes violating it mechanically impossible. Instructions and enforcement are different primitives, and only one of them can refuse.

Writ supplies the second primitive for the parts of the process you choose to gate. It sits between the AI and your files. In Work mode, a write attempted before you have approved a plan is refused. Not discouraged, refused, by code that runs whether or not the AI is still paying attention to what you said an hour ago.

**Enforcement solves only half the problem.** A large rulebook cannot simply be pasted into every turn, so Writ also moves rule selection outside the model. It looks at the work happening now and delivers only the rules that apply. Tool-time checks do not depend on the model remembering the process, and contextual delivery lets the rulebook grow without the cost of every turn growing with it.

Two boundaries hold no matter what, including when the background service is down and inside subagents. Writes to credential files (keys, `.env`, SSH material) are refused in every mode with no server involved. And the approval token cannot be created or spent without a human keystroke, so **advancing the workflow and writing new rules into the rulebook halt even when raw file writes do not.**

**What a review finding does.** A recorded CRITICAL verdict turns the next `git commit` into a confirmation prompt naming the unresolved findings. It is a stop and ask, not an absolute block: you can confirm and commit anyway, and that choice is recorded in the audit log. The part that carries the weight is that the AI cannot clear its own verdict. Writing a review record directly is refused outright; verdicts are written only from the reviewer's own output, and the only route an AI has to lifting a block is to fix t

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

### "Mandatory" is not a property an instruction can give itself

A skill can contain `MUST`, `REQUIRED`, `NEVER`, or `MANDATORY` as many times as its author wants. The model still has to discover the skill, load it, retain the relevant instruction, interpret it correctly, and choose the expected action.

That is an instruction with forceful wording. It is not external enforcement.

[Superpowers](https://github.com/obra/superpowers) makes the distinction unusually easy to see. It describes its workflows as mandatory, yet its own [porting guide](https://github.com/obra/superpowers/blob/main/docs/porting-to-a-new-harness.md) says the full bootstrap is injected into model context at the start of every session, calls that bootstrap "the entire integration," and states that without it the skill files are inert. The same guide treats automatic session-start injection as a non-negotiable requirement for a supported harness.

That is not a criticism of the quality of its methodology. It is the architectural boundary of an instruction-driven methodology.

A workflow does not become mandatory because the instructions describing it say that it is mandatory.

Writ draws the boundary somewhere else. If a checkpoint is important enough to call mandatory, Writ's position is that the model should not be the final authority over whether it happened. Selected checkpoints run outside the model and can refuse the action.

### The token incentive is worth saying out loud

Anthropic's own engineering guidance says context is a finite resource, additional tokens consume attention, and unnecessary context should be reduced. Its Skills design uses progressive disclosure specifically to avoid loading everything at once.

Anthropic's [API pricing](https://platform.claude.com/docs/en/about-claude/pricing) also bills input tokens.

That does **not** prove why Anthropic chose the product boundary it chose, and Writ makes no claim about anyone's private motive. It does create an incentive tension that users are allowed to notice: users benefit when governance requires less model context, while a token-priced API vendor earns revenue from inference usage.

Maybe the boundary exists because Skills prioritize simplicity and portability. Maybe it reflects
