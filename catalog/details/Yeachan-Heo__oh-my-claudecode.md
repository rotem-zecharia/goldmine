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

## requirements

- [Claude Code](https://docs.anthropic.com/claude-code) CLI
- Claude Max/Pro subscription OR Anthropic API key
