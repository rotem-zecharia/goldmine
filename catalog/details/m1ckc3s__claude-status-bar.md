# m1ckc3s/claude-status-bar

Menu bar status indicator for Claude Code

## installation

### Homebrew (recommended)

```bash
brew install --cask claude-status-bar && open -a "Claude Status Bar"
```

The one launch at the end matters: it wires up the Claude Code hooks automatically. After that it starts itself whenever Claude Code runs.

**Already using the app from the DMG?** The same command switches you to Homebrew. Your settings and hooks carry over, and the old copy cleans itself up on first launch. Full details, edge cases, and the tested upgrade matrix: **[HOMEBREW.md](HOMEBREW.md)**.

> [!IMPORTANT]
> **Updated (or installed) mid-session?** Sessions already open appear the next time they do something (a prompt or a tool call). Starting a new `claude` session also works.

### DMG

*Signed and notarized by Apple*

1. Download the latest `ClaudeStatusBar.dmg` from [Releases](../../releases).
2. Open it and drag **Claude Status Bar** into Applications.
3. Launch it once. On first launch it wires up the Claude Code hooks for you automatically.
4. Start a new Claude Code session, the icon appears whenever Claude Code is running.

## Updating

The menu tells you when an update is ready. Installed via brew, it shows **Update via brew** with a copy button (paste the command in your terminal); it appears once Homebrew can actually deliver the new version, which can lag a release by up to a day. Installed via DMG, **Update available** opens the releases page, plus a one-click **Switch to Homebrew** option.

Or just run `brew upgrade --cask claude-status-bar` (brew), or download the latest DMG and drag it into Applications (manual). Hooks refresh themselves on the next launch; nothing to run by hand. **Upgrading from 0.3.x via DMG? Launch the app once after dragging**, that's what retires the old-named copy ([details](HOMEBREW.md#faq--troubleshooting)).

## What it shows

- **Thinking / working** — the icon animates, with a live `1m 1s` timer.
- **Running a tool** — a short label (`Editing`, `Reading`, `Running command`, `Using tool`, …).
- **Awaiting permission** — a paused yellow dot, in both the CLI and the Desktop app.
- **Idle / done** — rests on the Claude logo.

Everything is controlled from the menu:

- **Show timer:** toggle the elapsed `1m 1s` clock.
- **Thinking words:** rotate a playful verb (`Manifesting…`, `Percolating…`) in place of `Thinking…`, like Claude Code (on by default).
- **Animation style:**
  - **Claude Spark**, the web/chat "morph" spark
  - **Claude Code**, the terminal glyph spinner
  - **Clawd Crab Walking**, a pixel-art Clawd crab that scuttles while Claude works
- **Icon color:** **Orange** or **System** (adaptive black/white). All three styles follow this setting: in System mode Crab Walking renders as a shaded monochrome silhouette that matches the menu bar.
- **Version and update:** the menu shows your current version and tells you when an update is ready (see [Updating](#updating)).

### Where it works

| Surface | Tracked? |
|---|---|
| Claude Code CLI (terminal) | ✅ |
| Claude Code Desktop — **Code** tab | ✅ |
| Cursor (Claude Code extension) | ✅ |
| Claude Desktop — **Chat/Cowork** tab | ❌ |

**Multi-session support.** When several Claude Code sessions run at once (multiple terminals, or a terminal plus the desktop app), the menu bar surfaces the highest-priority one: a session awaiting your permission is never hidden behind one that's thinking. The dropdown lists every live session. Precise per-tab focus is in progress: **[issue #19 →](https://github.com/m1ckc3s/claude-status-bar/issues/19)**.

## How it works

> [!NOTE]
> You don't open this app; it opens itself when a Claude Code session starts, and quits when none is running. The only manual launch is the very first one after install, to set up the hooks. Opened by hand with no session active, it quits again after a few seconds. That's normal.

The app is stateless. Claude Code fires hooks as it works; the app polls those updates and aggregates them across every live session into a single icon, a permission dot if one needs yo

## requirements

- macOS 12+, [Claude Code](https://claude.com/claude-code) (CLI or the Desktop app), Node.js

## Troubleshooting

See [Troubleshooting](TROUBLESHOOTING.md)
