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
