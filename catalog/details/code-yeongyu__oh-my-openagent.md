# code-yeongyu/oh-my-openagent

OmO: Drop your tokens. Ultrawork. Done.

## installation

oh-my-openagent ships in three editions of the same product: two plugins that load into a host you already run, plus one standalone edition.

- **Ultimate Edition (omo for OpenCode)** — full omo. 11 agents, 54+ lifecycle hooks, 5 built-in MCPs, all slash commands, Team Mode, `/goal`, ultrawork — everything. Hashline edits are opt-in (`hashline_edit: true`).
- **Light Edition (omo for Codex CLI)** — the portable components that fit Codex's plugin system: `rules`, `comment-checker`, `git-bash`, `lsp`, `ultrawork`, `ulw-loop`, `ulw-execute-continuation`, and `telemetry` at the core, plus `teammode` and supporting components (`bootstrap`, `lcx`, and more), plugin-scoped MCPs for `grep_app`, `context7`, `git_bash`, and `lsp`, and the shared `ast-grep` skill. It installs Codex agent TOMLs into `~/.codex/agents/`. No OpenCode `team_*` tools — Codex CLI's own spawn/collaboration surface does that work.
- **Senpi Edition (standalone, beta)** — the native `omo` command with the OMO extension built in. It installs from `omo-ai@beta` rather than loading into OpenCode or Codex.

Pick the edition(s) you want.

### TL;DR

| You want | Run | What lands on disk |
| :--- | :--- | :--- |
| **Ultimate** (OpenCode) | `bunx oh-my-openagent install` (TUI walks you through it) | Plugin registered in `opencode.json` + agent/model config + provider auth prompts |
| **Light** (Codex CLI) | `npx lazycodex-ai install` | `~/.codex/plugins/cache/sisyphuslabs/omo/` + local Codex marketplace cache + `~/.codex/config.toml` marketplace/plugin/agent blocks + optional autonomous permissions + component CLIs in `~/.local/bin` |
| **Both** | `bunx oh-my-openagent install --platform=both` | Both of the above |
| **Senpi edition** (beta) | `npm i -g omo-ai@beta`, then `omo` | The `omo` command: pinned senpi release with the OMO extension built in. Beta channel only; a bare `npm i -g omo-ai` fails by design. See the [install guide](docs/guide/installation.md#senpi-edition-beta-omo-via-npm-omo-ai). |

`lazycodex-ai` defaults to the Codex Light installer and runs through Node/npm. `--platform` on the shared `omo-agent-toolkit` CLI still defaults to `opencode` (Ultimate).

### Which edition should I pick?

- Already use OpenCode, or want the most-tested path? Choose **Ultimate**: `bunx oh-my-openagent install`.
- Already use Codex CLI? Choose **Light**: `npx lazycodex-ai install`.
- Want one command without installing a host first? Choose **Senpi/native (beta)**: `npm i -g omo-ai@beta`.

Ultimate and Light are plugins that load into a host you already run. Senpi is standalone: it ships a pinned Senpi engine with OMO built in.

For Senpi, the `@beta` tag is required; bare `npm i -g omo-ai` fails by design. Do not install plain `omo` from npm: it is an unrelated package by a different author.

### For Humans

**Strongly recommended: let an LLM agent install this for you.** The Ultimate edition setup involves subscription detection, model selection across 11 agents, and per-provider authentication — humans fat-finger these. An LLM agent reads the full guide and walks every step correctly.

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
curl -fsSL https://raw.githubusercontent.com/code-yeongy

## limitations

We are restructuring the codebase to support multiple agent harnesses (OpenCode, Codex, Pi, Claude Code, and others). The most urgent work is the package layering refactor: separating pure TypeScript core logic, MCP servers, skills, and adapter shims into distinct layers so the same logic can be reused across harnesses without duplication.

If you want to contribute, read the [ROADMAP](./ROADMAP.md) first. PRs related to this refactor should use the `ROADMAP` label so we can track them.

## Highlights

### 🪄 `ultrawork`

You're actually reading this? Wild.

Install. Type `ultrawork` (or `ulw`). Done.

Everything below, every feature, every optimization: you don't need to know any of it. It just works.

Even with only the following subscriptions, `ultrawork` works well (this project is not affiliated; these are personal recommendations):
- [ChatGPT Subscription ($20)](https://chatgpt.com/)
- [Kimi Code Subscription ($19)](https://www.kimi.com/code)
- [GLM Coding Plan ($10)](https://z.ai/subscribe)
- If you're eligible for pay-per-token, using Kimi and Gemini models won't cost much.

|       | Feature                                                  | Edition  | What it does                                                                                                                                                                                                     |
| :---: | :------------------------------------------------------- | :------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   🤖   | **Discipline Agents**                                    | Ultimate | Sisyphus orchestrates Hephaestus, Oracle, Librarian, Explore. A full AI dev team in parallel.                                                                                                                    |
|   🧩   | **Codex CLI Light Edition**                              | Light    | Portable OMO components (rules, comment-checker, git-bash, LSP, ultrawork, ulw-loop, ulw-execute continuation, telemetry, teammode, and more) running inside OpenAI Codex CLI. Install via `npx lazycodex-ai install`.             |
|   👥   | **Team Mode** (v4.0, opt-in)                             | Ultimate | Lead agent + up to 8 parallel members, real-time tmux visualization, dedicated `team_*` tools. Powers `hyperplan` (5 hostile critics) and `security-research` (3 hunters + 2 PoC engineers). [Docs →](docs/guide/team-mode.md) |
|   ⚡   | **`ultrawork` / `ulw`**                                  | Both     | One word. Every agent activates. Doesn't stop until done.                                                                                                                                                        |
|   🚪   | **[IntentGate](https://factory.ai/news/terminal-bench)** | Ultimate | Analyzes true user intent before classifying or acting. No more literal misinterpretations. (Light edition only recognises the `ultrawork`/`ulw` keyword.)                                                       |
|   🔗   | **Hash-Anchored Edit Tool**                              | Ultimate | Hashline (`LINE#ID`) edit/read tagging. Opt-in: set `hashline_edit: true` in `~/.omo/omo.jsonc`. Zero stale-line errors. Inspired by [oh-my-pi](https://github.com/can1357/oh-my-pi). [The Harness Problem →](https://blog.can.ac/2026/02/12/the-harness-problem/) |
|   🛠️   | **LSP integration**                                      | Both     | Diagnostics, navigation, symbols, workspace rename. IDE precision for agents. Same LSP MCP server in both editions.                                                                                              |
|   🔎   | **AST-Grep**                                             |   Both   | Pattern-aware code search and rewriting across 25 languages. Ultimate uses the MCP tools; Light uses the shared `ast-gr

## tools

LSP, AST-Grep, Tmux, and MCP, actually integrated, not duct-taped together.

- **LSP**: `lsp_rename`, `lsp_goto_definition`, `lsp_find_references`, `lsp_diagnostics`. IDE precision for every agent.
- **AST-Grep**: Pattern-aware code search and rewriting across 25 languages.
- **Tmux**: Full interactive terminal. REPLs, debuggers, TUI apps. Your agent stays in session.
- **MCP**: Web search, official docs, GitHub code search. All baked in.

### Skill-Embedded MCPs

MCP servers eat your context budget. We fixed that.

Skills bring their own MCP servers. They spin up on demand, scoped to the task, and go away when done. The context window stays clean.

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

The agent edits by referencing those tags. If the file has changed since the last read, the hash won't match and the edit is rejected before any corruption. No whitespace reproduction. No stale-line errors.

Grok Code Fast 1: **6.7% → 68.3%** success rate, just from changing the edit tool.

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

### Planning. Prometheus

Complex task? Don't prompt and pray.

Prometheus **interviews you like a real engineer**, identifies scope and ambiguities, and writes a verified plan to `.omo/plans/` before touching code. `/ulw-execute` then starts an **Atlas** work session from that plan. The agent knows what it's building before it starts.

### Skills

Skills aren't just prompts. Each brings:

- Domain-tuned system instructions.
- Embedded MCP servers, on demand.
- Scoped permissions so agents stay in bounds.

Built-ins: `playwright` (browser automation), `git-master` (atomic commits, rebase surgery), `frontend` (design-first UI).

Add your own under `.opencode/skills/*/SKILL.md` or `~/.config/opencode/skills/*/SKILL.md`.

**Want the full feature breakdown?** See the **[Features Documentation](docs/reference/features.md)** for agents, hooks, tools, MCPs, and everything else in detail.

---

> **New to oh-my-openagent?** Read the **[Overview](docs/guide/overview.md)** to understand what you have, or check the **[Orchestration Guide](docs/guide/orchestration.md)** for how agents collaborate.

## features

Features you'll think should've always existed. Once you use them, you can't go back.

See full [Features Documentation](docs/reference/features.md).

**Quick Overview:**
- **Agents**: Sisyphus (the main agent), Prometheus (planner), Oracle (architecture/debugging), Librarian (docs/code search), Explore (fast codebase grep), Multimodal Looker
- **Background Agents**: Run multiple agents in parallel like a real dev team
- **LSP & AST Tools**: Refactoring, rename, diagnostics, AST-aware code search
- **Hash-anchored Edit Tool** (opt-in via `hashline_edit: true`): `LINE#ID` references validate content before applying every change. Surgical edits, zero stale-line errors
- **Context Injection**: Auto-inject AGENTS.md, README.md, conditional rules
- **Claude Code Compatibility**: Full hook system, commands, skills, agents, MCPs
- **Built-in MCPs**: websearch (Exa), context7 (docs), grep_app (GitHub search) — injected at runtime by the plugin; not visible in `opencode mcp list` (see [MCP docs](docs/reference/features.md#native-vs-plugin-injected-mcps))
- **Session Tools**: List, read, search, and analyze session history
- **Productivity Features**: Goal, Todo Enforcer, Comment Checker, Think Mode, and more
- **Doctor Command**: Built-in diagnostics (`bunx oh-my-opencode doctor`) verify plugin registration, config, models, and environment
- **Model Fallbacks**: `fallback_models` can mix plain model strings with per-fallback object settings in the same array
- **File Prompts**: Load prompts from files with `file://` support in agent configurations
- **Session Recovery**: Automatic recovery from session errors, context window limits, and API failures
- **Model Setup**: Agent-model matching is built into the [Installation Guide](docs/guide/installation.md#step-5-understand-your-model-setup)

## configuration

Opinionated defaults, adjustable if you insist.

See [Configuration Documentation](docs/reference/configuration.md).

**Quick Overview:**
- **Config Locations**: User `~/.omo/omo.jsonc` plus walked project `.omo/omo.jsonc` configs up to `$HOME`; closest wins. Legacy `oh-my-*` files are migrated once into `omo.jsonc`.
- **JSONC Support**: Comments and trailing commas supported
- **Agents**: Override models, temperatures, prompts, and permissions for any agent
- **Built-in Skills**: `playwright` (browser automation), `git-master` (atomic commits)
- **Sisyphus Agent**: Main orchestrator with Prometheus (Planner) and Metis (Plan Consultant)
- **Background Tasks**: Configure concurrency limits per provider/model
- **Categories**: Domain-specific task delegation (`visual-engineering`, `ultrabrain`, `deep`, `artistry`, `quick`, `unspecified-low`, `unspecified-high`, `writing`, plus custom names)
- **Hooks**: 54+ lifecycle hooks (61 with Team Mode), all configurable via `disabled_hooks`
- **MCPs**: Built-in websearch (Exa), context7 (docs), grep_app (GitHub search) — runtime-injected, not shown in `opencode mcp list`
- **LSP**: Full LSP support with refactoring tools
- **Experimental**: Aggressive truncation, auto-resume, and more


## Author's Note

**Want the philosophy?** Read the [Ultrawork Manifesto](docs/manifesto.md).

---

I burned through $24K in LLM tokens on personal projects. Tried every tool. Configured everything to death. OpenCode won.

Every problem I hit, the fix is baked into this plugin. Install and go.

If OpenCode is Debian/Arch, oh-my-openagent is Ubuntu/[Omarchy](https://omarchy.org/).

Heavily influenced by [AmpCode](https://ampcode.com) and [Claude Code](https://code.claude.com/docs/overview). Features ported, often improved. Still building. It's **Open**Code.

Other harnesses promise multi-model orchestration. We ship it. Stability too. And features that actually work.

I'm this project's most obsessive user:
- Which model has the sharpest logic?
- Who's the debugging god?
- Who writes the best prose?
- Who dominates frontend?
- Who owns backend?
- What's fastest for daily driving?
- What are competitors shipping?

This plugin is the distillation. Take the best. Got improvements? PRs welcome.

**Stop agonizing over harness choices.**
**I'll research, steal the best, and ship it here.**

Sounds arrogant? Have a better way? Contribute. You're welcome.

No affiliation with any project or model mentioned. Just personal experimentation.

Credit: The LazyCodex name idea is inspired by [LazyVim](https://github.com/LazyVim/LazyVim). The Ultragoal and UltraQA ideas are inspired by [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex), reimplemented from concept for OmO.

99% of this project was built with OpenCode. I don't really know TypeScript, **but I personally reviewed and largely rewrote this doc.**

## Loved by professionals at

- [Indent](https://indentcorp.com)
  - Makers of Spray (influencer marketing solution), vovushop (cross-border commerce platform), and vreview (AI commerce review marketing solution).
- [Google](https://google.com)
- [Microsoft](https://microsoft.com)
- [Vercel](https://vercel.com)
- [ELESTYLE](https://elestyle.jp)
  - Makers of elepay (multi-mobile payment gateway) and OneQR (mobile application SaaS for cashless solutions).
- [Deepgram](https://deepgram.com)

*Special thanks to [@junhoyeo](https://github.com/junhoyeo) for this amazing hero image.*
