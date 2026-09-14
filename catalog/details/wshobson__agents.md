# wshobson/agents

Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi

## installation

Pick your harness:

### Claude Code

```bash
/plugin marketplace add wshobson/agents
/plugin install python-development          # or any of 94 plugins
```

[→ Full Claude Code setup, troubleshooting, and plugin catalog](docs/usage.md)

### Codex CLI · Cursor · OpenCode · Antigravity CLI · Copilot · Pi

Codex and Cursor install natively from the committed registries (which point at the source `plugins/`):

```bash
npx codex-marketplace add wshobson/agents        # Codex; then install individual plugins
# Cursor: add the marketplace, then `/plugin install <name>` (reads .cursor-plugin/ + source)
```

Antigravity, OpenCode, and Pi install via clone + generate (the transformed trees are gitignored):

```bash
gh repo clone wshobson/agents ~/agents && cd ~/agents
make generate HARNESS=antigravity && make install-antigravity  # Antigravity (agy)
make install-opencode                                          # OpenCode (runs generate + symlinks)
make generate HARNESS=pi && make install-pi                    # Pi
```

### Skills only: `gh skill` · `npx skills`

Both Agent Skills installers read `plugins/*/skills/` straight from GitHub, into whichever agent you use. No clone, no marketplace, no generate step. Skills only: no agents, commands, or hooks.

```bash
gh skill install wshobson/agents                                 # browse, then pick a skill or --all
gh skill install wshobson/agents python-testing-patterns --agent claude-code
npx skills add wshobson/agents --skill python-testing-patterns   # add -a claude-code, -g for user scope
```

Setup details and per-harness gotchas: [docs/harnesses.md](docs/harnesses.md).

## What's inside

| | Count | What it is |
|---|---:|---|
| **Plugins** | 94 | Granular, single-purpose installable units (92 local + 2 external via git-subdir) |
| **Agents** | 202 | Domain experts (architecture, languages, infra, security, data, ML, docs, business, SEO) |
| **Skills** | 183 | Modular knowledge packages with progressive disclosure (load when activated) |
| **Commands** | 105 | Slash commands: scaffolding, security scans, test gen, infrastructure setup |
| **Orchestrators** | 16 | Multi-agent coordination workflows (full-stack, security, ML, incident response) |

Browse the catalog: [docs/plugins.md](docs/plugins.md) · [docs/agents.md](docs/agents.md) · [docs/agent-skills.md](docs/agent-skills.md)

## How it works

Each plugin is isolated and composable: agents, commands, and skills are auto-discovered
from directory structure. **Installing a plugin loads only its components into
context** — not the whole marketplace.

```
plugins/python-development/
├── .claude-plugin/plugin.json
├── agents/             # 3 Python agents (python-pro, django-pro, fastapi-pro)
├── commands/           # 1 scaffolding command
└── skills/             # 16 specialized skills (async, testing, packaging, …)
```

Tiered model strategy:

| Tier | Model | Use |
|---|---|---|
| 0 | Fable 5  | Longest-horizon autonomous work — large migrations, multi-hour runs (opt-in, premium cost) |
| 1 | Opus     | Architecture, security, code review, production-critical |
| 2 | inherit  | User-chosen — backend, frontend, AI/ML, specialized |
| 3 | Sonnet   | Docs, testing, debugging, API references |
| 4 | Haiku    | Fast operational tasks, SEO, deployment, content |

[→ Model configuration details](docs/agents.md#model-configuration)

## Multi-harness support

This marketplace ships to seven agentic harnesses from one Markdown source. Each adapter
emits harness-native artifacts (not lowest-common-denominator translations):

| Harness | Generates | Notes |
|---|---|---|
| **Claude Code** | (source-of-truth) | Native `marketplace.json` + `plugins/` |
| **Codex CLI** | `.agents/plugins/marketplace.json` + `plugins/*/.codex-plugin/plugin.json` (committed); `.codex/skills/`, `.codex/agents/` (gitignored) | 8 KB skill cap respected; commands → skills |
| **Cursor** | `.cursor-plugin/`, `.cursor/rules/` | Thin marketplace + curated rules; reuses `
