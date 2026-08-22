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
