# CloakHQ/CloakBrowser

Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.

## installation

**Python:**

```bash
pip install cloakbrowser
```

**JavaScript / Node.js:**

```bash
# With Playwright
npm install cloakbrowser playwright-core

# With Puppeteer
npm install cloakbrowser puppeteer-core
```

**.NET / C#:**

```bash
dotnet add package CloakBrowser
```

> Community-maintained .NET client built on Microsoft.Playwright. See [`dotnet/README.md`](dotnet/README.md) for the full API.

---

On first run, the stealth Chromium binary is automatically downloaded (~200MB, cached locally).

**Optional:** Auto-detect timezone/locale from proxy IP:

```bash
pip install 'cloakbrowser[geoip]'
```

**Migrating from Playwright?** One-line change:

```diff
- from playwright.sync_api import sync_playwright
- pw = sync_playwright().start()
- browser = pw.chromium.launch()
+ from cloakbrowser import launch
+ browser = launch()

page = browser.new_page()
page.goto("https://example.com")
# ... rest of your code works unchanged
```

> ⭐ **Star** to show support — **[Watch releases](https://github.com/CloakHQ/CloakBrowser/subscription)** to get notified when new builds drop.

---

## Latest: v0.5.8 — 73 source-level stealth patches (Chromium 151.0.7922.108.2 — Linux + Windows)

- **CloakBrowser Pro Stable** — Chromium `151.0.7922.108.2` on Linux x64, Linux ARM64, and Windows x64; macOS remains on `150.0.7871.114.3`. Set a `license_key` (`licenseKey` in JS) or the `CLOAKBROWSER_LICENSE_KEY` env var and the wrapper fetches the latest Stable build for your platform automatically. See [CloakBrowser Pro](#cloakbrowser-pro)
- **CloakBrowser Pro Preview** — Chromium `151.0.7922.108.3` on Linux x64, Linux ARM64, Windows x64, and macOS. Opt in with `release_channel="preview"` or `CLOAKBROWSER_RELEASE_CHANNEL=preview`.
- **.NET 8 / C# client** — CloakBrowser now ships as a NuGet package (`CloakBrowser`), mirroring the Python and JS wrappers.
- **Chromium 151 upgrade** — rebased the full patch set onto Chromium 151 (Linux + Windows), re-validated against reference data; macOS remains on the Chromium 150 Stable line
- **73 fingerprint patches** — rendering consistency improvements across Linux and Windows, corrected GPU/display/graphics parameters to match stock Chrome profiles
- **Windows native GPU passthrough** — real hardware values pass through directly instead of being spoofed, matching real browser behavior
- **HTTP proxy inline credentials** — new network-layer support for proxies with inline authentication
- **`extension_paths`** — load Chrome extensions in all launch functions
- **Humanize actionability** — auto-wait for visible, enabled, stable elements before humanized actions
- **Per-call `human_config`** — override humanize settings on individual method calls
- **Composable JS helpers** — `buildLaunchOptions()` and `humanizeBrowser()` for custom Playwright integrations
- **Native SOCKS5 proxy** — `proxy="socks5://user:pass@host:port"` works directly in all launch functions, Python + JS. QUIC/HTTP3 tunnels through SOCKS5 via UDP ASSOCIATE
- **Proxy signal removal** — DNS/connect/SSL timing zeroed, proxy cache headers stripped, Proxy-Connection header leak removed
- **Chromium 146 upgrade** — rebased all patches from 145.0.7632.x to 146.0.7680.177
- **WebRTC IP spoofing** — `--fingerprint-webrtc-ip=auto` resolves your proxy's exit IP and spoofs WebRTC ICE candidates. Auto-injected when using `geoip=True` (no extra network call)
- **`humanize=True`** — one flag makes all mouse, keyboard, and scroll interactions behave like a real user. Bézier curves, per-character typing, realistic scroll patterns
- **Stealthy with zero flags** — binary auto-generates a random fingerprint seed at startup. No configuration required
- **Timezone & locale from proxy IP** — `launch(proxy="...", geoip=True)` auto-detects timezone and locale
- **Persistent profiles** — `launch_persistent_context()` keeps cookies and localStorage across sessions, bypasses incognito detection

See the full [CHANGELOG.md](CHANGELOG.md) for details.

## features

- **Config-level patches break** — `playwright-stealth`, `undetected-chromedriver`, and `puppeteer-extra` inject JavaScript or tweak flags. Every Chrome update breaks them. Antibot systems detect the patches themselves.
- **CloakBrowser patches Chromium source code** — fingerprints are modified at the C++ level, compiled into the binary. Detection sites see a real browser because it *is* a real browser.
- **Source-level stealth** — C++ patches handle fingerprints (GPU, screen, UA, hardware reporting) at the binary level. No JavaScript injection, no config-level hacks. Most stealth tools only patch at the surface.
- **Same behavior everywhere** — works identically local, in Docker, and on VPS. No environment-specific patches or config needed.
- **Works with AI agents and automation frameworks** — drop-in stealth for browser-use, Crawl4AI, Scrapling, Stagehand, LangChain, Selenium, and more. See [integrations](#framework-integrations).

CloakBrowser doesn't solve CAPTCHAs — it prevents them from appearing. No CAPTCHA-solving services, no proxy rotation built in — bring your own proxies, use the Playwright API you already know.

## CloakBrowser Pro

Anti-bot systems change every week and an older binary quietly degrades. The latest build is the one that keeps passing. **Try it free, then upgrade when you're running for real.**

- **Free, latest build (Chromium 151)** — the newest binary, the exact one that stays [green against live detection](#test-results). Free with a GitHub sign-in, one concurrent session. [Grab your key](https://cloakbrowser.dev/free) or run `cloakbrowser login`, then throw it at your hardest target.
- **Pro** — when it's part of production scraping, QA, monitoring, or automation: scale to **5, 20, 200, 2,000, or more concurrent sessions**, always first on the newest patches, with hands-on support. Linux, Windows, macOS. **[See plans and pricing →](https://cloakbrowser.dev)**
- **v146** — the older build stays free on [GitHub Releases](https://github.com/CloakHQ/cloakbrowser/releases). A quick first look, but it ages fast as detection evolves.

```bash
cloakbrowser login          # GitHub sign-in for a free key, or paste a paid key
# ...or set it directly (env var, license_key= param, or ~/.cloakbrowser/license.key):
export CLOAKBROWSER_LICENSE_KEY=cb_xxxxxxxx
```

Try the latest free → **[cloakbrowser.dev/free](https://cloakbrowser.dev/free)**  ·  Scale up on Pro → **[cloakbrowser.dev](https://cloakbrowser.dev)**

## Test Results

All tests verified against live detection services. Results below are for the latest Pro/current build unless noted. Last tested: Aug 2026 (Chromium 151).

| Detection Service | Stock Playwright | CloakBrowser | Notes |
|---|---|---|---|
| **reCAPTCHA v3** | 0.1 (bot) | **0.9** (human) | Pro/current build; server-side verified |
| **Cloudflare Turnstile** (non-interactive) | FAIL | **PASS** | Auto-resolve |
| **Cloudflare Turnstile** (managed) | FAIL | **PASS** | Single click |
| **ShieldSquare** | BLOCKED | **PASS** | Production site |
| **FingerprintJS** bot detection | DETECTED | **PASS** | Pro/current build; demo.fingerprint.com |
| **BrowserScan** bot detection | DETECTED | **NORMAL** (4/4) | browserscan.net |
| **bot.incolumitas.com** | 13 fails | **1 fail** | WEBDRIVER spec only |
| **deviceandbrowserinfo.com** | 6 true flags | **0 true flags** | `isBot: false` |
| `navigator.webdriver` | `true` | **`false`** | Source-level patch |
| `navigator.plugins.length` | 0 | **5** | Real plugin list |
| `window.chrome` | `undefined` | **`object`** | Present like real Chrome |
| UA string | `HeadlessChrome` | **`Chrome/151.0.0.0`** | No headless leak |
| CDP detection | Detected | **Not detected** | `isAutomatedWithCDP: false` |
| TLS fingerprint | Mismatch | **Identical to Chrome** | ja3n/ja4/akamai match |
| | | **Tested against 30+ detection sites** | |

### Proof

<p align="center">
<img src="https://i.imgur.com/hvIQyMv.png" width="600" alt="reCAPTCHA v3 — Score 0.9">
<br><em>Pro/

## tools

### `launch()`

```python
from cloakbrowser import launch

## configuration

browser = launch()

# Headed mode (see the browser window)
browser = launch(headless=False)

# Latest binary — pass a key (free via `cloakbrowser login`, or paid) or set CLOAKBROWSER_LICENSE_KEY
browser = launch(license_key="cb_xxxxxxxx")

# With proxy (HTTP or SOCKS5)
browser = launch(proxy="http://user:pass@proxy:8080")
browser = launch(proxy="socks5://user:pass@proxy:1080")

# With proxy dict (bypass, separate auth fields)
browser = launch(proxy={"server": "http://proxy:8080", "bypass": ".google.com", "username": "user", "password": "pass"})

# With extra Chrome args
browser = launch(args=["--disable-gpu"])

# With timezone and locale (sets binary flags — no detectable CDP emulation)
browser = launch(timezone="America/New_York", locale="en-US")
