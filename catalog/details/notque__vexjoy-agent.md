# notque/vexjoy-agent

VexJoy AI Agent with Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.

## installation

```bash
git clone https://github.com/notque/vexjoy-agent.git ~/vexjoy-agent
cd ~/vexjoy-agent
./install.sh
```

Links into `~/.claude/` and mirrors into `~/.codex/`, `~/.factory/`, `~/.reasonix/` — each mirror only when that runtime is detected (its command on PATH or its home dir already exists). The installer asks symlink (live updates via `git pull`) or copy (stable snapshot).

Want only part of the toolkit? Run `./install.sh --configure` to pick which skills, agents, and hooks install, or copy `.local.example/profile.yaml` to `.local/profile.yaml` and edit. No profile file = full install, unchanged behavior. Credit: [@thomasvan](https://github.com/thomasvan). Details: [.local.example/README.md](.local.example/README.md).

| CLI | Entry Point |
|-----|-------------|
| Claude Code | `/do` |
| Codex | `$do` |
| Factory | `/do` |
| Reasonix | `/do` |

**Full setup:** [docs/start-here.md](docs/start-here.md)

<details>
<summary><b>Codex CLI Parity</b></summary>

Mirrors agents, skills, and supported hooks into `~/.codex/`. The original six-hook allowlist was correct for Codex v0.114, when tool hooks only intercepted Bash. Current support requires Codex v0.144.1+ and classifies the 74 Claude hook registrations as **26 native, 35 adapter-backed, and 13 unsupported** (61 supported). These are registration counts, not unique hook files. The installer also preserves explicit per-subagent model routing for GPT-5.6 Sol by setting the MultiAgent V2 compatibility keys documented in [openai/codex#31814](https://github.com/openai/codex/issues/31814).

Codex now exposes `apply_patch` to tool hooks. VexJoy's adapter converts each patch operation into the Write/Edit payload expected by existing guards, but it cannot intercept writes performed through `unified_exec`, unmatched MCP tools, WebSearch, or other unsupported tool paths. PreCompact and Stop adapters also receive less telemetry than Claude Code: Codex does not provide Claude's `conversation_history` or `session_data`. This is expanded compatibility, not full Claude parity.

After install or any hook-definition change, run `/hooks` in Codex and review the new definitions before trusting them. Codex hash-trusts hook commands and skips changed, unreviewed definitions.

</details>

<details>
<summary><b>Gemini CLI / Antigravity CLI Support (removed)</b></summary>

Gemini CLI support removed (deprecated upstream, transitioned to Antigravity CLI); Antigravity support pending CLI maturity. Per Google's [transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), Gemini CLI stops serving requests on **2026-06-18** for Google AI Pro / Ultra and free Gemini Code Assist for individuals. Gemini **API** integrations (image-gen backends, sprite pipeline, `GEMINI_API_KEY`) are unaffected and stay in the toolkit.

If a prior install mirrored into `~/.gemini/`, remove the stale mirrors with:

```bash
rm -rf ~/.gemini/skills ~/.gemini/agents ~/.gemini/hooks ~/.gemini/scripts ~/.gemini/antigravity/plugins/vexjoy-agent
```

</details>

<details>
<summary><b>Factory CLI Support</b></summary>

Mirrors agents (as "droids"), skills, and all hooks into `~/.factory/`. Hook config merges into `~/.factory/settings.json` with paths rewritten.

</details>

<details>
<summary><b>Reasonix Support</b></summary>

Mirrors skills, scripts, and the allowlisted hooks (`scripts/reasonix-hooks-allowlist.txt`) into `~/.reasonix/` (no agent or custom-command surface, so neither is installed; the `/do` router rides in as a skill). Reasonix fires only 4 events (PreToolUse, PostToolUse, UserPromptSubmit, Stop), so only hooks for those events are allowlisted. Hook config is written to the `hooks` key of `~/.reasonix/settings.json` in Reasonix's native flat shape (one entry per hook, `match` regex over the tool name); the generator builds absolute `python3` commands, so no path rewrite is applied. MCP/model/permissions in `~/.reasonix/config.json` are user-owned an
