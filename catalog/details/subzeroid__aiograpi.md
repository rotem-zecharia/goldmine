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
