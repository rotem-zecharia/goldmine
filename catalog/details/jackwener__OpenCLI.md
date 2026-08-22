# jackwener/OpenCLI

Make Any Website into CLI & Use your logged-in browser by AI agent.

## installation

For desktop use, start with **OpenCLIApp**. It bundles the OpenCLI runtime,
keeps the managed `opencli` command installed, and gives you a system tray UI
for setup, diagnostics, updates, browser-login keepalive, and Web → Markdown.

**Option A — OpenCLIApp (recommended for macOS / Windows):**
Download the latest app from <https://opencli.info/download>, install it, then
open the app once and use the System page to install or repair the `opencli`
command.

**Option B — npm global install (CLI-only / CI / servers):**
OpenCLI requires **Node.js >= 20** when installed through npm.

```bash
node --version
npm install -g @jackwener/opencli
```

## tools

```bash
opencli list
opencli hackernews top --limit 5
opencli bilibili hot --limit 5
```

## configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENCLI_PROFILE` | — | Browser Bridge profile alias/contextId to use when multiple Chrome profiles are connected |
| `OPENCLI_WINDOW` | command default | Set to `foreground` or `background` to override Browser Bridge window placement. Browser-backed commands also accept `--window <foreground\|background>`. |
| `OPENCLI_BROWSER_CONNECT_TIMEOUT` | `45` | Seconds to wait for browser connection |
| `OPENCLI_BROWSER_COMMAND_TIMEOUT` | `60` | Seconds to wait for a single browser command |
| `OPENCLI_CDP_ENDPOINT` | — | Chrome DevTools Protocol endpoint for remote browser or Electron apps |
| `OPENCLI_CDP_TARGET` | — | Filter CDP targets by URL substring (e.g. `detail.1688.com`) |
| `OPENCLI_VERBOSE` | `false` | Enable verbose logging (`-v` flag also works) |
| `DEBUG_SNAPSHOT` | — | Set to `1` for DOM snapshot debug output |

`opencli browser *` requires an explicit `<session>` positional, uses a foreground browser window by default, and keeps that session's tab lease until `opencli browser <session> close` or idle cleanup. Browser-backed adapters use a background adapter window and release one-shot tab leases by default. Interactive adapters can declare `siteSession: 'persistent'` to keep a stable site tab for continuity; pass `--site-session ephemeral` for a one-shot tab.
