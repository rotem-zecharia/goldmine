# microlinkhq/youtube-dl-exec

Promise-friendly Node.js wrapper around youtube-dl / yt-dlp for downloading media.

## installation

> **Note**: It requires Python 3.9 or above available in your system as `python3`. Otherwise, the library will throw an error.

```bash
$ npm install youtube-dl-exec --save
```

By default, the library will auto-install the latest `yt-dlp` available that will downloaded on [build](https://github.com/microlinkhq/youtube-dl-exec/blob/master/package.json#L70) time.

## tools

Any `yt-dlp` flags is supported:

```js
const youtubedl = require('youtube-dl-exec')

youtubedl('https://www.youtube.com/watch?v=6xKWiCMKKJg', {
  dumpSingleJson: true,
  noCheckCertificates: true,
  noWarnings: true,
  preferFreeFormats: true,
  addHeader: ['referer:youtube.com', 'user-agent:googlebot']
}).then(output => console.log(output))
```

It's equivalent to:

```bash
$ ./bin/yt-dlp \
  --dump-single-json \
  --no-check-certificates \
  --no-warnings \
  --prefer-free-formats \
  --add-header='user-agent:googlebot' \
  --add-header='referer:youtube.com' \
  'https://www.youtube.com/watch?v=6xKWiCMKKJg'
```

Type `yt-dlp --help` for seeing all of them.

## configuration

It execs any `yt-dlp` command, returning back the output.

#### url

_Required_<br>
Type: `string`

The URL to target.

#### flags

Type: `object`

Any flag supported by `yt-dlp`.

#### options

Any option provided here will passed to [spawn#options](https://nodejs.org/api/child_process.html#child_processspawncommand-args-options).
