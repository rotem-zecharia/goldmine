# xuejianxianzun/PixivBatchDownloader

Powerful Pixiv batch downloader. Batch download artworks and novels, filter works, rename when downloading, convert animated images, and more. 浏览器扩展程序，批量下载 Pixiv 上的插画和小说。过滤作品、下载时重命名、转换动态图片等。

## installation

Browsers with Chromium core, such as Chrome and Edge, can install this extension from the **[Chrome Web Store](https://chrome.google.com/webstore/detail/powerful-pixiv-downloader/dkndmhgdcmjdmkdonmbgjpijejdcilfh)**.

Firefox browsers can install this extension from **[Add-Ons](https://addons.mozilla.org/firefox/addon/powerfulpixivdownloader/)**.

# Offline Installation

Please check the Wiki page:
[Offline Installation](https://xuejianxianzun.github.io/PBDWiki/#/en/Installation/OfflineInstallation)

If you want to use this extension on Android, please check the Wiki page:
[Install on Microsoft Edge Canary Browser](https://xuejianxianzun.github.io/PBDWiki/#/en/Installation/MicrosoftEdgeCanary)

# How to use

This downloader runs on Pixiv.net pages. When you browse Pixiv, you can open the downloader panel at any time to batch download the works on the current page.

# Wiki

[View Wiki](https://xuejianxianzun.github.io/PBDWiki/#/en/Introduction)

# Patreon

<a href='https://www.patreon.com/xuejianxianzun'><img src='https://c5.patreon.com/external/logo/become_a_patron_button.png' alt='Become a patron' width='140px' /></a>

Thank you for your support!

# Thanks

- Thanks [道滿](https://zhtw.me/) , [VHlqg](https://github.com/VHlqg) for translating traditional Chinese.

- Thanks [光の軌跡](https://github.com/jiaer24) for translating traditional Japanese.

- Thanks [bropines](https://github.com/bropines) for translating traditional Russia.

- Thanks [KOZ39](https://github.com/KOZ39) for translating traditional Korean.

- Thanks [z2n](https://github.com/z2n) for improvements to the program.

# Development

1. This tool needs to be installed Node.JS first during development.

2. Clone this project (or fork first) and install dependencies:

```
git clone https://github.com/xuejianxianzun/PixivBatchDownloader.git

cd ./PixivBatchDownloader

npm i
```

So far, the initialization is complete.

You can load the `dist` folder as an extension in the extension management of your browser for local debugging.

-----------

The npm command of this project:

```
npm run ts // compile ts file to dist folder
npm run less // compile less files to the dist folder
npm run fmt // format all files

npm run pre-build // execute fmt, ts, less commands (compile all code, but do not package)

npm run build // execute fmt, ts, less commands, and copy other files needed for packaging to the dist folder, and finally pack the dist folder into a zip file
```

When you modify the code and compile it, the code will be compiled to the `dist` folder. You need to refresh the offline loaded extension in the browser's extension management, and then refresh the pixiv page to apply the new code.
