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

## Documentation

- [Uppy](https://uppy.io/docs/uppy/) — full list of options, methods and events
- [Companion](https://uppy.io/docs/companion/) — setting up and running a
  Companion instance, which adds support for Dropbox, Box, Google
  Drive and remote URLs
- [React](https://uppy.io/docs/react/) — components to integrate Uppy UI plugins
  with React apps
- [Architecture & Writing a Plugin](https://uppy.io/docs/writing-plugins/) — how
  to write a plugin for Uppy

## Plugins

### UI Elements

- [`Dashboard`](https://uppy.io/docs/dashboard/) — universal UI with previews,
  progress bars, metadata editor and all the cool stuff. Required for most UI
  plugins like Webcam
- Headless components ([react](https://uppy.io/docs/react/), [svelte](https://uppy.io/docs/svelte/), [vue](https://uppy.io/docs/vue/))

### Sources

- [`Drag & Drop`](https://uppy.io/docs/drag-drop/) — plain drag and drop area
- [`File Input`](https://uppy.io/docs/file-input/) — even plainer “select files”
  button
- [`Webcam`](https://uppy.io/docs/webcam/) — snap and record those selfies 📷
- ⓒ [`Google Drive`](https://uppy.io/docs/google-drive/) — import files from
  Google Drive
- ⓒ [`Dropbox`](https://uppy.io/docs/dropbox/) — import files from Dropbox
- ⓒ [`Box`](https://uppy.io/docs/box/) — import files from Box
- ⓒ [`Facebook`](https://uppy.io/docs/facebook/) — import images and videos from
  Facebook
- ⓒ [`OneDrive`](https://uppy.io/docs/onedrive/) — import files from Microsoft
  OneDrive
- ⓒ [`Import From URL`](https://uppy.io/docs/url/) — import direct URLs from
  anywhere on the web

The ⓒ mark means that [`@uppy/companion`](https://uppy.io/docs/companion), a
server-side component, is needed for a plugin to work.

### Destinations

- [`Tus`](https://uppy.io/docs/tus/) — resumable uploads via the open
  [tus](http://tus.io) standard
- [`XHR Upload`](https://uppy.io/docs/xhr-upload/) — regular uploads for any
  backend out there (like Apache, Nginx)
- [`AWS S3`](https://uppy.io/docs/aws-s3/) — plain upload to AWS S3 or
  compatible services

### File Processing

- [`Transloadit`](https://uppy.io/docs/transloadit/) — support for
  [Transloadit](http://transloadit.com)’s robust file uploading and encoding
  backend

### Miscellaneous

- [`Golden Retriever`](https://uppy.io/docs/golden-retriever/) — restores files
  after a browser crash, like it’s nothing
- [`Thumbnail Generator`](https://uppy.io/docs/thumbnail-generator/) — generates
  image previews (included by default with `Dashboard`)
- [`Form`](https://uppy.io/docs/form/) — collects metadata from `<form>` right
  before an Uppy upload, then optionally appends results back to the form

## Browser Support

We aim to support recent versions of Chrome, Firefox, and Safari.

## FAQ
