# jarrodwatts/claude-hud

A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

## installation

Inside Claude Code, run:

```
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/reload-plugins
/claude-hud:setup
```

`/claude-hud:setup` points your status line at the HUD. Claude Code reloads settings on its own, so the HUD appears right away. To customize it, ask Claude or run `/claude-hud:configure`.

<details>
<summary><strong>Prefer the terminal?</strong></summary>

```bash
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud@claude-hud
```

Then run `/reload-plugins` and `/claude-hud:setup` inside a session.

</details>

<details>
<summary><strong>Windows: setup says no JavaScript runtime was found</strong></summary>

Install Node.js LTS (`winget install OpenJS.NodeJS.LTS`), restart your shell, and run `/claude-hud:setup` again.

</details>

## What You See

The default is two lines:

```
[Opus] │ my-project git:(main*)
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (resets in 1h 30m)
```

- **Line 1**: model, a provider label when one is detected (`Bedrock`, `Vertex`, `MiniMax`), project path, and git branch.
- **Line 2**: context used (green, then yellow, then red as it fills) and your subscriber rate limits.

Optional lines, which you turn on with `/claude-hud:configure`:

```
◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2        ← tools
◐ explore [haiku]: Finding auth code (2m 15s)    ← agents
▸ Fix authentication bug (2/5)                   ← todos
```

## How It Works

Claude HUD is a [status line](https://code.claude.com/docs/en/statusline) command. Claude Code runs it with session data on stdin (model, context window, cost, rate limits, prompt cache) and shows what it prints. Some optional elements, such as the tools, agents, and todos lines, also read the session transcript. It needs no separate window or tmux and works in any terminal.

## configuration

```
/claude-hud:configure
```

The guided flow covers layout, activity lines, session info, usage, git, language, and a custom line. It previews the changes before saving and keeps every setting it doesn't ask about.

Everything else lives in `~/.claude/plugins/claude-hud/config.json` (or under `$CLAUDE_CONFIG_DIR`). Invalid values fall back to their defaults.

If several `CLAUDE_CONFIG_DIR`s share one `plugins/` directory, put per-directory settings in `$CLAUDE_CONFIG_DIR/claude-hud.json`. It uses the same shape, only needs the keys it changes, and is layered on top of the shared config:

```json
{ "display": { "customLine": "Work Team" } }
```

Labels are available in English (the default), Simplified Chinese (`zh-Hans`, alias `zh`), and Traditional Chinese (`zh-Hant`, alias `zh-TW`).

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `language` | `en` \| `zh` \| `zh-Hans` \| `zh-Hant` \| `zh-TW` | `en` | HUD label language. Use `zh` or `zh-Hans` for Simplified Chinese and `zh-Hant` or `zh-TW` for Traditional Chinese. |
| `lineLayout` | string | `expanded` | Layout: `expanded` (multi-line) or `compact` (single line) |
| `showSeparators` | boolean | false | In `compact` layout, draw a rule between the session line and the activity lines |
| `pathLevels` | 1-3 \| `full` | 1 | Directory levels to show in project path, or `full` to show the entire absolute path |
| `maxWidth` | number \| `null` | `null` | Optional fallback width used only when terminal width detection fails completely |
| `forceMaxWidth` | boolean | false | Always use `maxWidth` when it is set, even if terminal width detection returns a smaller value |
| `elementOrder` | string[] | `["project","addedDirs","context","usage","promptCache","memory","environment","tools","skills","mcp","agents","todos","sessionTime"]` | Expanded-mode element order. Omit entries to hide them in expanded mode. Existing configs keep their explicit order until updated. |
| `projectLineOrder` | string[] | `[]` | Optional leading order of segments *within* the first line, in both layouts. Visibility stays with the `display.show*` flags, and omitted segments retain their existing renderer order. `model` covers provider + model + effort (plus the context bar in compact mode); `project` covers path + added dirs + git as one segment. Example: `["project","model"]` puts the project/git block before the model badge. |
| `display.mergeGroups` | string[][] | `[["context","usage"]]` | Expanded-mode groups that should share a line when adjacent. Set `[]` to disable merged lines. |
| `display.rightAlign` | string[] | `[]` | Starts a right-aligned suffix at the first listed element in a merged row, preserving `elementOrder` and padding the gap with spaces. Requires the anchor to be in a `display.mergeGroups` group that actually renders on one line. Ignored when the terminal width is unknown, the anchor is first, or there is no room for padding. Example: `["context"]` with a `["project","context","usage"]` group keeps project/git left and pins context + usage right. |
| `gitStatus.enabled` | boolean | true | Show git branch in HUD |
| `gitStatus.showDirty` | boolean | true | Show `*` for uncommitted changes |
| `gitStatus.showAheadBehind` | boolean | false | Show `↑N ↓N` for ahead/behind remote |
| `gitStatus.pushWarningThreshold` | number | 0 | Color the ahead count with the warning color at or above this unpushed-commit count (`0` disables it) |
| `gitStatus.pushCriticalThreshold` | number | 0 | Color the ahead count with the critical color at or above this unpushed-commit count (`0` disables it) |
| `gitStatus.showFileStats` | boolean | false | Show file change counts `!M +A ✘D ?U` |
| `gitStatus.showWorktree` | boolean | false | In a linked git worktree, show its name after the branch, e.g. `git:(feat/x) ⎇ feat-x` |
| `gitStatus.branchOverflow` | `truncate` \| `wrap` | `truncate` | Keep current truncation behavior or let the git block wrap onto its 

## tools

Usage shows whenever Claude Code sends subscriber `rate_limits`, which is after the first response of a session. API-key, Bedrock, and Vertex sessions have no subscriber limits, so it stays hidden. The 7-day window appears once it passes `display.sevenDayThreshold`:

```
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (resets in 1h 30m) | Weekly █████████░ 85% (resets in 1d)
```

With `display.usagePace`, a window you're using faster than it refills turns amber (on track to end at 90% or more) or red (on track to run out first) and gets a `▲`. Windows under 10% used stay neutral.

**External snapshot.** `display.externalUsagePath` reads a local JSON file. Its windows fill in when stdin has none, and its `balance_label` or `model_scoped` windows (for example a per-model weekly quota) add to stdin's. The file must be absolute and fresher than `display.externalUsageFreshnessMs`:

```json
{
  "updated_at": "2026-04-20T12:00:00.000Z",
  "five_hour": { "used_percentage": 42, "resets_at": "2026-04-20T15:00:00.000Z" },
  "seven_day": { "used_percentage": 84, "resets_at": "2026-04-27T12:00:00.000Z" },
  "balance_label": "$12.50",
  "model_scoped": [{ "display_name": "Fable", "utilization": 89, "resets_at": "2026-04-27T11:00:00Z" }]
}
```

`display.externalUsageWritePath` does the reverse: it writes stdin's rate limits to a private `.json` file in an existing directory for other tools to read.

### Cost

`display.showCost` shows Claude Code's own session cost, computed at list price or from your `modelPricing` table. Bedrock and Vertex bill through the cloud provider, so their cost is hidden unless `display.showRoutedCost` is also set.

`display.showDailyCost` adds today's spend across sessions (`Today $12.34`). It is kept in a small ledger in the plugin data directory, resets at local midnight, and counts a session from the first render that sees it. `display.showWeeklyCost` uses the same ledger from the start of the 7-day quota window, so it needs a subscriber session.

### Prompt Cache

`display.showPromptCache` shows when the main conversation's prompt cache goes cold, such as `Cache ⏱ until 14:30`, or `expired`. It shows a clock time rather than a countdown because the status line doesn't repaint between turns, which is exactly when the cache drains; a clock time stays correct however old the render is. `display.showCacheHitRate` shows the share of input tokens read from the cache.

### Jujutsu (jj)

Set `jjStatus.enabled` to `true` to show jj status, such as `jj:(mybookmark*)` or `jj:(wrulwzyw !conflict)`, instead of git in a directory with a `.jj` repository. The HUD runs jj read-only without snapshotting the working copy, so the dirty marker reflects jj's last snapshot. Ahead/behind and file stats are git-only.

### Example

```json
{
  "lineLayout": "expanded",
  "pathLevels": 2,
  "gitStatus": { "showAheadBehind": true, "showFileStats": true },
  "display": {
    "showTools": true,
    "showAgents": true,
    "showTodos": true,
    "showDuration": true,
    "showCost": true
  },
  "colors": { "context": "cyan", "custom": "#FF6600" }
}
```

### Auto-Refresh

Claude Code re-runs the status line after each message, `/compact`, a permission or vim mode change, a rate-limit reset, and a prompt-cache expiry. To keep countdowns and durations ticking while a session is idle, add `refreshInterval` (seconds) to the `statusLine` entry in `~/.claude/settings.json`.

### Turning It Off for a Session

```bash
CLAUDE_HUD_DISABLE=1 claude
```

Any value other than `0`, `false`, `off`, or `no` blanks the HUD for that session without touching `settings.json`.

## Security

Claude HUD is local-only. It makes no network requests, never reads credentials, and calls no undocumented APIs. It reads Claude Code's stdin, the session transcript, Claude configuration files, and git or jj metadata for the current directory. Its only writes are small state files (output speed and the cost ledger) under `~/.claude/plugins/claude-hud`, with private permissions

## requirements

- Claude Code v2.1.260 or later
- macOS or Linux: Node.js 18+ or Bun
- Windows: Node.js 18+

## Development

```bash
git clone https://github.com/jarrodwatts/claude-hud
cd claude-hud
npm ci && npm test
```

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jarrodwatts/claude-hud&type=Date)](https://star-history.com/#jarrodwatts/claude-hud&Date)
