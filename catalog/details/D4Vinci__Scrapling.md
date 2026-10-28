# D4Vinci/Scrapling

🕷️ The BEST Web Scraping framework that handles everything from a single request to a full-scale crawl! Don't be shy, join here: https://discord.gg/EMgGbDceNQ and follow here for daily tips and tricks

## features

### Spiders - A Full Crawling Framework
- 🕷️ **Scrapy-like Spider API**: Define spiders with `start_urls`, async `parse` callbacks, and `Request`/`Response` objects.
- ⚡ **Concurrent Crawling**: Configurable concurrency limits, per-domain throttling, and download delays.
- 🔄 **Multi-Session Support**: Unified interface for HTTP requests, and stealthy headless browsers in a single spider - route requests to different sessions by ID.
- 💾 **Pause & Resume**: Save pending requests and seen URLs with `crawldir`. Press Ctrl+C to stop gracefully and restart with the same directory.
- 📡 **Streaming Mode**: Stream scraped items as they arrive via `async for item in spider.stream()` with real-time stats - ideal for UI, pipelines, and long-running crawls.
- 🛡️ **Blocked Request Detection**: Automatic detection and retry of blocked requests with customizable logic.
- 🚦 **AutoThrottle**: Stop guessing delays. The spider tunes the delay of each domain on its own from how fast the website responds, then doubles it (or waits what `Retry-After` asks) whenever the website starts blocking or rate-limiting you, and speeds back up once it stops.
- 🤖 **Robots.txt Compliance**: Optional `robots_txt_obey` flag that respects `Disallow`, `Crawl-delay`, and `Request-rate` directives with per-domain caching.
- 🧪 **Development Mode**: Cache responses to disk on the first run and replay them on subsequent runs - iterate on your `parse()` logic without re-hitting the target servers.
- 🧩 **Ready-made Spider Templates**: Skip the boilerplate with `CrawlSpider` for rule-based link following, `SitemapSpider` for sitemap/robots.txt-driven crawls, `XMLFeedSpider`/`CSVFeedSpider` for iterating XML/RSS and CSV feeds, and `ShopifySpider` to collect products from public Shopify stores, one item per variant.
- 🔗 **Link Extraction**: A standalone `LinkExtractor` primitive with allow/deny patterns, domain filters, CSS/XPath scoping, extension filtering, and canonicalization - use it inside the templates or on its own.
- 📦 **Built-in Export**: Export results through hooks and your own pipeline or the built-in JSON/JSONL/CSV/XML exporters with `result.items.to_json()`, `to_jsonl()`, `to_csv()`, and `to_xml()`.

### Advanced Websites Fetching with Session Support
- **HTTP Requests**: Fast and stealthy HTTP requests with the `Fetcher` class. Can impersonate browsers' TLS fingerprint, headers, and use HTTP/3.
- **Dynamic Loading**: Fetch dynamic websites with full browser automation through the `StealthyFetcher` class supporting Playwright's Chromium and Google's Chrome.
- **Anti-bot Bypass**: Advanced stealth capabilities with `StealthyFetcher` and fingerprint spoofing. Can easily bypass all types of Cloudflare's Turnstile/Interstitial with automation.
- **Session Management**: Persistent session support with `FetcherSession` and `StealthySession` classes for cookie and state management across requests.
- **Proxy Rotation**: Built-in `ProxyRotator` with cyclic or custom rotation strategies across all session types, plus per-request proxy overrides.
- **Domain & Ad Blocking**: Block requests to specific domains (and their subdomains) or enable built-in ad blocking (~3,500 known ad/tracker domains) in browser-based fetchers.
- **DNS Leak Prevention**: Optional DNS-over-HTTPS support to route DNS queries through Cloudflare's DoH, preventing DNS leaks when using proxies.
- **Remote Browsers**: Instead of launching a browser locally, connect to one that's already running through CDP with `cdp_url`, whether it's on the same machine, another host, or a managed browser provider. You can also point any browser fetcher at your own Chromium build with `executable_path`.
- **Background API Capture**: Enable `record_requests=True` on a browser session, then search its saved responses with `session.network.search(limit=None)`. Read API data and HTTP errors across page loads without sending requests again. History is bounded and saves text response bodies.
- **Async Support**: Complete as

## installation

Let's give you a quick glimpse of what Scrapling can do without deep diving.

## tools

HTTP requests with session support
```python
from scrapling.fetchers import Fetcher, FetcherSession

with FetcherSession(impersonate='chrome') as session:  # Use latest version of Chrome's TLS fingerprint
    page = session.get('https://quotes.toscrape.com/', stealthy_headers=True)
    quotes = page.css('.quote .text::text').getall()

# Or use one-off requests
page = Fetcher.get('https://quotes.toscrape.com/')
quotes = page.css('.quote .text::text').getall()
```
Advanced stealth mode
```python
from scrapling.fetchers import StealthyFetcher, StealthySession

with StealthySession(headless=True, solve_cloudflare=True) as session:  # Keep the browser open until you finish
    page = session.fetch('https://nopecha.com/demo/cloudflare', google_search=False)
    data = page.css('#padded_content a').getall()

# Or use one-off request style, it opens the browser for this request, then closes it after finishing
page = StealthyFetcher.fetch('https://nopecha.com/demo/cloudflare', solve_cloudflare=True)
data = page.css('#padded_content a').getall()
```
Full browser automation
```python
from scrapling.fetchers import StealthyFetcher, StealthySession

with StealthySession(headless=True, disable_resources=False, network_idle=True) as session:  # Keep the browser open until you finish
    page = session.fetch('https://quotes.toscrape.com/', load_dom=False)
    data = page.xpath('//span[@class="text"]/text()').getall()  # XPath selector if you prefer it

# Or use one-off request style, it opens the browser for this request, then closes it after finishing
page = StealthyFetcher.fetch('https://quotes.toscrape.com/')
data = page.css('.quote .text::text').getall()
```

### Spiders
Build full crawlers with concurrent requests, multiple session types, and pause/resume:
```python
from scrapling.spiders import Spider, Response

class QuotesSpider(Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]
    concurrent_requests = 10
    
    async def parse(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                "text": quote.css('.text::text').get(),
                "author": quote.css('.author::text').get(),
            }
            
        next_page = response.css('.next a')
        if next_page:
            yield response.follow(next_page[0].attrib['href'])

result = QuotesSpider().start()
print(f"Scraped {len(result.items)} quotes")
result.items.to_json("quotes.json")
```
Use multiple session types in a single spider:
```python
from scrapling.spiders import Spider, Request, Response
from scrapling.fetchers import FetcherSession, AsyncStealthySession

class MultiSessionSpider(Spider):
    name = "multi"
    start_urls = ["https://example.com/"]
    
    def configure_sessions(self, manager):
        manager.add("fast", FetcherSession(impersonate="chrome"))
        manager.add("stealth", AsyncStealthySession(headless=True), lazy=True)
    
    async def parse(self, response: Response):
        for link in response.css('a::attr(href)').getall():
            # Route protected pages through the stealth session
            if "protected" in link:
                yield Request(link, sid="stealth")
            else:
                yield Request(link, sid="fast", callback=self.parse)  # explicit callback
```
Pause and resume long crawls with checkpoints by running the spider like this:
```python
QuotesSpider(crawldir="./crawl_data").start()
```
With `crawldir` set, press Ctrl+C to save pending requests and seen URLs. Restart with the same `crawldir` to resume. Save scraped items separately.

Or skip writing the crawling logic altogether with the ready-made templates, like pulling an entire Shopify store's catalog:
```python
from scrapling.spiders import ShopifySpider

class MyStore(ShopifySpider):
    target_website = "example.com"

result = MyStore().start()  # Every product in the store, one item per variant
```
The template reads products exposed through public collection endpoin

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
   - Install dependencies for ([building RAG systems](https://scrapling.readthedocs.io/en/latest/ai/building-rag-systems.html)):
       ```bash
       pip install "scrapling[rag]"
       ```
   - Install shell features (Web Scraping shell and the `extract` command): 
       ```bash
       pip install "scrapling[shell]"
       ```
   - Install everything: 
       ```bash
       pip install "scrapling[all]"
       ```
   Run `scrapling install` when you need browser fetchers. HTTP requests do not need a browser installation.

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
    note = {A Python Web Scraping framework for everything from a single request to a full-scale crawl!}
  }
```

## License

This work is licensed under the BSD-3-Clause License.

## Acknowledgments

This project includes code adapted from:
- Parsel (BSD License)-Used for [translator](https://github.com/D4Vinci/Scrapling/blob/main/scrapling/core/translator.py) submodule

---
<div align="center"><small>Designed & crafted with ❤️ by Karim Shoair.</small></div><br>
