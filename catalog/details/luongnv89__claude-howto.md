# luongnv89/claude-howto

A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

## features

The real power is in combining features. Learn to wire slash commands + memory + subagents + hooks into automated pipelines that handle code reviews, deployments, and documentation generation.

## installation

cp -r 03-skills/code-review-specialist ~/.claude/skills/
```

Want the full setup? Here's the **1-hour essential setup**:

```bash

## tools

cp 01-slash-commands/*.md .claude/commands/

## configuration

export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."
