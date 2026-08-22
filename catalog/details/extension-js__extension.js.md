# extension-js/extension.js

The cross-browser extension framework.

## features

Browser extensions ship with the worst dev experience in modern web. Manifest V3 fragmentation, browser-specific quirks, no hot reload for content scripts, and a separate build pipeline for every target. Extension.js fixes that.

- **Hot Module Replacement** for background, content, popup, and options scripts, including React, Vue, Svelte, and Preact components
- **Manifest V3 by default**, with automatic adapters for Chrome, Edge, Firefox, and Safari targets
- **One CLI** for Chrome, Edge, Firefox, and any Chromium or Gecko binary
- **Zero config**, no webpack, no rollup, no plugins to maintain
- **First-class** TypeScript, React, Vue, Svelte, and Preact support
- **Production builds** with `extension build --zip`, ready for the Chrome Web Store and Firefox Add-ons
- **Drop-in** for existing extensions with one `devDependency`

## installation

npx extension@latest install firefox
