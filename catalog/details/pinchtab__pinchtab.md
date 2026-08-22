# pinchtab/pinchtab

High-performance browser automation bridge and multi-instance orchestrator with advanced stealth injection and real-time dashboard.

## tools

The primary user journey is:

1. install Pinchtab
2. install and start the daemon with `pinchtab daemon install`
3. point your agent or tool at `http://localhost:9867`
4. let PinchTab act as your local browser service

That is the default “replace the browser runtime” scenario.
Most users should not need to think about `pinchtab bridge` directly, and only need `pinchtab` when they want the local interactive menu.

## features

- **CLI or Curl** — Control via command-line or HTTP API
- **Token-efficient** — 800 tokens/page with text extraction (5-13x cheaper than screenshots)
- **Headless or Headed** — Run without a window or with visible Chrome
- **Multi-instance** — Run multiple parallel Chrome processes with isolated profiles
- **Self-contained** — ~15MB binary, no external dependencies
- **Accessibility-first** — Element refs that denote a DOM node, not a row: the same `e5` survives a change of filter, selector or depth (filtered views are sparse), and expires only on navigation to a new document
- **ARM64-optimized** — First-class Raspberry Pi support with automatic Chromium detection
- **CloakBrowser support** — Optional drop-in provider for sites that fingerprint stock Chromium. PinchTab launches a user-supplied CloakBrowser binary; no CloakBrowser is bundled in released artifacts. See [docs/guides/cloakbrowser.md](docs/guides/cloakbrowser.md).

---

## installation

### Installation

**macOS / Linux:**
```bash
curl -fsSL https://pinchtab.com/install.sh | bash
```

**Homebrew (macOS / Linux):**
```bash
brew install pinchtab/tap/pinchtab
```

**npm:**
```bash
npm install -g pinchtab
```

### Platform Support

PinchTab's primary tested operator workflow is local macOS and Linux.

Windows binaries are published, but Windows support is currently limited and best-effort because the project does not have the same level of automated and manual coverage there. On Windows, prefer running `pinchtab server` or `pinchtab bridge` directly instead of relying on the daemon workflow.

On **macOS**, prefer a dedicated automation browser (Google Chrome for Testing or Chromium) over your daily Google Chrome. Driving your primary Chrome headless can prevent it from opening a normal window while PinchTab is running. PinchTab now prefers a dedicated browser automatically, and `pinchtab doctor browsers` warns if automation would fall back to your primary Chrome — install Chrome for Testing or set `browser.binary` to a separate build. See [docs/reference/config.md](docs/reference/config.md).

### Shell Completion

Generate and install shell completions after `pinchtab` is on your `PATH`:

```bash
# Generate and install zsh completions
pinchtab completion zsh > "${fpath[1]}/_pinchtab"

# Generate bash completions
pinchtab completion bash > /etc/bash_completion.d/pinchtab

# Generate fish completions
pinchtab completion fish > ~/.config/fish/completions/pinchtab.fish
```

**Docker:**
```bash
docker run -d \
  --name pinchtab \
  -p 127.0.0.1:9867:9867 \
  -v pinchtab-data:/data \
  --shm-size=2g \
  pinchtab/pinchtab
```

The bundled container persists its managed config at `/data/.config/pinchtab/config.json`.
If you want to supply your own config file instead, mount it and point `PINCHTAB_CONFIG` at it:

```bash
docker run -d \
  --name pinchtab \
  -p 127.0.0.1:9867:9867 \
  -e PINCHTAB_CONFIG=/config/config.json \
  -v "$PWD/config.json:/config/config.json:ro" \
  -v pinchtab-data:/data \
  --shm-size=2g \
  pinchtab/pinchtab
```

### Use It

**First useful command — auto-starts the local server if needed:**
```bash
pinchtab nav https://pinchtab.com --snap
```

**Or start the server explicitly when you want foreground logs:**
```bash
pinchtab server
```

**Recommended for daily local use — install the daemon once:**
```bash
pinchtab daemon install
pinchtab daemon
```

That keeps PinchTab running in the background so your agent tools can reuse it without an open terminal.

**Terminal 2 — Control the browser:**
```bash
# Navigate; starts the server automatically if needed
pinchtab nav https://pinchtab.com

# Get page structure
pinchtab snap -i -c

# Click an element
pinchtab click e5

# Extract text
pinchtab text
```

Or use the HTTP API directly:
```bash
# Create a profile first (returns profile id)
PROF=$(curl -s -X POST http://localhost:9867/profiles \
  -H "Content-Type: application/json" \
  -d '{"name":"work"}' | jq -r '.id')

# Start an instance for that profile (returns instance id)
INST=$(curl -s -X POST http://localhost:9867/instances/start \
  -H "Content-Type: application/json" \
  -d "{\"profileId\":\"$PROF\",\"mode\":\"headless\"}" | jq -r '.id')

# Open a tab in that instance
TAB=$(curl -s -X POST http://localhost:9867/instances/$INST/tabs/open \
  -H "Content-Type: application/json" \
  -d '{"url":"https://pinchtab.com"}' | jq -r '.tabId')

# Get snapshot
curl "http://localhost:9867/tabs/$TAB/snapshot?filter=interactive"

# Click element
curl -X POST "http://localhost:9867/tabs/$TAB/action" \
  -H "Content-Type: application/json" \
  -d '{"kind":"click","ref":"e5"}'
```

---

## Core Concepts

**Server** — The main PinchTab process. It manages profiles, instances, routing, and the dashboard.

**Instance** — A running Chrome process. Each instance can have one profile.

**Profile** — Browser state (cookies, history, local storage). Log in once, stay logged in across restarts.

**Tab** — A single we
