# Gitlawb/openclaude

runs anywhere. uses anything

## features

- One CLI across cloud APIs and local model backends — no per-provider tooling
- Guided provider setup and saved profiles with `/provider`
- Coding-agent workflows in one place: bash, file tools, grep, glob, agents, tasks, MCP, and web tools
- A bundled VS Code extension for launch integration and theme support
- A pixel-art hero companion who fires an arrow every time you press Enter (really — see [Meet your buddy](#meet-your-buddy))

## installation

OpenClaude requires Node.js `>=22.0.0` for npm installs and runtime. Bun is
only needed for source builds and local development.

```bash
npm install -g @gitlawb/openclaude@latest
```

If you're on Arch Linux, you can install OpenClaude from the community-maintained [AUR package](https://aur.archlinux.org/packages/openclaude):
```bash
paru -S openclaude
```

If the install later reports `ripgrep not found`, install ripgrep system-wide and confirm `rg --version` works in the same terminal before starting OpenClaude.

**Verify / troubleshoot installed version:**

```bash
openclaude --version
npm view @gitlawb/openclaude dist-tags
npm install -g @gitlawb/openclaude@latest
```

## configuration

OpenClaude stores its own config under `~/.openclaude` and `~/.openclaude.json`
by default. It does not read `~/.claude`, project `.claude/` directories, or
`CLAUDE_CONFIG_DIR`; new users can start with an empty OpenClaude config and do
not need Claude Code installed.

If you previously used OpenClaude with `.claude` paths, migrate intentionally:
copy only the settings, commands, agents, skills, scheduled tasks, or other files
you personally created for OpenClaude into the matching `.openclaude` location.
Do not blanket-copy `.claude`, and do not copy Claude Code credentials or auth
files. For provider authentication, prefer running OpenClaude's provider setup
again or exporting provider-specific environment variables.
