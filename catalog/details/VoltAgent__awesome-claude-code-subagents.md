# VoltAgent/awesome-claude-code-subagents

A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases

## installation

1. Clone this repository
2. Copy desired agent files to:
   - `~/.claude/agents/` for global access
   - `.claude/agents/` for project-specific use
3. Customize based on your project requirements

## tools

Claude Code skill for browsing and fetching subagents from this catalog.

| Command | Description |
|---------|-------------|
| `/subagent-catalog:search <query>` | Find agents by name, description, or category |
| `/subagent-catalog:fetch <name>` | Get full agent definition |
| `/subagent-catalog:list` | Browse all categories |
| `/subagent-catalog:invalidate` | Refresh cache |

**Installation:**
```bash
cp -r tools/subagent-catalog ~/.claude/commands/
```
