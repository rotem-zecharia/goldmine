# subzeroid/instagrapi

🔥 The fastest and powerful Python library for Instagram Private API 2026 with HikerAPI SaaS

## tools

> ⚠️ **Telegram support group moved to [aiograpi_support](https://t.me/aiograpi_support)** — the previous `@instagrapi` group has been restricted by Meta and is no longer maintained.

[![PyPI](https://img.shields.io/pypi/v/instagrapi)](https://pypi.org/project/instagrapi/)
[![Python](https://img.shields.io/pypi/pyversions/instagrapi)](https://pypi.org/project/instagrapi/)
[![License](https://img.shields.io/pypi/l/instagrapi)](LICENSE)
[![Package](https://github.com/subzeroid/instagrapi/actions/workflows/python-package.yml/badge.svg)](https://github.com/subzeroid/instagrapi/actions/workflows/python-package.yml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://subzeroid.github.io/instagrapi/)

Fast and effective unofficial Instagram API wrapper for Python.

`instagrapi` combines public web and private mobile API flows, supports session persistence and challenge handling, and covers the main automation primitives for users, media, stories, direct messages, notes, locations, comments, insights, and uploads.

Private API automation is fragile in production because account trust, proxies, device state, challenges, and rate limits can change independently of the library.
For account-owned business workflows, prefer official Instagram APIs where they cover your use case.
For production private API infrastructure, a hosted provider such as [HikerAPI](https://hikerapi.com/) may be a better fit than maintaining accounts, proxies, and challenge handling yourself.

The instagrapi project is best suited for testing, research, and controlled internal automation.

✨ [aiograpi - Asynchronous Python library for Instagram Private API](https://github.com/subzeroid/aiograpi) ✨

Support **Python 3.10+**

`Python 3.9` support was dropped in `2.5.0`. Upstream security patches for Pillow `12.x` and pytest `9.x` are not backported to `Python 3.9`, leaving conditional pins permanently exposed to known CVEs. Users who need `Python 3.9` should pin to `instagrapi==2.4.5`.

## installation

```bash
pip install instagrapi
```

Optional public web TLS impersonation support is available as an extra:

```bash
pip install "instagrapi[curl]"
```

Use it only for public web endpoints that are sensitive to browser TLS fingerprints:

```python
cl = Client(public_transport="curl", public_transport_impersonate="chrome136")
```

See the [public transport guide](docs/usage-guide/public-transport.md) for live comparison results and caveats.

TLS certificate verification is enabled by default. For a trusted debugging MITM proxy, prefer `Client(tls_verify="/path/to/proxy-ca.pem")`; use `Client(tls_verify=False)` only for temporary local debugging because it allows session interception.

If your project uses [uv](https://docs.astral.sh/uv/), you can add the package with:

```bash
uv add instagrapi
```

Or install it into the active virtual environment:

```bash
uv pip install instagrapi
```

Video uploads can use a built-in MP4 metadata parser when you provide `thumbnail=...`. Automatic thumbnail generation, `StoryBuilder`, and video/audio composition still need the optional video dependencies, MoviePy `2.2.1`, and executable `ffmpeg`:

```bash
pip install "instagrapi[video]"
pip install --no-deps "moviepy==2.2.1"
```

MoviePy `2.2.1` currently declares `Pillow<12`, but instagrapi keeps `Pillow>=12.2.0` for security fixes; the `--no-deps` install keeps the safe Pillow version. If your project imports MoviePy directly, migrate any MoviePy `1.x` code from `moviepy.editor`, `set_*`, `resize`, and `subclip` APIs to the MoviePy `2.x` API before upgrading.

Android users should see [Pydroid and ffmpeg](docs/usage-guide/pydroid.md) and [Termux](docs/usage-guide/termux.md).

## Quick Start

``` python
from instagrapi import Client

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
medias = cl.user_medias(user_id, 20)
```

## features

* Uses [Web API](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html) and [Mobile API](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html) flows where available
* Supports login by password, 2FA, 8-digit backup codes, `sessionid`, and [Bloks 2FA](https://subzeroid.github.io/instagrapi/usage-guide/totp.html#bloks-two-factor-flow) fallback/helpers for newer verification flows
* Includes email/SMS-based [challenge resolver](https://subzeroid.github.io/instagrapi/usage-guide/challenge_resolver.html) hooks
* Uploads and downloads photos, videos, albums, IGTV, reels, and stories
* Works with users, media, comments, locations, hashtags, collections, notes, direct messages, and insights
* Exposes account notification setting helpers with typed notification categories
* Supports story building with mentions, hashtags, link stickers, and media stickers
* Includes helpers for current location search and Direct message workflows
* Supports mobile follower sorting with `date_followed_latest` and `date_followed_earliest`
* App-side discovery surfaces: `chaining`, `fetch_suggestion_details`, `discover_recommended_accounts_for_category_v1`, `user_stream_*`, `user_web_profile_info_v1`
* v2 search SERPs: `media_search`, `fbsearch_accounts_v2`, `fbsearch_reels_v2`, `fbsearch_topsearch_v2`, `fbsearch_typehead`
* Alternative media-info path (`media_info_v2`) for ad-tagged / sponsored media that the canonical endpoint refuses
* Experimental Realtime MQTT helpers for live events, Direct message sync, lightweight Direct actions, and FBNS push callbacks

Anonymous/public web paths are best treated as opportunistic rather than guaranteed. Instagram can change or restrict them independently of the library, so production-grade workflows should prefer authenticated sessions.

## Documentation And Support

API reference and full usage guide live at [subzeroid.github.io/instagrapi](https://subzeroid.github.io/instagrapi/):

* [Documentation index](https://subzeroid.github.io/instagrapi/)
* [Getting Started](https://subzeroid.github.io/instagrapi/getting-started.html)
* [Usage Guide](https://subzeroid.github.io/instagrapi/usage-guide/fundamentals.html)
* [Interactions reference](https://subzeroid.github.io/instagrapi/usage-guide/interactions.html)
* [Best Practices](https://subzeroid.github.io/instagrapi/usage-guide/best-practices.html) for sessions, proxies, and anti-abuse handling
* [Handle Exceptions](https://subzeroid.github.io/instagrapi/usage-guide/handle_exception.html) for centralizing `429`, challenge, and relogin logic
* [GitHub Discussions](https://github.com/subzeroid/instagrapi/discussions)
* Support chat in Telegram: [aiograpi_support](https://t.me/aiograpi_support) — the previous `@instagrapi` group was restricted by Meta and is no longer maintained

For other languages, consider [instagrapi-rest](https://github.com/subzeroid/instagrapi-rest). For async Python, see [aiograpi](https://github.com/subzeroid/aiograpi).

## Tutorials

Hands-on guides for real instagrapi work — login flows, sessions, proxies, scraping, posting, error handling — live at [instagrapi.com/guides](https://instagrapi.com/guides/):

* [Instagram Private API in Python](https://instagrapi.com/guides/instagram-private-api-python/) — pillar walkthrough: login, sessions, fetching, posting
* [2FA and `challenge_required`](https://instagrapi.com/guides/instagrapi-2fa-challenge/)
* [Session persistence: file, Redis, and Postgres patterns](https://instagrapi.com/guides/instagrapi-session-persistence/)
* [Configuring proxies (HTTP, SOCKS5, residential)](https://instagrapi.com/guides/instagrapi-proxy-setup/)
* [Instagram scraper in Python: a working setup](https://instagrapi.com/guides/instagram-scraper-python/)
* [Upload a photo from Python](https://instagrapi.com/guides/instagrapi-upload-photo-python/)
* [Download Instagram stories](https://instagrapi.com/guides/instagrapi-download-stories-python/)
* [Common errors reference](https://instagrapi.co
