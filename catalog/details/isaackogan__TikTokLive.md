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

## installation

Install the TikTok LIVE API client for Python via pip from the [PyPi](https://pypi.org/project/TikTokLive/) repository:

```shell script
pip install TikTokLive
```

Then create your first real-time TikTok LIVE chat connection:

```python
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent
