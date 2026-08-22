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

## installation

```bash
pip install pydoll-python
```

No WebDriver binaries or external dependencies required.

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
