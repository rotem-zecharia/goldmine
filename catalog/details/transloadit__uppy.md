# transloadit/uppy

The next open source file uploader for web browsers :dog:

## features

- Lightweight, modular plugin-based architecture, light on dependencies :zap:
- Resumable file uploads via the open [tus](https://tus.io/) standard, so large
  uploads survive network hiccups
- Supports picking files from: Webcam, Dropbox, Box, Google Drive,
  bypassing the user’s device where possible, syncing between servers directly
  via [@uppy/companion](https://uppy.io/docs/companion)
- Works great with file encoding and processing backends, such as
  [Transloadit](https://transloadit.com), which handles encoding, conversion and
  delivery for you; works great without one too, if you would rather run and
  scale your own Apache/Nginx/Node/FFmpeg pipeline
- Sleek user interface :sparkles:
- Optional file recovery (after a browser crash) with
  [Golden Retriever](https://uppy.io/docs/golden-retriever/)
- Speaks several languages (i18n) :earth_africa:
- Built with accessibility in mind
- Free for the world, forever (as in beer 🍺, pizza 🍕, and liberty 🗽)
- Cute as a puppy, also accepts cat pictures :dog:

## installation

```bash
npm install @uppy/core @uppy/dashboard @uppy/tus
```

Add CSS
[uppy.min.css](https://releases.transloadit.com/uppy/v5.2.4/uppy.min.css),
either to your HTML page’s `<head>` or include in JS, if your bundler of choice
supports it.

Alternatively, you can also use a pre-built bundle from Transloadit’s CDN: Smart
CDN. In that case `Uppy` will attach itself to the global `window.Uppy` object.

> ⚠️ The bundle consists of most Uppy plugins, so this method is not recommended
> for production, as your users will have to download all plugins when you are
> likely using only a few.

```html
<!-- 1. Add CSS to `<head>` -->
<link
  href="https://releases.transloadit.com/uppy/v5.2.4/uppy.min.css"
  rel="stylesheet"
/>

<!-- 2. Initialize -->
<div id="files-drag-drop"></div>
<script type="module">
  import {
    Uppy,
    Dashboard,
    Tus,
  } from 'https://releases.transloadit.com/uppy/v5.2.4/uppy.min.mjs'

  const uppy = new Uppy()
  uppy.use(Dashboard, { target: '#files-drag-drop' })
  uppy.use(Tus, { endpoint: 'https://tusd.tusdemo.net/files/' })
</script>
```
