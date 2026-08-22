# Yeachan-Heo/oh-my-claudecode

Teams-first Multi-agent orchestration for Claude Code

## installation

**Step 1: Install**

Marketplace/plugin install (recommended for most Claude Code users).
These are Claude Code slash commands — enter them **one at a time** (pasting both lines at once will fail):

```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
```

Then:

```bash
/plugin install oh-my-claudecode
```

If you prefer the npm CLI/runtime path instead of the marketplace flow:

```bash
npm i -g oh-my-claude-sisyphus@latest
```

> **Known npm warning:** npm may print `deprecated prebuild-install@7.1.3` during the CLI install.
> This currently comes from the upstream `better-sqlite3` native-addon dependency
> (`better-sqlite3 -> prebuild-install`); `prebuild-install@7.1.3` is still the latest
> published version, so there is no safe repo-side dependency bump or override to remove
> the warning yet. The warning is tracked in [#2913](https://github.com/Yeachan-Heo/oh-my-claudecode/issues/2913)
> and does not by itself mean the OMC CLI install failed.

**Step 2: Setup**

```bash
# Inside a Claude Code / OMC session
/setup
/omc-setup

# From your terminal
omc setup
```

If you run OMC via `omc --plugin-dir <path>` or `claude --plugin-dir <path>`, add `--plugin-dir-mode` to `omc setup` (or export `OMC_PLUGIN_ROOT` before running it) so the installer doesn't duplicate skills/agents that the plugin already provides at runtime. See the [Plugin directory flags section in REFERENCE.md](./docs/REFERENCE.md#plugin-directory-flags) for a complete decision matrix and all available flags.

**Step 3: Build something**

```bash
# Inside a Claude Code / OMC session
/autopilot "build a REST API for managing tasks"

# Natural-language in-session shortcut
autopilot: build a REST API for managing tasks
```

#### Named autopilot stage profiles (v1)

Select a configured stage profile only through `/autopilot --workflow <name> <task>`:

```text
/autopilot --workflow plan-build-qa "build a REST API for managing tasks"
```

Profiles are configured under `autopilot.workflows` in `.claude/omc.jsonc` (project) or `~/.config/claude-omc/config.jsonc` (user). A v1 profile contains only `version: 1` and `stages`:

```jsonc
{
  "autopilot": {
    "workflows": {
      "plan-build-qa": {
        "version": 1,
        "stages": ["ralplan", "execution", "qa"]
      }
    }
  }
}
```

The admitted sequences are `[ralplan, execution]`, `[ralplan, execution, ralph]`, `[ralplan, execution, qa]`, and `[ralplan, execution, ralph, qa]`. A project profile of the same name wholly replaces the user profile; different names coexist. Environment variables cannot define profiles. Profiles remain within autopilot's existing state, cancel, resume, Stop, and HUD lifecycle; legacy invocations without `--workflow` remain compatible.

Named profiles currently require Linux with the `flock` utility because their transcript evidence boundary uses Linux no-follow file-descriptor traversal and their recoverable mutation lock uses kernel advisory locking. Unsupported environments reject explicit `--workflow` invocation before creating or changing autopilot state; legacy autopilot remains available.

V1 intentionally excludes model fields or routing (`stageModels`), inline execution, dynamic commands/modes/state, arbitrary stages or plugins, and the separate custom-skill frontmatter parser mismatch. See [Named Autopilot Stage Profiles ADR](docs/adr/03487-named-autopilot-stage-profiles.md) and [Reference](docs/REFERENCE.md#named-autopilot-stage-profiles-v1).


That's it. Everything else is automatic.

## tools

OMC exposes two different surfaces:

- **Terminal CLI commands**: run `omc ...` from your shell after installing the npm/runtime path (`npm i -g oh-my-claude-sisyphus@latest`) or from a local checkout.
- **In-session skills**: run `/...` inside a Claude Code session after installing the plugin/setup flow.

| Feature                                        | Terminal CLI                                  | In-session skill                                                        | Notes                                                                                                                                |
| ---------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Setup                                          | `omc setup`                                   | `/setup` or `/omc-setup`                                                | Both are real entrypoints. `/setup` is the easiest plugin-first path.                                                                |
| Ask providers                                  | `omc ask codex "review this patch"`           | `/ask codex "review this patch"`                                        | Both route through the same advisor flow. Providers: `claude`, `codex`, `gemini`, `antigravity`, `grok`, `cursor`.                                            |
| Team orchestration                             | `omc team 2:codex "review auth flow"`         | `/team 3:executor "fix all TypeScript errors"`                          | Both exist, but they are different runtimes: `omc team` launches tmux CLI workers; `/team` runs the in-session native team workflow. |
| Autopilot / Ralph / Ultrawork / Deep Interview | —                                             | `/autopilot ...`, `/ralph ...`, `/ultrawork ...`, `/deep-interview ...` | These are in-session skills. There is no `omc autopilot` / `omc ralph` / `omc ultrawork` CLI subcommand in this repo.                |
| Autoresearch                                   | `omc autoresearch` (**hard-deprecated shim**) | `/deep-interview --autoresearch ...` + `/oh-my-claudecode:autoresearch` | Setup stays in deep-interview; execution now belongs to the stateful skill.                                                          |

### VS Code, Agent SDK, and automation scope

- **VS Code / IDE extension**: OMC does not ship a VS Code extension and does not document extension-specific install or automation flows. Use the Claude Code plugin or terminal CLI surfaces above; IDE integrations are only an optional way to access Claude Code itself.
- **Agent SDK / programmatic usage**: the npm package exports TypeScript helpers such as `createOmcSession()` and prompt expansion utilities for local Node.js programs using `@anthropic-ai/claude-agent-sdk`. This is a library surface, not a replacement for the Claude Code plugin UI.
- **CI/CD and headless automation**: prefer deterministic terminal commands (`omc setup`, `omc ask`, `omc session search`, repository scripts such as `npm run sync-metadata:verify`) and set `ANTHROPIC_API_KEY` or provider-specific CLI auth in the runner environment. Do not rely on interactive slash commands (`/autopilot`, `/ralph`, `/team`) in CI; they require an active Claude Code session.

### Not Sure Where to Start?

If you're uncertain about requirements, have a vague idea, or want to micromanage the design:

```
/deep-interview "I want to build a task management app"
```

The deep interview uses Socratic questioning to clarify your thinking before any code is written. It exposes hidden assumptions and measures clarity across weighted dimensions, ensuring you know exactly what to build before execution begins.

## Team Mode (Recommended)

Starting in **v4.1.7**, **Team** is the canonical orch

## features

- **Zero configuration required** - Works out of the box with intelligent defaults
- **Team-first orchestration** - Team is the canonical multi-agent surface
- **Natural language interface** - No commands to memorize, just describe what you want
- **Automatic parallelization** - Complex tasks distributed across specialized agents
- **Persistent execution** - Won't give up until the job is verified complete
- **Cost optimization** - Smart model routing saves 30-50% on tokens
- **Learn from experience** - Automatically extracts and reuses problem-solving patterns
- **Real-time visibility** - HUD statusline shows what's happening under the hood

---

## Features

### Orchestration Modes

Multiple strategies for different use cases — from Team-backed orchestration to token-efficient refactoring. [Learn more →](https://yeachan-heo.github.io/oh-my-claudecode-website/docs/#execution-modes)

| Mode                        | What it is                                                                              | Use For                                                                 |
| --------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Team (recommended)**      | Canonical staged pipeline (`team-plan → team-prd → team-exec → team-verify → team-fix`) | Coordinated Claude agents on a shared task list                         |
| **omc team (CLI)**          | tmux CLI workers — real `claude`/`codex`/`gemini`/`antigravity`/`grok`/`cursor-agent` processes in split-panes       | Codex/Gemini/Antigravity/Grok/Cursor CLI tasks; on-demand spawn, die when done             |
| **ccg**                     | Tri-model advisors via `/ask codex` + `/ask antigravity`, Claude synthesizes             | Mixed backend+UI work needing both Codex and Antigravity                     |
| **Autopilot**               | Autonomous execution (single lead agent)                                                | End-to-end feature work with minimal ceremony                           |
| **Ultrawork**               | Maximum parallelism (non-team)                                                          | Burst parallel fixes/refactors where Team isn't needed                  |
| **Ralph**                   | Persistent mode with verify/fix loops                                                   | Tasks that must complete fully (no silent partials)                     |
| **UltraQA**                 | QA cycling until tests/build/lint/typecheck goals pass                                  | Quality gates that need repeat diagnose/fix cycles                      |
| **Claude Code `/goal`**     | Native Claude Code cross-turn goal loop                                                 | One measurable session completion condition; not an OMC evidence ledger |
| **Artifact-only Ultragoal** | Durable goal/checkpoint/evidence artifacts without starting a loop                      | Handoffs, audits, or unavailable/conflicting loop runtimes              |
| **Pipeline**                | Sequential, staged processing                                                           | Multi-step transformations with strict ordering                         |
| **Ultrapilot (legacy)**     | Deprecated compatibility mode (autopilot pipeline alias)                                | Existing workflows and older docs                                       |

### Goal Workflow Guidance

Use only one primary loop authority in a session. Claude Code `/goal` is useful for a native cross-turn completion condition, while Ralph owns single-agent verified completion, Team owns parallel staged execution, and UltraQA owns repeated quality-gate cycling. Artifact-only Ultragoal is the safe fallback when you need durable goal artifacts and evidence without starting another loop.

For `/goal` behavior, rely on Claude Code/Anthropic sources: the [Claude Code `/goa

## requirements

- [Claude Code](https://docs.anthropic.com/claude-code) CLI
- Claude Max/Pro subscription OR Anthropic API key

### Platform & tmux

OMC features like `omc team` and rate-limit detection require **tmux**:

| Platform       | tmux provider                                         | Install                 |
| -------------- | ----------------------------------------------------- | ----------------------- |
| macOS          | [tmux](https://github.com/tmux/tmux)                  | `brew install tmux`     |
| Ubuntu/Debian  | tmux                                                  | `sudo apt install tmux` |
| Fedora         | tmux                                                  | `sudo dnf install tmux` |
| Arch           | tmux                                                  | `sudo pacman -S tmux`   |
| Windows        | [psmux](https://github.com/marlocarlo/psmux) (native) | `winget install psmux`  |
| Windows (WSL2) | tmux (inside WSL)                                     | `sudo apt install tmux` |

> **Windows users:** [psmux](https://github.com/marlocarlo/psmux) provides a native `tmux` binary for Windows with 76 tmux-compatible commands. No WSL required.

### Optional: Multi-AI Orchestration

OMC can optionally orchestrate external AI providers for cross-validation and design consistency. These are **not required** — OMC works fully without them.

| Provider                                                                | Install                                                      | What it enables                                                           |
| ----------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| [Antigravity CLI](https://antigravity.google) (`agy`)                   | Install per the [official instructions](https://antigravity.google) (provides the `agy` binary) | Design review, UI consistency — Google's successor to the Gemini CLI |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)               | `npm install -g @google/gemini-cli`                          | Design review, UI consistency (1M token context) — enterprise/API-key access unaffected |
| [Codex CLI](https://github.com/openai/codex)                            | `npm install -g @openai/codex`                               | Architecture validation, code review cross-check                          |
| [Grok Build](https://build.grok.com)                                    | Download from build.grok.com (`grok` at `~/.grok/bin/grok`) | Code review, analysis cross-check                                         |

> **Migrating from Gemini CLI:** Per Google's announcement, the Gemini CLI is being superseded by the Antigravity CLI (`agy`); see the [official Antigravity docs](https://antigravity.google). Use `omc team N:antigravity` and `omc ask antigravity` wherever you previously used `gemini`. Windows headless support for `agy` is unknown/untested — report issues upstream.

**Cost:** 3 Pro plans (Claude + Antigravity/Gemini + ChatGPT) cover everything for ~$60/month.

---

## License

MIT

---

<div align="center">

**Inspired by:** [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) • [claude-hud](https://github.com/ryanjoachim/claude-hud) • [Superpowers](https://github.com/obra/superpowers) • [everything-claude-code](https://github.com/affaan-m/everything-claude-code) • [Ouroboros](https://github.com/Q00/ouroboros)

**Zero learning curve. Maximum power.**

</div>

<!-- OMC:FEATURED-CONTRIBUTORS:START -->
