# ykdojo/claude-code-tips

45+ tips for getting the most out of Claude Code, from basics to advanced - includes a custom status line script and Claude Code running itself in a container. Also includes the dx plugin: skills for 

## tools

There are a bunch of built-in slash commands (type `/` to see them all). Here are a few worth knowing:

### /usage

Check your rate limits:

```
 Current session
 █████████▌                                         19% used
 Resets 12:59am (America/Vancouver)

 Current week (all models)
 █████████████████████▌                             43% used
 Resets Feb 3 at 1:59pm (America/Vancouver)

 Current week (Sonnet only)
 ███████████████████▌                               39% used
 Resets 8:59am (America/Vancouver)
```

If you want to watch your usage closely, keep it open in a tab and use Tab then Shift+Tab or ← then → to refresh.

### /chrome

Toggle Claude's native browser integration:

```
> /chrome
Chrome integration enabled
```

### /mcp

Manage MCP (Model Context Protocol) servers:

```
 Manage MCP servers
 1 server

 ❯ 1. playwright  ✔ connected · Enter to view details

 MCP Config locations (by scope):
  • User config (available in all your projects):
    • /Users/yk/.claude.json
```

### /stats

View your usage statistics with a GitHub-style activity graph:

```
      Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan
      ··········································▒█░▓░█░▓▒▒
  Mon ·········································▒▒██▓░█▓█░█
      ·········································░▒█▒▓░█▒█▒█
  Wed ········································░▓▒█▓▓░▒▓▒██
      ········································░▓░█▓▓▓▓█░▒█
  Fri ········································▒░░▓▒▒█▓▓▓█
      ········································▒▒░▓░░▓▒▒░░

      Less ░ ▒ ▓ █ More

  Favorite model: Opus 4.5        Total tokens: 17.6m

  Sessions: 4.1k                  Longest session: 20h 40m 45s
  Active days: 79/80              Longest streak: 75 days
  Most active day: Jan 26         Current streak: 74 days

  You've used ~24x more tokens than War and Peace
```

### /clear

Clear the conversation and start fresh.

## Tip 2: Talk to Claude Code with your voice

I found that you can communicate much faster with your voice than typing with your hands. Using a voice transcription system on your local machine is really helpful for this.

On my Mac, I've tried a few different options:
- [superwhisper](https://superwhisper.com/)
- [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper)
- [Super Voice Assistant](https://github.com/ykdojo/super-voice-assistant) (open source, supports Parakeet v2/v3)

You can get more accuracy by using a hosted service, but I found that a local model is strong enough for this purpose. Even when there are mistakes or typos in the transcription, Claude is smart enough to understand what you're trying to say. Sometimes you need to say certain things extra clearly, but overall local models work well enough.

For example, in this screenshot you can see that Claude was able to interpret mistranscribed words like "ExcelElanishMark" and "advast" correctly as "exclamation mark" and "Advanced":

![Voice transcription mistakes interpreted correctly](assets/voice-transcription-mistakes.png)

I think the best way to think about this is like you're trying to communicate with your friend. Of course, you can communicate through texts. That might be easier for some people, or emails, right? That's totally fine. That's what most people seem to do with Claude Code. But if you want to communicate faster, why wouldn't you get on a quick phone call? You can just send voice messages. You don't need to literally have a phone call with Claude Code. Just send a bunch of voice messages. It's faster, at least for me, as someone who's practiced the art of speaking a lot over the past number of years. But I think for a majority of people, it's going to be faster too.

A common objection is "what if you're in a room with other people?" I just whisper using earphones - I personally like Apple EarPods (not AirPods). They're affordable, high quality enough, and you just whisper into them quietly. I've done it in front of other people and it works well. In offices

## configuration

Isolated environments are great for `--dangerously-skip-permissions` sessions where you don't have to give permission for each little thing. You can just let it run on its own for a while. This is useful for research or experimentation, things that take a long time and maybe could be risky.

There are two major ways of going about it:

1. You can run it in a container. I even created [a preset environment](https://github.com/ykdojo/safeclaw) to make running containerized Claude Code sessions easy.
2. You can take it a step further by [setting up a whole machine Claude Code can fully control](https://github.com/ykdojo/claude-controls-mac), computer use included.

There's also auto mode, which is a sensible default in general - Claude runs autonomously while a classifier reviews each command and only stops for risky ones. But this still doesn't remove the risks and the need for approval entirely, so for tasks where you want it to have complete independence, you can still use a container.

### Advanced: Orchestrating a worker Claude Code in a container

You can take this further by having your local Claude Code control another Claude Code instance running inside a container. The trick is using tmux as the control layer:

1. Your local Claude Code starts a tmux session
2. In that tmux session, it runs or connects to the container
3. Inside the container, Claude Code runs with `--dangerously-skip-permissions`
4. Your outer Claude Code uses `tmux send-keys` to send prompts and `capture-pane` to read output

This gives you a fully autonomous "worker" Claude Code that can run experimental or long-running tasks without you approving every action. When it's done, your local Claude Code can pull the results back. If something goes wrong, it's all sandboxed in the container.

### Advanced: Multi-model orchestration

Beyond just Claude Code, you can run different AI CLIs in containers - Codex, Antigravity CLI, or others. I tried OpenAI Codex for code review, and it works well. The point isn't that you can't run these CLIs directly on your host machine - you obviously can. The value is that Claude Code's UI/UX is smooth enough that you can just talk to it and let it handle the orchestration: spinning up different models, sending data between containers and your host. Instead of manually switching between terminals and copy-pasting, Claude Code becomes the central interface that coordinates everything.

## Tip 20: The best way to get better at using Claude Code is by using it

Recently I saw a world-class rock climber being interviewed by another rock climber. She was asked, "How do you get better at rock climbing?" She simply said, "By rock climbing."

That's how I feel about this too. Of course, there are supplementary things you can do, like watching videos, reading books, learning about tips. But using Claude Code is the best way to learn how to use it. Using AI in general is the best way to learn how to use AI.

I like to think of it like a billion token rule instead of the 10,000 hour rule. If you want to get better at AI and truly get a good intuition about how it works, the best way is to consume a lot of tokens. And nowadays it's possible. I found that especially with Opus 4.5, it's powerful enough but affordable enough that you can run multiple sessions at the same time. You don't have to worry as much about token usage, which frees you up a lot.

## Tip 21: Fork and half-clone conversations

Sometimes you want to try a different approach from a specific point in a conversation without losing your original thread. Claude Code has native forking:
- `/branch` - branches the current session from within a conversation
- `--fork-session` - use with `--resume` or `--continue` (e.g., `claude -c --fork-session`)

Since `--fork-session` has no short form, you can add this function to your `~/.zshrc` or `~/.bashrc` to use `--fs` as a shortcut:

```bash
claude() {
  local args=()
  for arg in "$@"; do
    if [[ "$arg" == "--fs" ]]; then
     

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

## Tip 45: Quick setup script

If you want to set up multiple recommendations from this repo at once, there's a setup script that handles many of them:

```bash
bash <(curl -s https://raw.githubusercontent.com/ykdojo/claude-code-tips/main/scripts/setup.sh)
```

The script shows you everything it will configure and lets you skip any items:

```
INSTALLS:
  1. DX plugin - skills like /dx:gha, /dx:handoff, and reddit-fetch

SETTINGS (~/.claude/settings.json):
  2. Status line - shows model, git branch, uncommitted files, token usage at bottom of screen
  3. Disable auto-updates - prevents Claude Code from auto-updating
  4. Lazy-load MCP tools - only loads MCP tool definitions when needed, saves context
  5. Read(~/.claude) permission - allows the half-clone command to read conversation history
  6. Read(//tmp/**) permission - allows reading temporary files without prompts
  7. Disable attribution - removes Co-Authored-By from commits and attribution from PRs

SHELL CONFIG (~/.zshrc or ~/.bashrc):
  8. Aliases: c=claude, ch=claude --chrome, cs=claude --dangerously-skip-permissions
  9. Fork shortcut: --fs expands to --fork-session (e.g., claude -c --fs)

Skip any? [e.g., 1 4 7 or Enter for all]:
```

## Tip 46: Switch between multiple Claude accounts

If you have multiple Claude accounts (for example, personal vs work), here's how you can switch between them quickly.

On macOS your login lives in a single Keychain entry, but the `CLAUDE_CODE_OAUTH_TOKEN` env var overrides it, so you can launch as a specific account. The env var works on Linux and Windows too (their logins live in `~/.claude/.credentials.json` instead). Here's an example of how you can set this up on Mac - feel free to adapt it to your own system.

Mint a one-year token per account (`claude setup-token` opens a browser - log into the account you want), then store each in the Keychain so it's not plaintext in your dotfiles:

```bash
claude setup-token   # log in as each account, copy the token
security add-generic-password -s "claude-token-work"     -a "$USER" -U -w
security add-generic-password -s "claude-token-personal" -a "$USER" -U -w
```

Add two functions to your `~/.zshrc` that look up the token and pass any args through to `claude`:

```bash
clw() { CLAUDE_CODE_OAUTH_TOKEN="$(security find-generic-password -s claude-token-work     -a "$USER" -w)" claude "$
