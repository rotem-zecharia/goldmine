# ykdojo/claude-code-tips

45+ tips for getting the most out of Claude Code, from basics to advanced - includes a custom status line script and Claude Code running itself in a container. Also includes the dx plugin: skills for 

## tools

There are a bunch of built-in slash commands (type `/` to see them all). Here are a few worth knowing:

## configuration

Isolated environments are great for `--dangerously-skip-permissions` sessions where you don't have to give permission for each little thing. You can just let it run on its own for a while. This is useful for research or experimentation, things that take a long time and maybe could be risky.

There are two major ways of going about it:

1. You can run it in a container. I even created [a preset environment](https://github.com/ykdojo/safeclaw) to make running containerized Claude Code sessions easy.
2. You can take it a step further by [setting up a whole machine Claude Code can fully control](https://github.com/ykdojo/claude-controls-mac), computer use included.

There's also auto mode, which is a sensible default in general - Claude runs autonomously while a classifier reviews each command and only stops for risky ones. But this still doesn't remove the risks and the need for approval entirely, so for tasks where you want it to have complete independence, you can still use a container.

## installation

This repo is also a Claude Code plugin called `dx` (developer experience). It bundles several tools from the tips above into a single install:

| Skill | Description |
|-------|-------------|
| `/dx:gha <url>` | Analyze GitHub Actions failures (Tip 27) |
| `/dx:handoff` | Create handoff documents for context continuity (Tip 8) |
| `/dx:half-clone` | Half-clone to reduce context (Tip 21) |
| `/dx:quarter-clone` | Quarter-clone to reduce context even more (Tip 21) |
| `/dx:reddit-fetch` | Fetch Reddit content via Reddit's JSON API |
| `/dx:review-claudemd` | Review conversations to improve CLAUDE.md files (Tip 28) |
| `/dx:hn-summarize` | Summarize Hacker News top stories, articles, and comment threads |
| `/dx:version-check` | Recommend which Claude Code version to run, or whether to update |
| `/dx:private-github-search` | Full-text search across all your GitHub repos, including private ones |

**Install with two commands:**

```bash
claude plugin marketplace add ykdojo/claude-code-tips
claude plugin install dx@ykdojo
```

After installing, the commands are available as `/dx:half-clone`, `/dx:handoff`, and `/dx:gha`. The `reddit-fetch` skill is invoked automatically when you ask about Reddit URLs. The `review-claudemd` skill analyzes your recent conversations and suggests improvements for your CLAUDE.md files. For the half-clone command, see the [recommended permission](#recommended-permission-for-the-half-clone-script).

**Recommended companion:** [Playwright MCP](https://github.com/microsoft/playwright-mcp) for browser automation - add with `claude mcp add -s user playwright npx @playwright/mcp@latest`
