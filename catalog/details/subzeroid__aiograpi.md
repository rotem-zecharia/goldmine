# subzeroid/aiograpi

⚡ Asynchronous Python library for Instagram Private API 2026

## tools

> ⚠️ **Telegram support group moved to https://t.me/aiograpi_support** — the previous `@instagrapi` group has been restricted by Meta and is no longer maintained.

If you want to work with aiograpi (business interests), we strongly advise you to prefer [HikerAPI](https://hikerapi.com/p/KhMxYMSn) project.
However, you won't need to spend weeks or even months setting it up.
The best service available today is [HikerAPI](https://hikerapi.com/p/KhMxYMSn), which handles 4–5 million daily requests, provides support around-the-clock, and offers partners a special rate.
In many instances, our clients tried to save money and preferred aiograpi, but in our experience, they ultimately returned to [HikerAPI](https://hikerapi.com/p/KhMxYMSn) after spending much more time and money.
It will be difficult to find good accounts, good proxies, or resolve challenges, and IG will ban your accounts.

The aiograpi more suits for testing or research than a working business!

Video uploads can use a built-in MP4 metadata parser when you provide `thumbnail=...`. Automatic thumbnail generation, `StoryBuilder`, and video/audio composition still need the optional video dependencies, MoviePy `2.2.1`, and executable `ffmpeg`:

```bash
pip install "aiograpi[video]"
pip install --no-deps "moviepy==2.2.1"
```

MoviePy `2.2.1` currently declares `Pillow<12`, but aiograpi keeps `Pillow>=12.3.0` for security fixes; the `--no-deps` install keeps the safe Pillow version. If your project imports MoviePy directly, migrate any MoviePy `1.x` code from `moviepy.editor`, `set_*`, `resize`, and `subclip` APIs to the MoviePy `2.x` API before upgrading.

Android users should see [Pydroid and ffmpeg](docs/usage-guide/pydroid.md) and [Termux](docs/usage-guide/termux.md).

### We recommend using our services:

* [LamaTok](https://lamatok.com/p/X0HatoxX) for TikTok API 🔥
* [HikerAPI](https://hikerapi.com/p/KhMxYMSn) for Instagram API ⚡⚡⚡
* [DataLikers](https://datalikers.com/p/XPhrh0Y3) for Instagram Datasets 🚀

[![PyPI](https://img.shields.io/pypi/v/aiograpi)](https://pypi.org/project/aiograpi/)
[![Python](https://img.shields.io/pypi/pyversions/aiograpi)](https://pypi.org/project/aiograpi/)
[![License](https://img.shields.io/pypi/l/aiograpi)](LICENSE)
[![Package](https://github.com/subzeroid/aiograpi/actions/workflows/python-package.yml/badge.svg)](https://github.com/subzeroid/aiograpi/actions/workflows/python-package.yml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://subzeroid.github.io/aiograpi/latest/)
[![SemVer](https://img.shields.io/badge/semver-1.2.0-blue)](https://semver.org/spec/v2.0.0.html)


Features:

* Getting public data of user, posts, stories, highlights, followers and following users
* Getting public email and phone number, if the user specified them in his business profile
* Getting public data of post, story, album, Reels, IGTV data and the ability to download content
* Getting public data of hashtag and location data, as well as a list of posts for them
* Getting public data of all comments on a post and a list of users who liked it
* Management of proxy servers, mobile devices and challenge resolver
* Login by username and password, sessionid, 2FA, 8-digit backup codes, and Bloks 2FA fallback/helpers
* Managing messages, reactions and threads for Direct and attach files
* Experimental Realtime MQTT/MQTToT for Direct message sync, lightweight Direct actions, and FBNS push callbacks
* Download and upload a Photo, Video, IGTV, Reels, Albums, Stories and Trial Reels
* Work with Users, Posts, Comments, Insights, Collections, Location, Hashtag and account notification settings
* Insights by account, posts and stories
* Like, following, commenting, editing account (Bio) and much more else

-----

Asynchronous Instagram Private API wrapper without selenium. Use the most recent version of the API from Instagram, which was obtained using reverse-engineering with Charles Proxy and [Proxyman](https://proxyman.io/).

Support **Python >= 3.10**

F

## features

1. Performs [Web API](https://subzeroid.github.io/aiograpi/latest/usage-guide/fundamentals/) or [Mobile API](https://subzeroid.github.io/aiograpi/latest/usage-guide/fundamentals/) requests depending on the situation (to avoid Instagram limits)
2. [Login](https://subzeroid.github.io/aiograpi/latest/usage-guide/interactions/) by username and password, including 2FA, 8-digit backup codes, [Bloks 2FA](https://subzeroid.github.io/aiograpi/latest/usage-guide/totp/#bloks-two-factor-flow) fallback/helpers, and by sessionid (and uses Authorization header instead Cookies)
3. [Challenge Resolver](https://subzeroid.github.io/aiograpi/latest/usage-guide/challenge_resolver/) have Email and SMS handlers
4. Support [upload](https://subzeroid.github.io/aiograpi/latest/usage-guide/media/) a Photo, Video, IGTV, Reels, Albums and Stories
5. Support work with [User](https://subzeroid.github.io/aiograpi/latest/usage-guide/user/), [Media](https://subzeroid.github.io/aiograpi/latest/usage-guide/media/), [Comment](https://subzeroid.github.io/aiograpi/latest/usage-guide/comment/), [Insights](https://subzeroid.github.io/aiograpi/latest/usage-guide/insight/), [Collections](https://subzeroid.github.io/aiograpi/latest/usage-guide/collection/), [Location](https://subzeroid.github.io/aiograpi/latest/usage-guide/location/) (Place), [Hashtag](https://subzeroid.github.io/aiograpi/latest/usage-guide/hashtag/) and [Direct Message](https://subzeroid.github.io/aiograpi/latest/usage-guide/direct/) objects
6. [Like](https://subzeroid.github.io/aiograpi/latest/usage-guide/media/), [Follow](https://subzeroid.github.io/aiograpi/latest/usage-guide/user/), [Edit account](https://subzeroid.github.io/aiograpi/latest/usage-guide/account/) (Bio) and much more else
7. [Insights](https://subzeroid.github.io/aiograpi/latest/usage-guide/insight/) by account, posts and stories
8. [Build stories](https://subzeroid.github.io/aiograpi/latest/usage-guide/story/) with custom background, font animation, link sticker and mention users
9. [Realtime MQTT](https://subzeroid.github.io/aiograpi/latest/usage-guide/realtime/) for Direct message sync, lightweight Direct MQTT actions, and FBNS push notifications
10. Account [registration](https://github.com/subzeroid/aiograpi/blob/main/aiograpi/mixins/signup.py) and captcha passing will appear

### Versioning policy

Starting with `1.0.0`, aiograpi follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
for the Python library API surface. Instagram's private API still rotates
`doc_id`s, deprecates endpoints, and changes response shapes without notice, so
`1.0.0` is not a promise that every Instagram-side flow will stay stable forever.

What you can rely on instead:

- **Breaking library API changes use major releases** when they are under our control.
- **Instagram-driven endpoint removals are flagged in the [CHANGELOG](https://github.com/subzeroid/aiograpi/blob/main/CHANGELOG.md)** with migration notes.
- **Deprecated methods stay around for ≥2 minor releases** with
  `DeprecationWarning` before removal — you'll get loud warnings, not
  surprise `AttributeError`s.
- **Live CI smoke** runs on every push: `tests/live/smoke.py` against a
  real account through a real proxy. If we ship something that breaks
  the basic happy path, CI catches it.
- **Migration Guide** at [docs/migration.md](https://subzeroid.github.io/aiograpi/latest/migration/) — breaking changes are documented with before/after examples.

### What's new in 1.0.0 and recent releases

- **1.3.0 upstream sync** — synced through `instagrapi 2.9.0`, adding experimental modern CAA email signup via `signup_caa_email(...)`, the mobile `graphql_www` Bloks app wrapper, and per-request private headers/domain routing for Bloks calls.
- **1.2.x upstream sync** — synced through `instagrapi 2.8.19`, adding Direct media share to existing threads, clearer Direct message request privacy errors, private-first high-level user/media/story lookups, sessionid username recovery via private stre

## installation

```
pip install aiograpi
```

Optional public web TLS impersonation support is available as an extra:

```bash
pip install "aiograpi[curl]"
```

Use it only for public web endpoints that are sensitive to browser TLS fingerprints:

```python
cl = Client(public_transport="curl", public_transport_impersonate="chrome136")
```

See the [public transport guide](docs/usage-guide/public-transport.md) for live comparison results and caveats.

TLS certificate verification is enabled by default. For a trusted debugging MITM proxy, prefer `Client(tls_verify="/path/to/proxy-ca.pem")`; use `Client(tls_verify=False)` only for temporary local debugging because it allows session interception.

### Realtime MQTT and Direct

`aiograpi 1.1.0` adds experimental async Realtime MQTT/MQTToT helpers. They can receive Direct message sync payloads,
publish lightweight Direct actions over MQTT, and subscribe to FBNS push notifications.

```python
from aiograpi import Client

cl = Client()
await cl.login(USERNAME, PASSWORD)


def handle_message(payload):
    print(payload)


cl.realtime_on("message", handle_message)
rt = await cl.realtime_connect()
await rt.direct_subscribe()

await rt.direct_send_text(thread_id, "Hello from MQTT")

while True:
    await cl.realtime_read_once()
```

See the [Realtime MQTT guide](docs/usage-guide/realtime.md) for Direct sync, MQTT Direct actions, and FBNS push examples.
