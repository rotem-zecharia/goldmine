# nyldn/claude-octopus

Run multiple AI models against the same research, design, or coding task. Surface disagreements before you ship.

## installation

```bash
# Terminal (not inside a Claude Code session):
claude plugin marketplace add https://github.com/nyldn/plugins.git
claude plugin install octo@nyldn-plugins

# Then inside Claude Code:
/octo:setup
```

That's it. Setup detects installed providers, shows what's missing, and walks you through configuration. You need **zero** external providers to start — Claude is built in.

### Dormant by default

Installing Octopus does not route ordinary prompts, launch provider workflows,
or delegate to Octopus agents. Every shipped command and skill uses Claude
Code's native manual-invocation gate. Start it with `/octo:*`.

> **Seeing `cannot be used with Skill tool due to disable-model-invocation`?**
> That is the gate working as intended — the model tried to auto-invoke an
> Octopus skill. Invoke it explicitly instead: type `/octo:skill-doctor` (the
> manually invokable skill), not a model call to the `skill-doctor` skill. Slash skills are
> user-invoked, so they bypass this invocation gate; the model will not call
> Octopus skills on its own unless you opt into the router below. Rule of thumb:
> **invoke Octopus with
> `/octo:…`, don't expect Claude to reach for it for you.**

Optional automation remains available, but it is explicit opt-in:

```bash
export OCTOPUS_AUTO_ROUTER_MODE=suggest  # suggest a route for plain prompts
# or: OCTOPUS_AUTO_ROUTER_MODE=invoke    # load the matched command route
export OCTO_DONE_CRITERIA=on             # compound-task completion coaching
export OCTOPUS_COMPRESS_ENABLED=true     # PostToolUse output compression
export OCTO_STRATEGY_ROTATION=on         # failure strategy rotation
export OCTOPUS_CONTEXT_AWARENESS=on      # statusline-to-context reinforcement
export OCTOPUS_SESSION_MEMORY=on         # SessionStart preference restoration
```

This legacy opt-in examines ordinary prompts. `invoke` can start paid
external-provider workflows and share the routed prompt context with configured
providers; prefer `suggest` unless that behavior is intentional. Provider-side
retention follows each provider account's policy. Unset the variable (or set it
to `off`) to opt out without disabling direct `/octo:*` commands.

Safety guards that prevent invalid direct Codex, Qwen, or retired Gemini CLI
dispatch remain available, but host-side command filters keep them out of
unrelated tool calls.

Claude Code **v2.1.14+** is the minimum supported runtime. Newer Claude Code releases unlock additional Octopus diagnostics and release checks automatically; the current plugin tracks 183 Claude Code capability flags through **Claude Code v2.1.219**.

<details>
<summary>Install for Codex CLI</summary>

```bash
codex plugin marketplace add https://github.com/nyldn/plugins.git
codex plugin add claude-octopus@nyldn-plugins
```

Restart Codex. Skills appear automatically — invoke with `$skill-doctor`, `$skill-debug`, etc.

Codex owns the versioned cache. To refresh an existing installation without
editing cache files or symlinks directly, exit Codex and run these commands in
a separate terminal:

```bash
codex plugin marketplace upgrade nyldn-plugins
codex plugin add claude-octopus@nyldn-plugins
```

Restart Codex after the update. Replacing the cache from the session that is
using it can leave hooks and skills bound to a removed version directory.

</details>

<details>
<summary>Install for Cursor IDE</summary>

Cursor uses Octopus as an **MCP server** (not a plugin — Cursor doesn't have Claude Code's plugin system). You get MCP tools like `octopus_discover`, `octopus_review`, etc. instead of `/octo:*` slash commands.

> **Important:** Just cloning the repo is not enough. You must complete all three steps below — install dependencies and configure the MCP server — for Cursor to pick up Octopus tools.

```bash
# 1. Clone the repo
git clone --depth 1 https://github.com/nyldn/claude-octopus.git ~/.cursor/claude-octopus

# 2. Install MCP server dependencies
cd ~/.cursor/claude-octopus/mcp-server && npm install

## configuration

```

```json
{
  "mcpServers": {
    "claude-octopus": {
      "command": "npx",
      "args": ["tsx", "${userHome}/.cursor/claude-octopus/mcp-server/src/index.ts"],
      "env": {
        "OCTO_CLAW_ENABLED": "true",
        "OPENAI_API_KEY": "${env:OPENAI_API_KEY}"
      }
    }
  }
}
```

Restart Cursor. Tools appear in Cursor's AI chat — invoke by asking e.g. "use octopus_discover to research X".

<details>
<summary>Using Cursor on WSL?</summary>

If you're running Cursor on Windows with WSL, clone the repo inside WSL and point the MCP config through `wsl.exe`:

```json
{
  "mcpServers": {
    "claude-octopus": {
      "command": "wsl",
      "args": ["npx", "tsx", "/home/<user>/.cursor/claude-octopus/mcp-server/src/index.ts"],
      "env": {
        "OPENAI_API_KEY": "${env:OPENAI_API_KEY}"
      }
    }
  }
}
```

Replace `<user>` with your WSL username. Make sure `node` and `npm` are installed inside WSL.
</details>

See [docs/IDE-INTEGRATION.md](docs/IDE-INTEGRATION.md) for the full guide including `ide-attach.sh` auto-setup.
</details>

<details>
<summary>Install for OpenCode</summary>

```bash
git clone --depth 1 https://github.com/nyldn/claude-octopus.git ~/.opencode/claude-octopus
mkdir -p ~/.agents/skills
ln -s ~/.opencode/claude-octopus/skills ~/.agents/skills/claude-octopus
```
</details>

<details>
<summary>Other install methods (Claude Code)</summary>

**From the Claude Code UI:** Type `/plugin` in a session → **Marketplace** tab → install **octo**.

**Factory AI (Droid):**
```bash
droid plugin marketplace add https://github.com/nyldn/claude-octopus.git
droid plugin install octo@nyldn-plugins
```
</details>

<details>
<summary>Update / Troubleshooting</summary>

[Claude Code leaves auto-update off by default for third-party marketplaces](https://code.claude.com/docs/en/discover-plugins#configure-auto-updates).
To opt in to host-managed startup updates, run `/plugin`, open
**Marketplaces**, select **nyldn-plugins**, and choose **Enable auto-update**.
When Claude reports that Octopus was updated, run `/reload-plugins` (or restart
Claude Code) before using the new version.

```bash
# Manual update
claude plugin marketplace update nyldn-plugins
claude plugin update octo@nyldn-plugins

## tools

~/.claude-octopus/plugin/scripts/orchestrate.sh update-plugin
