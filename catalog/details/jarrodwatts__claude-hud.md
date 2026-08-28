# jarrodwatts/claude-hud

A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

## installation

Inside a Claude Code instance, run the following commands:

**Step 1: Add the marketplace**
```
/plugin marketplace add jarrodwatts/claude-hud
```

**Step 2: Install the plugin**

<details>
<summary><strong>⚠️ Linux users: Click here if install fails with an EXDEV error</strong></summary>

On older Claude Code versions, `/tmp` being a separate filesystem (tmpfs) caused plugin installation to fail with:
```
EXDEV: cross-device link not permitted
```

This [Claude Code bug](https://github.com/anthropics/claude-code/issues/14799) has since been fixed — if you hit it, update Claude Code first. If you can't update, set TMPDIR before installing:
```bash
mkdir -p ~/.cache/tmp && TMPDIR=~/.cache/tmp claude
```

Then run the install command below in that session.

</details>

```
/plugin install claude-hud
```

After that, reload plugins (no restart needed):

```
/reload-plugins
```

<details>
<summary><strong>Prefer the terminal?</strong></summary>

Steps 1–2 can also be done outside a session with the Claude Code CLI:
```bash
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud@claude-hud
```
Then run `/reload-plugins` inside your session (or start a new one).

</details>

**Step 3: Configure the statusline**
```
/claude-hud:setup
```

<details>
<summary><strong>⚠️ Windows users: Click here if setup says no JavaScript runtime was found</strong></summary>

On Windows, Node.js LTS is the supported runtime for Claude HUD setup. If setup says no JavaScript runtime was found, install Node.js for your shell first:
```powershell
winget install OpenJS.NodeJS.LTS
```
Then restart your shell and run `/claude-hud:setup` again.

</details>

Done! Claude Code reloads settings automatically — the HUD appears after your next message, no restart needed. If it doesn't show up, restart Claude Code (older versions require a restart to pick up statusLine changes).

---

## What is Claude HUD?

Claude HUD gives you better insights into what's happening in your Claude Code session.

| What You See | Why It Matters |
|--------------|----------------|
| **Project path** | Know which project you're in (configurable 1-3 directory levels) |
| **Context health** | Know exactly how full your context window is before it's too late |
| **Tool activity** | Watch Claude read, edit, and search files as it happens |
| **Agent tracking** | See which subagents are running and what they're doing |
| **Todo progress** | Track task completion in real-time |

## What You See

### Default (2 lines)
```
[Opus] │ my-project git:(main*)
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h)
```
- **Line 1** — Model, provider label when positively identified (for example `Bedrock`, `Vertex`, `MiniMax`), project path, git branch
- **Line 2** — Context bar (green → yellow → red) and usage rate limits

## configuration

```
◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2        ← Tools activity
◐ explore [haiku]: Finding auth code (2m 15s)    ← Agent status
▸ Fix authentication bug (2/5)                   ← Todo progress
```

---

## How It Works

Claude HUD uses Claude Code's native **statusline API** — no separate window, no tmux required, works in any terminal.

```
Claude Code → stdin JSON → claude-hud → stdout → displayed in your terminal
           ↘ transcript JSONL (tools, agents, todos)
```

**Key features:**
- Native token data from Claude Code (not estimated)
- Scales with Claude Code's reported context window size, including newer 1M-context sessions
- Parses the transcript for tool/agent activity
- Re-renders after each interaction (new assistant messages, `/compact`, permission changes, vim-mode toggles), debounced at 300ms

---

## Configuration

Customize your HUD anytime:

```
/claude-hud:configure
```

The guided flow handles layout, language, and common display toggles. Advanced overrides such as
custom colors and thresholds are preserved there, but you set them by editing the config file directly:

- **First time setup**: Choose a preset (Full/Essential/Minimal), pick a label language, then fine-tune individual elements
- **Customize anytime**: Toggle items on/off, adjust git display style, switch layouts, or change label language
- **Preview before saving**: See exactly how your HUD will look before committing changes

### Presets

| Preset | What's Shown |
|--------|--------------|
| **Full** | Everything enabled — tools, agents, todos, git, usage, duration |
| **Essential** | Activity lines + git status, minimal info clutter |
| **Minimal** | Core only — just model name and context bar |

After choosing a preset, you can turn individual elements on or off.

### Manual Configuration

Edit `~/.claude/plugins/claude-hud/config.json` directly for advanced settings such as `colors.*`,
`pathLevels`, `maxWidth`, threshold overrides, `display.timeFormat`, `display.hourCycle`, and `display.promptCacheTtlSeconds`. Running `/claude-hud:configure`
preserves those manual settings while still letting you change `language`, layout, and the common
guided toggles.

If you run several Claude config directories via `CLAUDE_CONFIG_DIR` and symlink `plugins/` to a
shared location, `plugins/claude-hud/config.json` is the same physical file for all of them. Put
per-directory settings in `$CLAUDE_CONFIG_DIR/claude-hud.json` instead - it uses the same shape,
only needs the keys it changes, and is layered on top of the shared config at load time:

For example, put this in `~/.config/claude/work/claude-hud.json`:

```json
{ "display": { "customLine": "Work Team" } }
```

Simplified and Traditional Chinese HUD labels are available as explicit opt-ins. English stays the default unless you choose a Chinese locale in `/claude-hud:configure` or set `language` in config. The `zh` alias maps to Simplified Chinese, and `zh-TW` maps to Traditional Chinese. Guided config writes the canonical `zh-Hans` or `zh-Hant` value.

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `language` | `en` \| `zh` \| `zh-Hans` \| `zh-Hant` \| `zh-TW` | `en` | HUD label language. Use `zh` or `zh-Hans` for Simplified Chinese and `zh-Hant` or `zh-TW` for Traditional Chinese. |
| `lineLayout` | string | `expanded` | Layout: `expanded` (multi-line) or `compact` (single line) |
| `pathLevels` | 1-3 \| `full` | 1 | Directory levels to show in project path, or `full` to show the entire absolute path |
| `maxWidth` | number \| `null` | `null` | Optional fallback width used only when terminal width detection fails completely |
| `forceMaxWidth` | boolean | false | Always use `maxWidth` when it is set, even if terminal width detection returns a smaller value |
| `elementOrder` | string[] | `["project","addedDirs","context","usage","promptCache","memory","environment","tools","skills","mcp","agents","todos","sessionTime"]` | Expanded-mode elemen

## tools

Usage display is **enabled by default** when Claude Code provides subscriber `rate_limits` data on stdin. It shows your rate limit consumption on line 2 alongside the context bar.

Set `display.usageValue` to `remaining` to show quota left instead of quota used. Warning colors and 7-day threshold checks still use the underlying used percentage.

ClaudeHUD prefers the official statusline stdin payload for rate-limit windows. If `display.externalUsagePath` points to a fresh local sidecar snapshot, ClaudeHUD can append its `balance_label` alongside stdin windows. If stdin `rate_limits` are missing, the same snapshot can provide fallback usage windows.

The fallback snapshot path must be absolute. The snapshot must be fresh enough (`display.externalUsageFreshnessMs`) and include valid `updated_at`, plus a `five_hour` window, `seven_day` window, `balance_label`, or `model_scoped` array. `balance_label` is optional text for prepaid provider balances; it is trimmed, length-limited, and sanitized before display. Relative paths, invalid JSON, stale files, or invalid timestamps are ignored quietly.

The snapshot may also carry `model_scoped` windows using the same shape Claude Code defines for stdin (`display_name`, `utilization` on the 0-100 scale, ISO `resets_at`). They render exactly like stdin scoped windows (see the model-scoped usage section) and stdin always wins when it carries its own `model_scoped` data. This lets a local feeder surface per-model weekly quotas (e.g. Fable) that the statusline payload does not include yet:

```json
{
  "updated_at": "2026-07-24T14:12:37Z",
  "model_scoped": [
    { "display_name": "Fable", "utilization": 89, "resets_at": "2026-07-27T11:00:00Z" }
  ]
}
```

One zero-credential way to produce such a snapshot is Claude Code's own `get_usage` control request, which returns `rate_limits.model_scoped` without spending tokens; a scheduled job can pipe it through `jq` into the snapshot file. The HUD itself never fetches anything: it only reads the file.

Set `display.externalUsageWritePath` if you want ClaudeHUD to write the official stdin `rate_limits` into a local snapshot for other tools. The path must be absolute, end in `.json`, and live in an existing directory. ClaudeHUD writes the file with private permissions and ignores invalid paths quietly.

Free/weekly-only accounts render the weekly window by itself instead of showing a ghost `5h: --` placeholder.

The 7-day percentage appears when above the `display.sevenDayThreshold` (default 80%):

```
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h) | ██████████ 85% (2d / 7d)
```

To disable, set `display.showUsage` to `false`.

Reset times use relative countdowns by default. Set `display.timeFormat` to `absolute` for wall-clock
times, `both` to show both forms, `elapsed` to show how far through each usage window you are, or
`elapsedAndAbsolute` to show elapsed window progress plus the wall-clock reset time. This setting is
manual-only today; `/claude-hud:configure` preserves it without editing it.

Wall-clock reset times (`absolute`/`both`/`elapsedAndAbsolute`) default to your system locale for 12-
vs 24-hour formatting. Set `display.hourCycle` to `h23` to force 24-hour time regardless of locale, or
to `h12`/`h11` to force 12-hour time with AM/PM. Set `display.showClockSeconds` to `true` to include
seconds in the wall-clock time, e.g. `at 14:30:07`.

Set `display.showResetLabel` to `false` if you want shorter usage countdowns such as `(3h 17m)` instead of `(resets in 3h 17m)`.

Set `display.usageCompact` to `true` if you want the shorter usage-only form, for example `5h: 25% (1h 30m)`. Compact usage takes precedence over `display.usageBarEnabled`.

Set `display.showModelScopedUsage` to `false` to hide the per-model weekly windows (e.g. Fable). The usage line then renders exactly as it would for an account that has none: the 5h/7d windows stay, snapshot windows are hidden along with the stdin ones, and a hidden window no longer counts towar

## requirements

- Claude Code v1.0.80+
- macOS/Linux: Node.js 18+ or Bun
- Windows: Node.js 18+

---

## Development

```bash
git clone https://github.com/jarrodwatts/claude-hud
cd claude-hud
npm ci && npm run build
npm test
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT — see [LICENSE](LICENSE)

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jarrodwatts/claude-hud&type=Date)](https://star-history.com/#jarrodwatts/claude-hud&Date)
