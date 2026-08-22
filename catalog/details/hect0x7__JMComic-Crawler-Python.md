# hect0x7/JMComic-Crawler-Python

Python API for JMComic / 提供Python API访问禁漫天堂，同时支持网页端和移动端 / 禁漫天堂GitHub Actions下载器🚀

## tools

import asyncio
asyncio.run(jmcomic.download_album_async('123'))
```

上面的 `download_album`方法还有一个参数`option`，可用于控制下载配置，配置包括禁漫域名、网络代理、图片格式转换、插件等等。

你可能需要这些配置项。推荐使用配置文件创建option，用option下载本子，见下章：
