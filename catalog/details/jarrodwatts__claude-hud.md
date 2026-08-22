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

## configuration

```
◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2        ← Tools activity
◐ explore [haiku]: Finding auth code (2m 15s)    ← Agent status
▸ Fix authentication bug (2/5)                   ← Todo progress
```

---

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

## requirements

- Claude Code v1.0.80+
- macOS/Linux: Node.js 18+ or Bun
- Windows: Node.js 18+

---
