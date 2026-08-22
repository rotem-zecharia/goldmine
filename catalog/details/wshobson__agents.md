# wshobson/agents

Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Google Antigravity

## installation

Pick your harness:

### Claude Code

```bash
/plugin marketplace add wshobson/agents
/plugin install python-development          # or any of 92 plugins
```

[→ Full Claude Code setup, troubleshooting, and plugin catalog](docs/usage.md)

### Codex CLI · Cursor · OpenCode · Antigravity CLI · Copilot

Codex and Cursor install natively from the committed registries (which point at the source `plugins/`):

```bash
npx codex-marketplace add wshobson/agents        # Codex; then install individual plugins
# Cursor: add the marketplace, then `/plugin install <name>` (reads .cursor-plugin/ + source)
```

Antigravity and OpenCode install via clone + generate (the transformed trees are gitignored):

```bash
gh repo clone wshobson/agents ~/agents && cd ~/agents
make generate HARNESS=antigravity && make install-antigravity  # Antigravity (agy)
make install-opencode                                          # OpenCode (runs generate + symlinks)
```

Setup details and per-harness gotchas: [docs/harnesses.md](docs/harnesses.md).

## What's inside

| | Count | What it is |
|---|---:|---|
| **Plugins** | 92 | Granular, single-purpose installable units (91 local + 1 external via git-subdir) |
| **Agents** | 202 | Domain experts (architecture, languages, infra, security, data, ML, docs, business, SEO) |
| **Skills** | 181 | Modular knowledge packages with progressive disclosure (load when activated) |
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

This marketplace ships to five agentic harnesses from one Markdown source. Each adapter
emits harness-native artifacts (not lowest-common-denominator translations):

| Harness | Generates | Notes |
|---|---|---|
| **Claude Code** | (source-of-truth) | Native `marketplace.json` + `plugins/` |
| **Codex CLI** | `.agents/plugins/marketplace.json` + `plugins/*/.codex-plugin/plugin.json` (committed); `.codex/skills/`, `.codex/agents/` (gitignored) | 8 KB skill cap respected; commands → skills |
| **Cursor** | `.cursor-plugin/`, `.cursor/rules/` | Thin marketplace + curated rules; reuses `.claude/` |
| **OpenCode** | `.opencode/agents/`, `.opencode/commands/`, `.opencode/skills/` | `permission:` block from `tools:` allowlist; OpenCode-safe skill names |
| **Antigravity CLI** | `.antigravity/plugins/<p>/{skills/,agents/,commands/}` | Self-contained agy plugin per source plugin; model tier alias (`inherit`/`flash`/`pro`) |
| **Copilot** | `.copilot/agents/`, `.copilot/skills/`, `.copilot/commands/` | Markdown agent profiles + SKILL.md skills + commands-as-skills; model maps to native Claude models |

```bash
make generate-all                        # all five
make validate                      
