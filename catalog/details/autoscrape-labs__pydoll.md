# autoscrape-labs/pydoll

Pydoll is a library for automating chromium-based browsers without a WebDriver, offering realistic interactions.

## features

- **Fingerprint injection**: Make the browser report a fully consistent identity with [`tab.apply_fingerprint()`](#2-fingerprint-injection): User-Agent, Client Hints, `navigator`, WebGL, canvas, screen, fonts, timezone and locale, all aligned. The injected overrides survive `toString` and prototype introspection and propagate into Web Workers, so lie-detection checks like CreepJS's don't flag them.
- **Humanized interactions**: [Mouse movement](https://pydoll.tech/docs/guides/mouse/) along Bezier curves, realistic typing, and scroll physics. Often enough to pass behavioral challenges like Cloudflare Turnstile or reCAPTCHA v3, depending on your browser and IP reputation.
- **Zero WebDrivers**: A direct CDP connection over WebSocket. No driver binary, no `navigator.webdriver` flag, no version-matching headaches.
- **Async and typed**: Built on `asyncio`, type-checked with `mypy`. Full IDE autocompletion and static error checking.
- **Network control**: [Intercept](https://pydoll.tech/docs/guides/request-interception/) requests to block ads/trackers, [monitor](https://pydoll.tech/docs/guides/network-monitoring/) traffic for API discovery, and make [authenticated HTTP requests](https://pydoll.tech/docs/guides/http-requests/) that inherit the browser session.
- **Shadow DOM and iframes**: Full support for [shadow roots](https://pydoll.tech/docs/guides/dom-traversal/#shadow-dom) (including closed) and cross-origin iframes. Discover, query, and interact with elements inside them using the same API.
- **Structured extraction**: Define a [Pydantic](https://docs.pydantic.dev/) model, call `tab.extract()`, and get typed, validated data back. No manual element-by-element querying.

> [!NOTE]
> **A word from the maintainer.** Pydoll is currently maintained by a single person, and I'm a bit stretched at the moment, so new releases and replies to issues may take a little longer than usual. To be clear: **the project is not dead, and it is not going anywhere.** Development continues; it's just moving at a calmer pace for now.
>
> **A goal to aim for:** once the project reaches **10k stars**, I plan to ship **Firefox support**, a big step that opens up a whole new range of possibilities for the library. Momentum like that is exactly the kind of incentive that makes a feature this large worth taking on, so if you'd like to see it happen, that's the push it needs.

### Top Sponsors

<table>
  <tr>
    <td width="300" align="center" valign="middle">
      <a href="https://substack.thewebscraping.club/p/pydoll-webdriver-scraping?utm_source=github&utm_medium=repo&utm_campaign=pydoll"><img src="public/images/banner-the-webscraping-club.png" width="280" alt="The Web Scraping Club" /></a>
    </td>
    <td valign="middle">
      <b><a href="https://substack.thewebscraping.club/p/pydoll-webdriver-scraping?utm_source=github&utm_medium=repo&utm_campaign=pydoll">The Web Scraping Club</a></b><br />
      <sub>The #1 newsletter dedicated to web scraping. Read their full, independent review of Pydoll.</sub>
    </td>
  </tr>
  <tr>
    <td width="300" align="center" valign="middle">
      <a href="https://go.nodemaven.com/pydollaugust"><img src="public/images/nodemaven-banner.png" width="280" alt="NodeMaven" /></a>
    </td>
    <td valign="middle">
      <b><a href="https://go.nodemaven.com/pydollaugust">NodeMaven</a></b><br />
      <sub>The most efficient proxy provider for web scraping and automation: ZIP targeting, 99.9% uptime, filtered high-quality IPs, no KYC. Use <code>PYDOLL35</code> for 35% off Mobile &amp; Residential, or <code>PYDOLL40</code> for 40% off ISP (Static) proxies.</sub>
    </td>
  </tr>
  <tr>
    <td width="300" align="center" valign="middle">
      <a href="https://niuproxy.com/?utm_source=pydoll&utm_medium=pydoll&ref=pydoll"><img src="public/images/niuproxy-banner.png" width="280" alt="NiuProxy" /></a>
    </td>
    <td valign="middle">
      <b><a href="https://niuproxy.com/?utm_source=pydoll&utm_medium=pydoll&ref=pydoll">NiuPro

## installation

```bash
pip install pydoll-python
```

No WebDriver binaries or external dependencies required.

## Getting Started

### 1. Stealthy Automation

The imperative API handles the basics: start a browser, navigate, find elements, and interact with them. Pass `humanize=True` to add human-like timing for anti-bot evasion.

```python
import asyncio

from pydoll.browser import Chrome
from pydoll.constants import Key

async def google_search(query: str):
    async with Chrome() as browser:
        tab = await browser.start()
        await browser.set_window_maximized()
        tab.mouse.debug = True
        await tab.go_to('https://www.google.com')
        # Find elements and interact with human-like timing
        search_box = await tab.find(tag_name='textarea', name='q')
        await search_box.type_text(query, humanize=True)
        await tab.keyboard.press(Key.ENTER)

        first_result = await tab.find(
            tag_name='h3',
            text='autoscrape-labs/pydoll',
            timeout=10,
        )
        await first_result.click(humanize=True)
        await asyncio.sleep(5)
        print(f"Page loaded: {await tab.title}")

asyncio.run(google_search('pydoll site:github.com'))
```

<p align="center">
  <img width="100%" alt="Pydoll running a humanized Google search: mouse curves to the box, types, and clicks the result" src="public/images/humanized-google-search.gif" />
</p>

### 2. Fingerprint Injection

Pydoll can also make the browser *report* a different identity. `tab.apply_fingerprint()` overrides the surface that fingerprinting scripts read (User-Agent and Client Hints, `navigator`, WebGL, canvas, screen, fonts, timezone and locale) and keeps those values consistent with each other.

Spoofing a fingerprint is less about changing the values than about not getting caught changing them. Modern anti-bot scripts inspect *how* a property was defined: a naive `Object.defineProperty` leaves a fake `toString`, an own-property where a prototype getter should be, or an override that a phantom `iframe` or a Web Worker can see straight through. Pydoll handles this: injected getters read as native under `toString` and prototype introspection, and the same identity is replayed inside dedicated, shared and service workers.

It also neutralizes the **headless** tells, chiefly the SwiftShader WebGL renderer that gives away a GPU-less browser, so `headless=True` is no longer an automatic giveaway. That is what lets a plain Google search run in headless mode. (Cloudflare Turnstile in headless is still under study.)

```python
import asyncio

from pydoll.browser.chromium import Chrome

from examples.fingerprints import FINGERPRINTS

async def spoof_fingerprint():
    async with Chrome() as browser:
        tab = await browser.start()

        # Apply before navigating: the JS overrides register on every new document.
        await tab.apply_fingerprint(FINGERPRINTS['windows11_rtx3060_nyc'])

        await tab.go_to('https://abrahamjuliot.github.io/creepjs/')
        print('Fingerprint applied.')
        await asyncio.sleep(5)

asyncio.run(spoof_fingerprint())
```

In our testing it passed each of these fingerprint and bot-detection suites without being flagged:

| Test site | What it checks | Result |
| --- | --- | --- |
| [CreepJS](https://abrahamjuliot.github.io/creepjs/) | Lie detection, prototype / `toString` tampering, workers, fonts | No detection |
| [SannySoft](https://bot.sannysoft.com/) | Headless and bot signals | No detection |
| [BrowserScan](https://www.browserscan.net/bot-detection) | Bot-detection suite | No detection |
| [BrowserLeaks WebGL](https://browserleaks.com/webgl) | WebGL vendor / renderer / hash | No detection |
| [BrowserLeaks JavaScript](https://browserleaks.com/javascript) | `navigator` / JS environment | No detection |
| [BrowserLeaks Canvas](https://browserleaks.com/canvas) | Canvas fingerprint | No detection |
| [BrowserLeaks WebRTC](https://browserleaks.com/webrtc) | WebRTC IP leak | No detection |

*

## tools

response = await tab.request.get('https://my-site.com/api/user/profile')
user_data = response.json()
```
[Hybrid Automation Docs](https://pydoll.tech/docs/guides/http-requests/)
</details>

<details>
<summary><b>Network Interception and Monitoring</b></summary>
<br>

Monitor traffic for API discovery or intercept requests to block ads, trackers, and unnecessary resources.

```python
import asyncio
from pydoll.browser.chromium import Chrome
from pydoll.protocol.fetch.events import FetchEvent, RequestPausedEvent
from pydoll.protocol.network.types import ErrorReason

async def block_images():
    async with Chrome() as browser:
        tab = await browser.start()

        async def block_resource(event: RequestPausedEvent):
            request_id = event['params']['requestId']
            resource_type = event['params']['resourceType']

            if resource_type in ['Image', 'Stylesheet']:
                await tab.fail_request(request_id, ErrorReason.BLOCKED_BY_CLIENT)
            else:
                await tab.continue_request(request_id)

        await tab.enable_fetch_events()
        await tab.on(FetchEvent.REQUEST_PAUSED, block_resource)

        await tab.go_to('https://example.com')
        await asyncio.sleep(3)
        await tab.disable_fetch_events()

asyncio.run(block_images())
```
[Network Monitoring](https://pydoll.tech/docs/guides/network-monitoring/) | [Request Interception](https://pydoll.tech/docs/guides/request-interception/)
</details>

<details>
<summary><b>Browser Fingerprint Control</b></summary>
<br>

Granular control over [browser preferences](https://pydoll.tech/docs/guides/browser-preferences/): hundreds of internal Chrome settings for building consistent fingerprints.

```python
options = ChromiumOptions()

options.browser_preferences = {
    'profile': {
        'default_content_setting_values': {
            'notifications': 2,
            'geolocation': 2,
        },
        'password_manager_enabled': False
    },
    'intl': {
        'accept_languages': 'en-US,en',
    },
    'browser': {
        'check_default_browser': False,
    }
}
```
[Browser Preferences Guide](https://pydoll.tech/docs/guides/browser-preferences/)
</details>

<details>
<summary><b>Concurrency, Contexts and Remote Connections</b></summary>
<br>

Manage [multiple tabs](https://pydoll.tech/docs/guides/tabs/) and [browser contexts](https://pydoll.tech/docs/guides/browser-contexts/) (isolated sessions) concurrently. Connect to browsers running in Docker or remote servers.

```python
async def scrape_page(url, tab):
    await tab.go_to(url)
    return await tab.title

async def concurrent_scraping():
    async with Chrome() as browser:
        tab_google = await browser.start()
        tab_ddg = await browser.new_tab()

        results = await asyncio.gather(
            scrape_page('https://google.com/', tab_google),
            scrape_page('https://duckduckgo.com/', tab_ddg)
        )
        print(results)
```
[Multi-Tab Management](https://pydoll.tech/docs/guides/tabs/) | [Remote Connections](https://pydoll.tech/docs/guides/remote-connections/)
</details>

<details>
<summary><b>Retry Decorator</b></summary>
<br>

The `@retry` decorator supports custom recovery logic between attempts (e.g., refreshing the page, rotating proxies) and exponential backoff.

```python
from pydoll.decorators import retry
from pydoll.exceptions import ElementNotFound, NetworkError

@retry(
    max_retries=3,
    exceptions=[ElementNotFound, NetworkError],
    on_retry=my_recovery_function,
    exponential_backoff=True
)
async def scrape_product(self, url: str):
    # scraping logic
    ...
```
[Retry Decorator Docs](https://pydoll.tech/docs/guides/retrying/)
</details>

---

## Contributing

Contributions are welcome, whether that is a bug report, a docs fix, or a new feature. If you are not sure where to start, open an issue and we can figure it out together. [CONTRIBUTING.md](CONTRIBUTING.md) has the dev setup, how to run the tests, and the co
