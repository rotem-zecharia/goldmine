# luongnv89/claude-howto

A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

## features

The real power is in combining features. Learn to wire slash commands + memory + subagents + hooks into automated pipelines that handle code reviews, deployments, and documentation generation.

### 4. Test your understanding

Run `/lesson-quiz [topic]` after each module. The quiz pinpoints what you missed so you can fill gaps fast.

**[Get Started in 15 Minutes](#get-started-in-15-minutes)**

---

## Trusted by Developers

- **GitHub stars** from developers who use Claude Code daily
- **Forks** from teams adapting this guide for their own workflows
- **Actively maintained** — synced with every Claude Code release (latest: v2.1.235, August 2026)
- **Community-driven** — contributions from developers who share their real-world configurations

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## Not Sure Where to Start?

Take the self-assessment or pick your level:

| Level | You can... | Start here | Time |
|-------|-----------|------------|------|
| **Beginner** | Start Claude Code and chat | [Slash Commands](01-slash-commands/) | ~2.5 hours |
| **Intermediate** | Use CLAUDE.md and custom commands | [Skills](03-skills/) | ~3.5 hours |
| **Advanced** | Configure MCP servers and hooks | [Advanced Features](09-advanced-features/) | ~5 hours |

**Full learning path with all 10 modules:**

| Order | Module | Level | Time |
|-------|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/) | Beginner | 30 min |
| 2 | [Memory](02-memory/) | Beginner+ | 45 min |
| 3 | [Checkpoints](08-checkpoints/) | Intermediate | 45 min |
| 4 | [CLI Basics](10-cli/) | Beginner+ | 30 min |
| 5 | [Skills](03-skills/) | Intermediate | 1 hour |
| 6 | [Hooks](06-hooks/) | Intermediate | 1 hour |
| 7 | [MCP](05-mcp/) | Intermediate+ | 1 hour |
| 8 | [Subagents](04-subagents/) | Intermediate+ | 1.5 hours |
| 9 | [Advanced Features](09-advanced-features/) | Advanced | 2-3 hours |
| 10 | [Plugins](07-plugins/) | Advanced | 2 hours |

**[Complete Learning Roadmap ->](LEARNING-ROADMAP.md)**

---

## Get Started in 15 Minutes

> **Installation note**: Starting in v2.1.113, Claude Code ships as a native per-platform binary (macOS/Linux/Windows). `npm install -g @anthropic-ai/claude-code` still works — the native binary is downloaded as an optional dep on first use. As of v2.1.116, downloads come from `https://downloads.claude.ai/claude-code-releases` — corporate proxies must allowlist this host.

```bash
# 1. Clone the guide
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. Copy your first slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Try it — in Claude Code, type:
# /optimize

# 4. Ready for more? Set up project memory:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

## installation

cp -r 03-skills/code-review-specialist ~/.claude/skills/
```

Want the full setup? Here's the **1-hour essential setup**:

```bash

## tools

cp 01-slash-commands/*.md .claude/commands/

# Project memory (15 min)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

## configuration

# See 08-checkpoints/README.md
