# vakra-dev/reader

Open source web infrastructure for AI. Scrape, crawl, and automate the web, clean markdown, browser sessions, ready for your agents.

## features

- **Browser Sessions** - Launch stealthed Chrome, connect Playwright/Puppeteer via CDP
- **Anti-Bot Bypass** - TLS fingerprinting, navigator spoofing, WebRTC masking, `webdriver=false`
- **Clean Output** - Markdown and HTML with automatic main content extraction
- **Smart Content Cleaning** - Removes nav, headers, footers, popups, cookie banners
- **CLI & API** - Use from command line or programmatically
- **Browser Pool** - Auto-recycling, health monitoring, tiered proxy pools
- **Concurrent Scraping** - Parallel URL processing with progress tracking
- **Website Crawling** - BFS link discovery with depth/page limits
- **Tiered Proxies** - Standard and premium proxy pools with health tracking

## installation

```bash
npm install @vakra-dev/reader
```

**Requirements:** Node.js >= 18

> **First run:** Playwright bundles Chromium for all platforms. Install it with:
>
> ```bash
> npx playwright install chromium
> ```

## Quick Start

### Cloud (Fastest)

Get an API key at [console.reader.dev](https://console.reader.dev) and start scraping immediately:

```typescript
import { ReaderClient } from "@vakra-dev/reader-js";

const reader = new ReaderClient({ apiKey: process.env.READER_API_KEY });

const result = await reader.read({ url: "https://example.com" });
if (result.kind === "scrape") {
  console.log(result.data.markdown);
}
```

```bash
npm install @vakra-dev/reader-js
```

See the [cloud docs](https://docs.reader.dev) for the full API reference.

### Self-Hosted

Install the reader engine and run scraping on your own infrastructure:

### Basic Scrape

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown", "html"],
});

console.log(result.data[0].markdown);
console.log(result.data[0].html);

await reader.close();
```

## tools

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://example.com", "https://example.org", "https://example.net"],
  formats: ["markdown"],
  batchConcurrency: 3,
  onProgress: (progress) => {
    console.log(`${progress.completed}/${progress.total}: ${progress.currentUrl}`);
  },
});

console.log(`Scraped ${result.batchMetadata.successfulUrls} URLs`);

await reader.close();
```

### Crawling

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.crawl({
  url: "https://example.com",
  depth: 2,
  maxPages: 20,
  scrape: true,
});

console.log(`Discovered ${result.urls.length} URLs`);
console.log(`Scraped ${result.scraped?.batchMetadata.successfulUrls} pages`);

await reader.close();
```

### Browser Session

Launch a stealthed Chrome and control it with Playwright or Puppeteer. The browser has anti-bot stealth active (`webdriver=false`, navigator spoofing, WebRTC masking). Your existing scripts just work.

```typescript
import { ReaderClient } from "@vakra-dev/reader";
import { chromium } from "playwright-core";

const reader = new ReaderClient();

// Create a browser session - returns a CDP WebSocket URL
const session = await reader.browser();

// Connect Playwright (one-line change from a local script)
const browser = await chromium.connectOverCDP(session.wsEndpoint);
const context = await browser.newContext();
const page = await context.newPage();

// Use Playwright normally - full stealth active
await page.goto("https://news.ycombinator.com/");
console.log(await page.title());

await browser.close();
await session.close();
await reader.close();
```

Also works with Puppeteer:

```typescript
import { connect } from "puppeteer-core";

const browser = await connect({ browserWSEndpoint: session.wsEndpoint });
```

### With Proxy

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient();

const result = await reader.scrape({
  urls: ["https://example.com"],
  formats: ["markdown"],
  proxy: {
    type: "premium",
    host: "proxy.example.com",
    port: 8080,
    username: "username",
    password: "password",
    country: "us",
  },
});

await reader.close();
```

### With Tiered Proxy Pools

Configure standard (datacenter, fast) and premium (residential, anti-bot) proxy tiers:

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient({
  proxyPools: {
    standard: [
      { url: "http://user:pass@dc-proxy1:8080" },
      { url: "http://user:pass@dc-proxy2:8080" },
    ],
    premium: [{ url: "http://user:pass@res-proxy1:8080" }],
  },
});

const result = await reader.scrape({
  urls: ["https://example.com"],
  proxyMode: "standard", // or "premium" for anti-bot sites
});

await reader.close();
```

Or via environment variables:

```bash
PROXY_STANDARD=http://user:pass@dc1:8080,http://user:pass@dc2:8080
PROXY_PREMIUM=http://user:pass@res1:8080
```

## configuration

```typescript
import { ReaderClient } from "@vakra-dev/reader";

const reader = new ReaderClient({
  browserPool: {
    size: 5, // 5 browser instances
    retireAfterPages: 50, // Recycle after 50 pages
    retireAfterMinutes: 15, // Recycle after 15 minutes
  },
  verbose: true,
});

const result = await reader.scrape({
  urls: manyUrls,
  batchConcurrency: 5,
});

await reader.close();
```

## CLI Reference

### Daemon Mode

For multiple requests, start a daemon to keep browser pool warm:

```bash
# Start daemon with browser pool
npx reader start --direct-pool-size 5
