# code-yeongyu/oh-my-openagent

OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.

## installation

oh-my-openagent ships in three editions of the same product: two plugins that load into a host you already run, plus one standalone edition.

**Ultimate Edition (omo for OpenCode)** is the full omo. 11 agents, 54+ lifecycle hooks, 4 built-in MCPs (websearch, context7, grep_app, lsp), all slash commands, Team Mode, `/goal`, ultrawork. Hashline edits are opt-in (`hashline_edit: true`).

**Light Edition (omo for Codex CLI)** carries the portable components that fit Codex's plugin system: `rules`, `comment-checker`, `git-bash`, `lsp`, `ultrawork`, `ulw-loop`, `ulw-execute-continuation`, and `telemetry` at the core, plus `teammode` and supporting components (`bootstrap`, `lcx`, and more), plugin-scoped MCPs for `grep_app`, `context7`, `git_bash`, and `lsp`, and the shared `ast-grep` skill. It installs Codex agent TOMLs into `~/.codex/agents/`. There are no OpenCode `team_*` tools; Codex CLI's own spawn/collaboration surface does that work.

**Senpi Edition (standalone, beta)** is the native `omo` command with the OMO extension built in. It installs from `omo-ai@beta` and loads into neither OpenCode nor Codex.

Pick the edition(s) you want.

### One-line install

| You want | Run | What lands on disk |
| :--- | :--- | :--- |
| **Ultimate** (OpenCode) | `bunx oh-my-openagent install` (TUI walks you through it) | Plugin registered in `opencode.json` + agent/model config + provider auth prompts |
| **Light** (Codex CLI) | `npx lazycodex-ai install` | `~/.codex/plugins/cache/sisyphuslabs/omo/` + local Codex marketplace cache + `~/.codex/config.toml` marketplace/plugin/agent blocks + optional autonomous permissions + component CLIs in `~/.local/bin` |
| **Both** | `bunx oh-my-openagent install --platform=both` | Both of the above |
| **Senpi edition** (beta) | `bun add -g omo-ai@beta`, then `omo` | The `omo` command: pinned senpi release with the OMO extension built in. Beta channel only; a bare `bun add -g omo-ai` fails by design. See the [install guide](docs/guide/installation.md#senpi-edition-beta-omo-via-npm-omo-ai). |

`lazycodex-ai` defaults to the Codex Light installer and runs through Node/npm. `--platform` on the shared `omo-agent-toolkit` CLI still defaults to `opencode` (Ultimate).

### Which edition should I pick?

Already on OpenCode, or want the most-tested path? **Ultimate**. Already on Codex CLI? **Light**. Want one command without installing a host first? The **Senpi edition**, which ships a pinned Senpi engine with OMO built in; bun is the recommended runtime for it, and the `@beta` tag is required. Do not install plain `omo` from npm; that is an unrelated package by a different author.

### For Humans

**Strongly recommended: let an LLM agent install this for you.** The Ultimate edition setup involves subscription detection, model selection across 11 agents, and per-provider authentication, and humans fat-finger these. An LLM agent reads the full guide and walks every step correctly.

Paste this prompt into Claude Code, AmpCode, Cursor, or any agent:

```
Install and configure oh-my-openagent by following the instructions here:
https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

If you only want the **Light edition** (Codex CLI), the installer asks whether to configure Codex for autonomous full-permissions mode. You can run it yourself in one line:

```bash
npx lazycodex-ai install
# non-interactive recommended mode:
npx lazycodex-ai install --no-tui --codex-autonomous
```

For the Light edition, Bun is not required. Use `npx lazycodex-ai install` from a Node/npm environment. Global installation is not officially supported; the installer writes the Codex plugin into `~/.codex/`.

### For LLM Agents

Fetch the full guide and follow it step by step:

```bash
curl -fsSL https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

The guide covers: platform selection, the subscription interview, provider authenticatio

## limitations

We are restructuring the codebase to support multiple agent harnesses (OpenCode, Codex, Pi, Claude Code, and others). The most urgent work is the package layering refactor: separating pure TypeScript core logic, MCP servers, skills, and adapter shims into distinct layers so the same logic can be reused across harnesses without duplication.

If you want to contribute, read the [ROADMAP](./ROADMAP.md) first. PRs related to this refactor should use the `ROADMAP` label so they are easy to track.

## Highlights

### 🪄 `ultrawork`

You're actually reading this? Wild.

Install. Type `ultrawork` (or `ulw`). Done.

Everything below, every feature, every optimization: you don't need to know any of it. It just works.

Even with only a [ChatGPT subscription ($20)](https://chatgpt.com/), a [Kimi Code subscription ($19)](https://www.kimi.com/code) or the [GLM Coding Plan ($10)](https://z.ai/subscribe), `ultrawork` works well (this project is not affiliated; these are personal recommendations). If you're eligible for pay-per-token, Kimi and GLM models won't cost much either.

|       | Feature                                                  | Edition  | What it does                                                                                                                                                                                                     |
| :---: | :------------------------------------------------------- | :------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   🤖   | **Discipline Agents**                                    | Ultimate | The main agent orchestrates the architect consult, Librarian, Explore and category workers. A full AI dev team in parallel.                                                                                     |
|   🧩   | **Codex CLI Light Edition**                              | Light    | Portable OMO components (rules, comment-checker, git-bash, LSP, ultrawork, ulw-loop, ulw-execute continuation, telemetry, teammode, and more) running inside OpenAI Codex CLI. Install via `npx lazycodex-ai install`.             |
|   👥   | **Team Mode** (opt-in)                                   | Ultimate | Lead agent + up to 8 parallel members, real-time tmux visualization, dedicated `team_*` tools. Powers `hyperplan` (5 hostile critics) and `security-research` (3 hunters + 2 PoC engineers). [Docs →](docs/guide/team-mode.md) |
|   ⚡   | **`ultrawork` / `ulw`**                                  | Both     | One word. Every agent activates. Doesn't stop until done.                                                                                                                                                        |
|   🚪   | **[IntentGate](https://factory.ai/news/terminal-bench)** | Ultimate | Keyword detection for `ultrawork`/`ulw`, `team`, and `hyperplan` (does not semantically classify intent). (Light edition only recognises the `ultrawork`/`ulw` keyword.)                                                       |
|   🔗   | **Hash-Anchored Edit Tool**                              | Ultimate | Hashline (`LINE#ID`) edit/read tagging. Opt-in: set `hashline_edit: true` in `~/.omo/omo.jsonc`. Zero stale-line errors. Inspired by [oh-my-pi](https://github.com/can1357/oh-my-pi). [The Harness Problem →](https://blog.can.ac/2026/02/12/the-harness-problem/) |
|   🛠️   | **LSP integration**                                      | Both     | Diagnostics, navigation, symbols, workspace rename. IDE precision for agents. Same LSP MCP server in both editions.                                                                                              |
|   🔎   | **AST-Grep**                                             |   Both   | Pattern-aware code search and rewriting across 25 languages. Both editions use the shared `ast-grep` skill with a provisioned `

## tools

LSP, AST-Grep, Tmux, and MCP, actually integrated, not duct-taped together. LSP gives every agent `lsp_rename`, `lsp_goto_definition`, `lsp_find_references` and `lsp_diagnostics`, IDE precision included. AST-Grep does pattern-aware code search and rewriting across 25 languages. Tmux is a full interactive terminal, so REPLs, debuggers and TUI apps stay in session. MCP brings web search, official docs and GitHub code search, all baked in.

### Skill-Embedded MCPs

MCP servers eat your context budget. We fixed that.

Skills bring their own MCP servers. They spin up on demand, scoped to the task, and go away when done. The context window stays small.

### Codes Better. Hash-Anchored Edits

The harness problem is real. Most agent failures aren't the model's fault; it's the edit tool.

> *"None of these tools give the model a stable, verifiable identifier for the lines it wants to change... They all rely on the model reproducing content it already saw. When it can't - and it often can't - the user blames the model."*
>
> <br/>- [Can Bölük, The Harness Problem](https://blog.can.ac/2026/02/12/the-harness-problem/)

Inspired by [oh-my-pi](https://github.com/can1357/oh-my-pi), we built **Hashline**. When `hashline_edit` is enabled, every line the agent reads comes back tagged with a content hash:

```
11#VK| function hello() {
22#XJ|   return "world";
33#MB| }
```

The agent edits by referencing those tags. If the file has changed since the last read, the hash won't match and the edit is rejected before it can corrupt the file. No whitespace reproduction. No stale-line errors.

### Deep Initialization. `/init-deep`

Run `/init-deep`. It generates hierarchical `AGENTS.md` files:

```
project/
├── AGENTS.md              ← project-wide context
├── src/
│   ├── AGENTS.md          ← src-specific context
│   └── components/
│       └── AGENTS.md      ← component-specific context
```

Agents auto-read relevant context. Zero manual management.

### Planning. The Ultrawork Planner

Complex task? Don't prompt and pray.

The Ultrawork Planner (`/ulw-plan`) **interviews you like a real engineer**, identifies scope and ambiguities, and writes a reviewed plan to `.omo/plans/` before touching code. `/ulw-execute` then has the main agent execute that plan in the same session. The agent knows what it's building before it starts.

### Skills

Skills aren't just prompts. Each brings domain-tuned system instructions, embedded MCP servers on demand, and scoped permissions so agents stay in bounds.

Built-ins include `playwright` (browser automation), `git-master` (atomic commits, rebase surgery) and `frontend` (design-first UI).

Add your own under `.opencode/skills/*/SKILL.md` or `~/.config/opencode/skills/*/SKILL.md`.

**Want the full feature breakdown?** See the **[Features Documentation](docs/reference/features.md)** for agents, hooks, tools, MCPs, and everything else in detail.

---

> **New to oh-my-openagent?** Read the **[Overview](docs/guide/overview.md)** to understand what you have, or check the **[Orchestration Guide](docs/guide/orchestration.md)** for how agents collaborate.

## configuration

Edit `~/.config/opencode/opencode.json` (or `opencode.jsonc`) and remove either `"oh-my-openagent"` or the legacy `"oh-my-opencode"` entry from the `plugin` array:

```bash
# Using jq
jq '.plugin = [.plugin[] | select(. != "oh-my-openagent" and . != "oh-my-opencode")]' \
    ~/.config/opencode/opencode.json > /tmp/oc.json && \
    mv /tmp/oc.json ~/.config/opencode/opencode.json
```

### Remove configuration files (optional)

```bash
# Remove the runtime config files
rm -f ~/.omo/omo.jsonc ~/.omo/omo.json

# Remove project config (if exists)
rm -f .omo/omo.jsonc .omo/omo.json

# Remove leftover legacy migration backups (if any)
rm -f ~/.config/opencode/oh-my-openagent.jsonc ~/.config/opencode/oh-my-openagent.json \
      ~/.config/opencode/oh-my-opencode.jsonc ~/.config/opencode/oh-my-opencode.json \
      .opencode/oh-my-openagent.jsonc .opencode/oh-my-openagent.json \
      .opencode/oh-my-opencode.jsonc .opencode/oh-my-opencode.json
```

### Verify removal

```bash
opencode --version
# Plugin should no longer be loaded
```

### Remove omo-codex (Codex CLI Light edition)

```bash
npx lazycodex-ai uninstall
# backward-compatible alias:
npx lazycodex-ai cleanup

omo-agent-toolkit uninstall --platform=codex
# backward-compatible alias:
omo-agent-toolkit cleanup --platform=codex
```

The uninstall command removes managed `sisyphuslabs` Codex cache/marketplace state, strips `omo@sisyphuslabs` plugin and hook-state blocks from `~/.codex/config.toml` after writing a backup, and removes agent TOML links listed in the install manifest. If a specific project still has old project-local Codex plugin state, run the command from that project or pass `--project <path>`; it repairs known project-local `.codex/config.toml` conflicts and reports project-local `.codex` artifacts without deleting project-owned files.

## features

Features you'll think should've always existed. Once you use them, you can't go back.

See the full [Features Documentation](docs/reference/features.md). The short version follows.

The main agent orchestrates; the Ultrawork Planner (`/ulw-plan`), the architect consult (architecture and debugging), Librarian (docs and code search), Explore (fast codebase grep) and the Multimodal Looker specialize, and background agents run several of them in parallel like a real dev team. LSP and AST tools cover refactoring, rename, diagnostics and AST-aware code search. The hash-anchored edit tool (opt-in via `hashline_edit: true`) validates `LINE#ID` references before applying every change, so edits are surgical and stale-line errors are gone.

AGENTS.md, README.md and conditional rules are injected into context automatically. Claude Code hooks, commands, skills, agents and MCPs run unchanged. The built-in MCPs (websearch via Exa, context7 for docs, grep_app for GitHub search, lsp) are injected at runtime by the plugin, which is why they do not show up in `opencode mcp list` (see the [MCP docs](docs/reference/features.md#native-vs-plugin-injected-mcps)). Session tools list, read, search and analyze session history.

Goal, the Todo Enforcer, the Comment Checker and Think Mode keep a run on track. `bunx oh-my-opencode doctor` checks plugin registration, config, models and environment. `fallback_models` can mix plain model strings with per-fallback object settings in the same array, agent prompts can load from files with `file://`, and sessions recover from session errors, context window limits and API failures on their own. Agent-model matching is part of the [Installation Guide](docs/guide/installation.md#step-5-understand-your-model-setup).
