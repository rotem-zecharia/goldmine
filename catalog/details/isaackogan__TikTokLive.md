# isaackogan/TikTokLive

TikTok LIVE API for Python: The definitive 3rd-party library to receive livestream events (comments, gifts, etc.) in realtime from TikTok LIVE.

## tools

TikTok LIVE API (TikTokLive) is the #1 TikTok LIVE client for **Python**. Connect to any [TikTok LIVE](https://www.tiktok.com/live) stream and receive **real-time chat messages, gifts, likes, follows, shares, viewer counts, battles, and more** using just a creator's `@unique_id`. No login, no credentials or app are required.

TikTokLive is the definitive third-party Python library for reading the TikTok LIVE websocket, building TikTok chat bots, gift trackers, live stream overlays, alerts, and analytics tools.

[![Discord](https://img.shields.io/discord/977648006063091742?logo=discord&label=TikTokLive%20Discord&labelColor=%23171717&color=%231877af)](https://discord.gg/N3KSxzvDX8)
![Live TikTok LIVE API connections](https://api.eulerstream.com/analytics/pips)
![TikTokLive PyPI downloads](https://pepy.tech/badge/tiktoklive)
![TikTokLive GitHub stars](https://img.shields.io/github/stars/isaackogan/TikTokLive?style=flat&color=0274b5)
![TikTokLive GitHub forks](https://img.shields.io/github/forks/isaackogan/TikTokLive?style=flat&color=0274b5)
![TikTokLive open issues](https://img.shields.io/github/issues/isaackogan/TikTokLive)

> **Note:** This is <strong>not</strong> a production-ready API. It is a reverse engineering project. Use the [WebSocket API](https://www.eulerstream.com/websockets) for production by [Euler Stream](https://www.eulerstream.com/).

## What Can You Build With the TikTok LIVE API?

- **TikTok live chat readers** and chat bots that respond to comments in real time
- **Gift trackers and donation alerts** for TikTok LIVE streamers (with streak handling)
- **OBS overlays and stream widgets** driven by live TikTok events
- **TikTok LIVE analytics**: viewer counts, likes, follows, battle (PK) scores
- **Moderation tools** that react to deleted messages and room events
- **Text-to-speech (TTS) readers** and interactive livestream games

## TikTok LIVE API for Production

<table>
<tr>
    <td><br/><img width="180px" style="border-radius: 10px" alt="Euler Stream TikTok LIVE API logo" src="https://raw.githubusercontent.com/isaackogan/TikTokLive/master/.github/SquareLogo.png"><br/><br/></td>
    <td>
        <a href="https://www.eulerstream.com/">
            <strong>Euler Stream</strong> offers a comprehensive TikTok LIVE API, WebSocket Server, CAPTCHA Solutions and much more!
        </a>
    </td>
</tr>
</table>

## Table of Contents

- [Getting Started](#getting-started)
    - [Parameters](#parameters)
    - [Methods](#methods)
    - [Properties](#properties)
    - [WebDefaults](#webdefaults)
- [Events](#events)
- [Documentation](https://isaackogan.github.io/TikTokLive/)
- [Other Languages](#tiktok-live-api-in-other-languages-nodejs-java-c-go-rust)
- [Community](#community)
- [Examples](https://github.com/isaackogan/TikTokLive/tree/master/examples)
- [FAQ](#frequently-asked-questions)
- [Licensing](#license)
- [Star History](#star-history)
- [Contributors](#contributors)

## Community

Join the [TikTokLive discord](https://discord.gg/e2XwPNTBBr) and visit
the [`#py-support`](https://discord.gg/uja6SajDxd)
channel for questions, contributions and ideas.

## installation

Install the TikTok LIVE API client for Python via pip from the [PyPi](https://pypi.org/project/TikTokLive/) repository:

```shell script
pip install TikTokLive
```

Then create your first real-time TikTok LIVE chat connection:

```python
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@isaackogz")


# Listen to an event with a decorator!
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to @{event.unique_id} (Room ID: {client.room_id}")


# Or, add it manually via "client.add_listener()"
async def on_comment(event: CommentEvent) -> None:
    print(f"{event.user.nickname} -> {event.comment}")


client.add_listener(CommentEvent, on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
```

For more quickstart examples, including a TikTok live chat reader, gift tracker, and live status checker, see the [examples folder](https://github.com/isaackogan/TikTokLive/tree/master/examples) provided in the source tree.
