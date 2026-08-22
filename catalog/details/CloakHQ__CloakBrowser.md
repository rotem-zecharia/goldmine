# CloakHQ/CloakBrowser

Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.

## installation

**Python:**

```bash
pip install cloakbrowser
```

**JavaScript / Node.js:**

```bash

## features

- **Config-level patches break** — `playwright-stealth`, `undetected-chromedriver`, and `puppeteer-extra` inject JavaScript or tweak flags. Every Chrome update breaks them. Antibot systems detect the patches themselves.
- **CloakBrowser patches Chromium source code** — fingerprints are modified at the C++ level, compiled into the binary. Detection sites see a real browser because it *is* a real browser.
- **Source-level stealth** — C++ patches handle fingerprints (GPU, screen, UA, hardware reporting) at the binary level. No JavaScript injection, no config-level hacks. Most stealth tools only patch at the surface.
- **Same behavior everywhere** — works identically local, in Docker, and on VPS. No environment-specific patches or config needed.
- **Works with AI agents and automation frameworks** — drop-in stealth for browser-use, Crawl4AI, Scrapling, Stagehand, LangChain, Selenium, and more. See [integrations](#framework-integrations).

CloakBrowser doesn't solve CAPTCHAs — it prevents them from appearing. No CAPTCHA-solving services, no proxy rotation built in — bring your own proxies, use the Playwright API you already know.

## configuration

browser = launch()

## tools

CloakBrowser ships a TypeScript package with full type definitions. Choose Playwright or Puppeteer — same stealth binary underneath.
