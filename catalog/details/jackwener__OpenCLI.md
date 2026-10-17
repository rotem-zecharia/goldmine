# jackwener/OpenCLI

Make Any Website into CLI & Use your logged-in browser by AI agent.

## installation

### 1. Install OpenCLI

For desktop use, start with **OpenCLIApp**. It bundles the OpenCLI runtime,
keeps the managed `opencli` command installed, and gives you a system tray UI
for setup, diagnostics, updates, browser-login keepalive, and Web → Markdown.

**Option A — OpenCLIApp (recommended for macOS / Windows):**
Download the latest app from <https://opencli.info/download>, install it, then
open the app once and use the System page to install or repair the `opencli`
command.

**Option B — npm global install (CLI-only / CI / servers):**
OpenCLI requires **Node.js >= 20.18.1** when installed through npm.

```bash
node --version
npm install -g @jackwener/opencli
```

### 2. Install the Browser Bridge Extension

OpenCLI connects to Chrome/Chromium through a lightweight Browser Bridge extension plus a small local daemon. The daemon auto-starts when needed.

**Option A — Chrome Web Store (recommended):**
Install **OpenCLI** from the [Chrome Web Store](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk).

**Option B — Manual install:**
1. Download the latest `opencli-extension-v{version}.zip` from the GitHub [Releases page](https://github.com/jackwener/opencli/releases).
2. Unzip it, open `chrome://extensions`, and enable **Developer mode**.
3. Click **Load unpacked** and select the unzipped folder.

### 3. Verify the setup

```bash
opencli doctor
```

### 4. Optional: name your Chrome profile

Each Chrome profile runs its own OpenCLI extension instance. If you use multiple Chrome profiles, list the connected profiles and assign local aliases:

```bash
opencli profile list
opencli profile rename <contextId> work
opencli profile use work
opencli --profile work browser main state
```

With only one connected profile, OpenCLI uses it automatically. With multiple connected profiles and no default, OpenCLI asks you to choose instead of guessing.

## tools

```bash
opencli list
opencli hackernews top --limit 5
opencli bilibili hot --limit 5
```

## For Humans

Use OpenCLI directly when you want a reliable command instead of a live browser session:

- `opencli list` shows every registered command.
- `opencli <site> <command>` runs a built-in or generated adapter.
- `opencli doctor` helps diagnose browser connectivity.

## Extending OpenCLI

If you want to add your own commands, start with the [Extending OpenCLI guide](./docs/guide/extending-opencli.md). README keeps this short; the guide covers the directory layout, source-control model, and install commands.

| Need | Recommended path |
|------|------------------|
| Keep personal website commands in your own Git repo | `opencli plugin create` + `opencli plugin install file://...` |
| Quickly draft a private local adapter | `opencli adapter init <site>/<command>` in `~/.opencli/clis/` |
| Modify an official adapter locally | `opencli adapter eject <site>` + `opencli adapter reset <site>` |
| Publish or install third-party commands | `opencli plugin install github:user/repo` |

### Close temporary browser tabs after use

To remove temporary owned tabs when a workflow finishes:

```bash
export OPENCLI_CLOSE_OWNED_TAB=1
opencli web read --url https://example.com --stdout true
# Multi-step browser sessions stay open between calls; close explicitly at the end:
opencli browser close --session research
```

This opts into closing only the current lease's owned tab. Chrome closes its
window automatically if no tabs remain; existing user pages and other sessions
are preserved. Bound tabs are detached and kept open. The default reusable
container policy, idle expiry, `--keep-tab true`, and persistent site sessions
remain unchanged. Use `--site-session ephemeral` for one-shot reads of adapters
that otherwise keep a persistent site session.

Cleanup uses a dedicated action, so older extensions reject it without releasing
the lease, and requires an extension acknowledgement. If cleanup fails or the extension
is too old, a warning reports it separately from the site action. Retry explicit
browser cleanup, or close a remaining one-shot adapter tab manually; do not
repeat a completed site write. Explicit `browser close` also exits
with an error; a one-shot adapter can still return its already-completed result.

## For AI Agents

OpenCLI's browser commands are designed to be used by AI Agents — not run manually. Install skills into your AI agent (Claude Code, Cursor, etc.), and the agent operates websites on your behalf using your logged-in Chrome session.

## configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENCLI_PROFILE` | — | Browser Bridge profile alias/contextId to use when multiple Chrome profiles are connected |
| `OPENCLI_WINDOW` | command default | Set to `foreground` or `background` to override Browser Bridge window placement. Browser-backed commands also accept `--window <foreground\|background>`. |
| `OPENCLI_SITE_SESSION` | adapter default | Set to `ephemeral` or `persistent` to override `siteSession` metadata for browser-backed adapter commands. `ephemeral` releases the one-shot tab when the command finishes, and the automation window stays open as a reusable container; `persistent` reuses the site's session. Per-command `--site-session` takes precedence. |
| `OPENCLI_CLOSE_OWNED_TAB` | `0` | Set to `1` to close the current owned tab on explicit session close or one-shot adapter cleanup instead of keeping a blank placeholder. Requires a supporting Browser Bridge extension. |
| `OPENCLI_SITE_SLOTS` | — | Pool sites onto warm persistent tabs, e.g. `xiaohongshu:1:1500-3000,weibo:2` (`site:poolSize[:minMs[-maxMs]]`). Each command run borrows one slot tab exclusively (reads included) and queues when all are busy; the optional interval spaces runs by a jittered delay. Tabs share one automation window and only its active tab renders, so with `poolSize` > 1 render-dependent commands (lazy-loaded lists) can stall on background slots — use `1` for those and for risk-controlled sites. `--site-session ephemeral` opts one invocation out. |
| `OPENCLI_BROWSER_CONNECT_TIMEOUT` | `45` | Seconds to wait for browser connection |
| `OPENCLI_BROWSER_COMMAND_TIMEOUT` | `60` | Seconds to wait for a single browser command |
| `OPENCLI_BROWSER_IDLE_TIMEOUT` | extension default | Owned session idle timeout in seconds; per-command `idleTimeout` takes precedence. Does not extend explicit cleanup: ephemeral adapters normally release their tab at command completion. Bound tabs and persistent adapter sessions ignore idle timeouts. Releasing a session keeps its reusable window container open. |
| `OPENCLI_CDP_ENDPOINT` | — | Chrome DevTools Protocol endpoint for remote browsers |
| `OPENCLI_CDP_TARGET` | — | Filter CDP targets by URL substring (e.g. `detail.1688.com`) |
| `OPENCLI_VERBOSE` | `false` | Enable verbose logging (`-v` flag also works) |
| `DEBUG_SNAPSHOT` | — | Set to `1` for DOM snapshot debug output |

`opencli browser *` requires an explicit `--session <name>` option for page operations, uses a foreground browser window by default, and keeps that session's tab lease until `opencli browser --session <session> close` or idle cleanup. Browser-backed adapters use a background adapter window and release one-shot tab leases by default. Interactive adapters can declare `siteSession: 'persistent'` to keep a stable site tab for continuity; pass `--site-session ephemeral` for a one-shot tab.
