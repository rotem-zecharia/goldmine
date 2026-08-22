# D4Vinci/Scrapling

🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

## features

### Spiders - A Full Crawling Framework
- 🕷️ **Scrapy-like Spider API**: Define spiders with `start_urls`, async `parse` callbacks, and `Request`/`Response` objects.
- ⚡ **Concurrent Crawling**: Configurable concurrency limits, per-domain throttling, and download delays.
- 🔄 **Multi-Session Support**: Unified interface for HTTP requests, and stealthy headless browsers in a single spider - route requests to different sessions by ID.
- 💾 **Pause & Resume**: Checkpoint-based crawl persistence. Press Ctrl+C for a graceful shutdown; restart to resume from where you left off.
- 📡 **Streaming Mode**: Stream scraped items as they arrive via `async for item in spider.stream()` with real-time stats - ideal for UI, pipelines, and long-running crawls.
- 🛡️ **Blocked Request Detection**: Automatic detection and retry of blocked requests with customizable logic.
- 🚦 **AutoThrottle**: Stop guessing delays. The spider tunes the delay of each domain on its own from how fast the website responds, then doubles it (or waits what `Retry-After` asks) whenever the website starts blocking or rate-limiting you, and speeds back up once it stops.
- 🤖 **Robots.txt Compliance**: Optional `robots_txt_obey` flag that respects `Disallow`, `Crawl-delay`, and `Request-rate` directives with per-domain caching.
- 🧪 **Development Mode**: Cache responses to disk on the first run and replay them on subsequent runs - iterate on your `parse()` logic without re-hitting the target servers.
- 🧩 **Ready-made Spider Templates**: Skip the boilerplate with `CrawlSpider` for rule-based link following, `SitemapSpider` for sitemap/robots.txt-driven crawls, `XMLFeedSpider`/`CSVFeedSpider` for iterating XML/RSS and CSV feeds, and `ShopifySpider` to pull every product out of any Shopify store through its JSON API, one item per variant.
- 🔗 **Link Extraction**: A standalone `LinkExtractor` primitive with allow/deny patterns, domain filters, CSS/XPath scoping, extension filtering, and canonicalization - use it inside the templates or on its own.
- 📦 **Built-in Export**: Export results through hooks and your own pipeline or the built-in JSON/JSONL/CSV/XML exporters with `result.items.to_json()`, `to_jsonl()`, `to_csv()`, and `to_xml()`.

### Advanced Websites Fetching with Session Support
- **HTTP Requests**: Fast and stealthy HTTP requests with the `Fetcher` class. Can impersonate browsers' TLS fingerprint, headers, and use HTTP/3.
- **Dynamic Loading**: Fetch dynamic websites with full browser automation through the `DynamicFetcher` class supporting Playwright's Chromium and Google's Chrome.
- **Anti-bot Bypass**: Advanced stealth capabilities with `StealthyFetcher` and fingerprint spoofing. Can easily bypass all types of Cloudflare's Turnstile/Interstitial with automation.
- **Session Management**: Persistent session support with `FetcherSession`, `StealthySession`, and `DynamicSession` classes for cookie and state management across requests.
- **Proxy Rotation**: Built-in `ProxyRotator` with cyclic or custom rotation strategies across all session types, plus per-request proxy overrides.
- **Domain & Ad Blocking**: Block requests to specific domains (and their subdomains) or enable built-in ad blocking (~3,500 known ad/tracker domains) in browser-based fetchers.
- **DNS Leak Prevention**: Optional DNS-over-HTTPS support to route DNS queries through Cloudflare's DoH, preventing DNS leaks when using proxies.
- **Remote Browsers**: Instead of launching a browser locally, connect to one that's already running through CDP with `cdp_url`, whether it's on the same machine, another host, or a managed browser provider. You can also point any browser fetcher at your own Chromium build with `executable_path`.
- **Background API Capture**: Pass a URL pattern to `capture_xhr`, and all matching XHR/fetch responses the page makes while loading are collected for you as `Response` objects in `response.captured_xhr` - grab a site's API data without reverse-engineering the requests yourself.
- **As

## tools

- 🔄 **Smart Element Tracking**: Relocate elements after website changes using intelligent similarity algorithms.
- 🎯 **Smart Flexible Selection**: CSS selectors, XPath selectors, filter-based search, text search, regex search, and more.
- 🔍 **Find Similar Elements**: Automatically locate elements similar to found elements.
- 🤖 **MCP Server to be used with AI**: Built-in MCP server for AI-assisted Web Scraping and data extraction. The MCP server features powerful, custom capabilities that leverage Scrapling to extract targeted content before passing it to the AI (Claude/Cursor/etc), thereby speeding up operations and reducing costs by minimizing token usage. ([demo video](https://www.youtube.com/watch?v=qyFk3ZNwOxE)) It can also keep browser sessions open across calls, take page screenshots, and drive remote browsers over CDP.
- 🧠 **Agent Skill**: A ready-to-install [Agent Skill](https://github.com/D4Vinci/Scrapling/tree/main/agent-skill) that teaches coding agents the whole library, so the code they write with Scrapling matches the current API instead of guessing.

### High-Performance & battle-tested Architecture
- 🚀 **Lightning Fast**: Optimized performance outperforming most Python scraping libraries.
- 🔋 **Memory Efficient**: Optimized data structures and lazy loading for a minimal memory footprint.
- ⚡ **Fast JSON Serialization**: 10x faster than the standard library.
- 🏗️ **Battle tested**: Not only does Scrapling have 92% test coverage and full type hints coverage, but it has been used daily by hundreds of Web Scrapers over the past year.

### Developer/Web Scraper Friendly Experience
- 🎯 **Interactive Web Scraping Shell**: Optional built-in IPython shell with Scrapling integration, shortcuts, and new tools to speed up Web Scraping scripts development, like converting curl requests to Scrapling requests and viewing requests results in your browser.
- 🚀 **Use it directly from the Terminal**: Optionally, you can use Scrapling to scrape a URL without writing a single line of code!
- 🛠️ **Rich Navigation API**: Advanced DOM traversal with parent, sibling, and child navigation methods.
- 🧬 **Enhanced Text Processing**: Built-in regex, cleaning methods, and optimized string operations.
- 📝 **Auto Selector Generation**: Generate robust CSS/XPath selectors for any element.
- 🔌 **Familiar API**: Similar to Scrapy/BeautifulSoup with the same pseudo-elements used in Scrapy/Parsel.
- 🤝 **Drop-in Scrapy Integration**: Already invested in Scrapy? Decorate any callback with `scrapling_response` to parse the responses you already fetch with Scrapling's parser, no rewrite needed.
- 📘 **Complete Type Coverage**: Full type hints for excellent IDE support and code completion. The entire codebase is automatically scanned with **PyRight** and **MyPy** with each change.
- 🔋 **Ready Docker image**: With each release, a Docker image containing all browsers is automatically built and pushed.

## installation

Let's give you a quick glimpse of what Scrapling can do without deep diving.

## requirements

1. If you are going to use any of the extra features below, the fetchers, or their classes, you will need to install fetchers' dependencies and their browser dependencies as follows:
    ```bash
    pip install "scrapling[fetchers]"
    
    scrapling install           # normal install
    scrapling install  --force  # force reinstall
    ```

    This downloads all browsers, along with their system dependencies and fingerprint manipulation dependencies.

    Or you can install them from the code instead of running a command like this:
    ```python
    from scrapling.cli import install
    
    install([], standalone_mode=False)          # normal install
    install(["--force"], standalone_mode=False) # force reinstall
    ```

2. Extra features:
   - Install the MCP server feature:
       ```bash
       pip install "scrapling[ai]"
       ```
   - Install shell features (Web Scraping shell and the `extract` command): 
       ```bash
       pip install "scrapling[shell]"
       ```
   - Install everything: 
       ```bash
       pip install "scrapling[all]"
       ```
   Remember that you need to install the browser dependencies with `scrapling install` after any of these extras (if you didn't already)

### Docker
You can also install a Docker image with all extras and browsers with the following command from DockerHub:
```bash
docker pull pyd4vinci/scrapling
```
Or download it from the GitHub registry:
```bash
docker pull ghcr.io/d4vinci/scrapling:latest
```
This image is automatically built and pushed using GitHub Actions and the repository's main branch.

## Contributing

We welcome contributions! Please read our [contributing guidelines](https://github.com/D4Vinci/Scrapling/blob/main/CONTRIBUTING.md) before getting started.

## Disclaimer

> [!CAUTION]
> This library is provided for educational and research purposes only. By using this library, you agree to comply with local and international data scraping and privacy laws. The authors and contributors are not responsible for any misuse of this software. Always respect the terms of service of websites and robots.txt files.

## 🎓 Citations
If you have used our library for research purposes please quote us with the following reference:
```text
  @misc{scrapling,
    author = {Karim Shoair},
    title = {Scrapling},
    year = {2024},
    url = {https://github.com/D4Vinci/Scrapling},
    note = {An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!}
  }
```

## License

This work is licensed under the BSD-3-Clause License.

## Acknowledgments

This project includes code adapted from:
- Parsel (BSD License)-Used for [translator](https://github.com/D4Vinci/Scrapling/blob/main/scrapling/core/translator.py) submodule

---
<div align="center"><small>Designed & crafted with ❤️ by Karim Shoair.</small></div><br>
