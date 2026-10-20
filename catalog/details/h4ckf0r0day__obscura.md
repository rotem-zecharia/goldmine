# h4ckf0r0day/obscura

The headless browser for AI agents and web scraping

## features

| Metric       | Obscura      | Headless Chrome |
|--------------|--------------|------------------|
| Memory       | **30 MB**    | 200+ MB          |
| Binary size  | **~70 MiB**  | 300+ MB          |
| Anti-detect  | **Built-in** | None          |
| Page load    | **85 ms**    | ~500 ms          |
| Startup      | **Instant**  | ~2s              |
| Puppeteer    | **Yes**      | Yes              |
| Playwright   | **Yes**      | Yes              |

<table>
  <tr>
    <td width="90" align="center">
      <a href="https://blog.cloudflare.com/kitesurf/">
        <img
          src="https://cdn.simpleicons.org/cloudflare/F38020"
          alt="Cloudflare"
          width="54"
        />
      </a>
    </td>
    <td>
      <strong>Obscura inspired Cloudflare Kitesurf’s first prototype</strong>
      <br>
      Cloudflare began by porting Obscura to Workers while developing its
      new agent-first browser.
      <br>
      <a href="https://blog.cloudflare.com/kitesurf/">
        Read Cloudflare’s engineering story →
      </a>
    </td>
  </tr>
</table>

## Obscura Cloud

We are working on **Obscura Cloud** the hosted version, with managed infrastructure, residential proxies, and dedicated support. For people who want the engine without operating it themselves.

The open-source engine stays Apache-2.0, fully featured. No feature gating, ever.

**[Get on the waitlist →](https://tally.so/r/gDWzdD)**
<br>
**[📅 Book a demo →](https://cal.com/obscura/quick-chat)**

### Open Source Support

<a href="https://vercel.com/open-source-program">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge-2026.svg" />
</a>

## Sponsors

**Obscura** is supported by organizations helping us build independent open-source browser infrastructure.

Want to sponsor? Email [hello@obscura.sh](mailto:hello@obscura.sh).

<table>
   <tr>
    <td width="200" align="center" valign="middle">
      <a href="https://go.nodemaven.com/obscurareadmeoctober" target="_blank">
        <img alt="NodeMaven" src="assets/sponsors/nodemaven4.png" width="180"/>
      </a>
    </td>
    <td valign="middle">
      <a href="https://go.nodemaven.com/obscurareadmeoctober" target="_blank"><b>NodeMaven</b></a>: The most efficient proxy provider for Web Scraping and Automation with the Highest Quality IP on the market.<br><br>
      <b>Why <a href="https://go.nodemaven.com/obscurareadmeoctober" target="_blank">NodeMaven</a>?</b><br>
      ZIP targeting<br>
      99.9% uptime<br>
      IP filtering: all proxies have fraud score &lt;97%<br>
      No KYC required<br>
      Unique free tools: Proxy Bandwidth Checker, Meta Tag Checker, IP Lookup and others!<br><br>
      🎁 <b>Special codes for Obscura users:</b><br>
      <b>OBSCURA35</b> - 35% off to Mobile and Residential Proxies<br>
      <b>OBSCURA40</b> - 40% off to ISP (Static) Proxies
    </td>
    <tr>
    <td width="200" align="center" valign="middle">
      <a href="https://masklabs.io" target="_blank">
        <img alt="Masklabs" src="assets/sponsors/Masklabs.png" width="180"/>
      </a>
    </td>
    <td valign="middle">
      <b>Obscura + <a href="https://masklabs.io" target="_blank">Masklabs</a></b><br><br>
      Obscura masks the browser. Masklabs masks the traffic.<br><br>
      Mobile proxies for scrapers, bots, and AI agents that need to look human. Real carrier IPs across a rotating pool, zero shared-IP baggage.<br><br>
      Pair Obscura's stealth rendering with Masklabs' mobile network and your requests blend into everyday traffic.<br><br>
      💸 <b>Try it free for 30 days.</b><br><br>
      🎁 Use code <b>OBSCURA25</b> for <b>25% off your first month</b>.
    </td>
  </tr>
</table>

## installation

### Download

Grab the latest binary from [Releases](https://github.com/h4ckf0r0day/obscura/releases):

```bash
# Linux x86_64
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-linux.tar.gz
tar xzf obscura-x86_64-linux.tar.gz
./obscura fetch https://example.com --eval "document.title"

# Linux ARM64 (aarch64)
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-aarch64-linux.tar.gz
tar xzf obscura-aarch64-linux.tar.gz

# NixOS
nix-env -iA nixpkgs.obscura

# macOS Apple Silicon
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-aarch64-macos.tar.gz
tar xzf obscura-aarch64-macos.tar.gz

# macOS Intel
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-macos.tar.gz
tar xzf obscura-x86_64-macos.tar.gz

# Windows
Download the `.zip` from the releases page and extract it manually.
```

No Chrome, no Node.js, no dependencies. Release archives include both
`obscura` and `obscura-worker`; keep them in the same directory for the
parallel `scrape` command.

| Archive suffix | Rendering | Stealth transport |
|----------------|-----------|-------------------|
| none | Yes | No |
| `-stealth` | Yes | Yes |
| `-no-render` | No | No |
| `-no-render-stealth` | No | Yes |

Linux release builds target Ubuntu 22.04 so the downloaded binary remains
usable on common LTS servers with glibc 2.35+.

### Docker

```bash
docker run -d --name obscura -p 127.0.0.1:9222:9222 \
  -e OBSCURA_CDP_TOKEN="$(openssl rand -hex 32)" \
  h4ckf0r0day/obscura
```

Image on [Docker Hub](https://hub.docker.com/r/h4ckf0r0day/obscura). Multi-stage build on `distroless/cc:nonroot` — no shell, no package manager, runs as uid 65532, ~57 MB compressed. A mounted `--storage-dir` must be writable by uid 65532. Publish to host loopback as above; `-p 9222:9222` exposes the port on every interface.

### Build from source

```bash
git clone https://github.com/h4ckf0r0day/obscura.git
cd obscura

# Rendering
cargo build --release -p obscura-cli --bins --features render

# Rendering and stealth
cargo build --release -p obscura-cli --bins --features render,stealth

# No rendering
cargo build --release -p obscura-cli --bins --no-default-features

# No rendering, with stealth
cargo build --release -p obscura-cli --bins --no-default-features --features stealth
```

Requires Rust 1.75+ ([rustup.rs](https://rustup.rs)). First build takes ~5 min (V8 compiles from source, cached after).
The stealth build also compiles BoringSSL and generates bindings, so it needs
CMake, Clang, and the libclang/LLVM development libraries. On Ubuntu/Debian:

```bash
sudo apt-get install build-essential cmake clang libclang-dev llvm-dev
```

The rendering build uses rustls. The rendering-and-stealth build uses
wreq/BoringSSL and therefore needs the additional build tools above.

## Quick Start

### Fetch a page

```bash
# Get the page title
obscura fetch https://example.com --eval "document.title"

# Extract all links
obscura fetch https://example.com --dump links

# Render JavaScript and dump HTML
obscura fetch https://news.ycombinator.com --dump html

# Write dump or eval output to a file
obscura fetch https://example.com --dump text --output page.txt

# Stream the raw response body verbatim (binary-safe; bypasses the JS/DOM layer).
# Use this for images, JSON, JS, CSS, or any non-HTML resource.
obscura fetch https://picsum.photos/200/300 --dump original > photo.jpg

# List every sub-resource URL the page would fetch (NDJSON; one record per asset)
obscura fetch https://example.com --dump assets

# Fetch through an HTTP or SOCKS proxy
obscura --proxy socks5://127.0.0.1:1080 fetch https://example.com --dump text

# Wait for dynamic content
obscura fetch https://example.com --wait-until networkidle0

# Bound navigation time for slow or broken pages
obscura fetch https://example.com --timeout 10

# Capture the settled page as PNG
obscura fetch https://example.com --screenshot page.pn

## tools

Obscura implements the Chrome DevTools Protocol for Puppeteer/Playwright compatibility.

| Domain | Methods |
|--------|---------|
| **Target** | createTarget, closeTarget, attachToTarget, createBrowserContext, disposeBrowserContext |
| **Page** | navigate, getFrameTree, lifecycleEvents, captureScreenshot, start/stopScreencast, printToPDF |
| **Runtime** | evaluate, callFunctionOn, getProperties, addBinding |
| **DOM** | getDocument, querySelector, querySelectorAll, getOuterHTML, resolveNode |
| **Network** | enable, setCookies, getCookies, setExtraHTTPHeaders, setUserAgentOverride |
| **Fetch** | enable, continueRequest, fulfillRequest, failRequest (live interception), takeResponseBodyAsStream |
| **IO** | read, close (stream a large response body in chunks) |
| **Storage** | getCookies, setCookies, deleteCookies |
| **Input** | dispatchMouseEvent, dispatchKeyEvent |
| **LP** | getMarkdown (DOM-to-Markdown conversion) |

To download a large resource without one giant `Network.getResponseBody` blob, call `Fetch.takeResponseBodyAsStream` then read it in chunks with `IO.read` / `IO.close`. Response bodies over the cache limit (`OBSCURA_NETWORK_BODY_BUFFER_BYTES`, default 2 MiB) are not retained, so raise that limit when you intend to stream large downloads.
## CLI Reference

### Tuning V8

Obscura embeds V8 directly. Use `--v8-flags` to pass raw flags through to V8, same syntax as Chromium's `--js-flags` and Node's command-line flags. Most common use is raising the heap cap to fix `JavaScript heap out of memory` on JS-heavy pages:

```bash
obscura --v8-flags "--max-old-space-size=4096" fetch <url>
```

### Heavy SPAs (script execution budget)

Obscura caps the page's script-execution phase so one slow or hung page cannot stall a worker. The default budget is 30s; pages that finish sooner return immediately, so the cap only affects pages that keep running. A very heavy React/Vue/Angular SPA on a slow network can need more time to boot before it fires its data requests. Raise the budget with `OBSCURA_SCRIPT_DEADLINE_MS` (milliseconds), and pair it with a matching navigation timeout in your CDP client:

```bash
OBSCURA_SCRIPT_DEADLINE_MS=60000 obscura serve --port 9222
```

Modules that enhance an already-rendered page have a separate 3s per-module budget so one non-essential module cannot hold navigation open. Raise it for legitimate long-running modules such as a Vite HMR client:

```bash
OBSCURA_MODULE_BUDGET_MS=10000 obscura serve --port 9222
```

An unmounted SPA shell already gives its app modules the full `OBSCURA_SCRIPT_DEADLINE_MS` budget. `OBSCURA_FETCH_TIMEOUT_MS` controls the module's network request, not its evaluation time. See [Environment variables](docs/Environment-variables.md) for the complete timeout model.

### `obscura serve`

Start a CDP WebSocket server.

| Flag | Default | Description |
|------|---------|-------------|
| `--port` | `9222` | WebSocket port |
| `--proxy` | — | HTTP/SOCKS5 proxy URL |
| `--stealth` | off | Enable anti-detection + tracker blocking |
| `--workers` | `1` | Number of parallel worker processes |
| `--worker-max-connections` | off | Recycle a worker after N CDP connections (needs `--workers` > 1) |
| `--worker-max-rss` | off | Recycle a worker above this many MB resident (Linux) |
| `--worker-max-age` | off | Recycle a worker after this many seconds |
| `--worker-drain-timeout` | `120` | Seconds a replaced worker may finish its live connections before it is killed |
| `--font-dir` | — | Recursively load fonts once per worker (repeatable; render build) |
| `--obey-robots` | off | Respect robots.txt |

With multiple workers, exited children are reaped and restarted. New connections
use ready workers only; if none are ready, the balancer returns HTTP 503. A crash
still closes that worker's existing sessions, which clients must reconnect.

The `--worker-max-*` options recycle workers gracefully: a replacement starts
first, new connections go only to it, and the old worker keeps serving 

## configuration

```json
{
  "mcpServers": {
    "obscura": {
      "command": "obscura",
      "args": ["mcp"]
    }
  }
}
```
