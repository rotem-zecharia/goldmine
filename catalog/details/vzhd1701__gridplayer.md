# vzhd1701/gridplayer

Play videos side-by-side

## features

- Cross-platform (Linux, Mac, and Windows)
- Support for any video and audio format (VLC)
- Support for (almost) any streaming
  URLs ([streamlink](https://streamlink.github.io/plugins.html) + [yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md))
- Hardware & software video decoding
- Control video aspect, playback speed, zoom
- Set loop fragments with frame percision
- Configurable grid layout
- Easy swap videos with drag-n-drop
- Playlist retains settings for each video

## installation

```shell
uv tool install gridplayer
```

**Python 3.10 or later required.**

This type of installation will also require VLC installed (Windows & Mac) or a `vlc` package (Linux) present in your
system.
Please refer to [VLC official page](https://www.videolan.org/vlc/) for instructions on how to install it.

Some distros (e.g. Ubuntu) might also require `libxcb-xinerama0` package.
