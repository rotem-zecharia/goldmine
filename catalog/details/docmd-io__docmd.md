# docmd-io/docmd

Build production-ready documentation from Markdown in seconds. No React, no bloat, just content.

## installation

Run docmd in any folder with Markdown files — no install needed:

```bash
npx @docmd/core dev
```

<details>
  <summary><b>Opens at <code>http://localhost:3000</code></b></summary><br>

```bash
    _                 _ 
  _| |___ ___ _____ _| |
 | . | . |  _|     | . |
 |___|___|___|_|_|_|___|

 v0.9.0

BUILD
  Engine          JS
  Source          docs/
  Output          site/
  Versions        2 (06, 05)
  Locales         7 (en, hi, zh, es, de, ja, fr)

DATA INDEXING
  [ DONE ] Syncing git metadata
  [ DONE ] Building search index & RAG embeddings (multi-version)
  [ DONE ] Generating AI Assistant RAG context

PUBLISHING
  [ DONE ] Generated robots.txt
  [ DONE ] Generated .nojekyll (disables Jekyll on GitHub Pages)
  [ DONE ] Generated sitemap
  [ DONE ] Generating LLMs context files (llms.txt)
  [ DONE ] Generating OKF bundles

⬢ Initial build completed in 1.2s.

WATCHING
  Source          ./docs
  Config          ./docmd.config.json
  Assets          ./assets

DEVELOPMENT SERVER RUNNING
  Local Access    http://127.0.0.1:3000
  Network Access  http://192.168.1.6:3000
  Serving from    ./site
```

</details>

Navigation is generated from your file structure. No config file, no frontmatter required, no framework to learn.

**When you're ready to ship:**

```bash
npx @docmd/core build
```

This outputs a highly optimized static site (SPA) ready for deployment to Vercel, Cloudflare Pages, Netlify, GitHub Pages, or any static host.

**Requirements:** Node.js 18+

<details>
  <summary><b>Or install globally / via Docker</b></summary><br/>

```bash
# Install globally via npm
npm install -g @docmd/core

# Or via pnpm
pnpm add -g @docmd/core

# Run it
docmd dev    # start dev server
docmd build  # build for deployment
```

Or run via Docker:

```bash
docker run -p 3000:3000 ghcr.io/docmd-io/docmd:0.9.0
```

> Pin a version for reproducible builds.

</details>

## features

<div align="center">
  <img width="1000" alt="image" src="https://raw.githubusercontent.com/docmd-io/docmd/refs/heads/main/assets/docmd-comparison.webp" />
</div>

<!--
| Feature | docmd | Docusaurus | MkDocs | VitePress | Mintlify |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Config required** | **None** | `docusaurus.config.js` | `mkdocs.yml` | `config.mts` | `docs.json` |
| **JS payload** | **~18 kb** | ~250 kb | ~40 kb | ~50 kb | ~120 kb |
| **Navigation** | **Instant SPA** | React SPA | Full reload | Vue SPA | Hosted SPA |
| **Versioning** | **Native** | Native (complex) | mike plugin | Manual | Native |
| **i18n** | **Native** | Native (complex) | Plugin-based | Native | Native |
| **Multi-project** | **Native** | Plugin | Plugin | - | - |
| **Search** | **Built-in** | Algolia (cloud) | Built-in | MiniSearch | Cloud |
| **AI Assistant** | **Built-in — BYOK + Cloud Relay** | - | - | - | Built-in (Cloud) |
| **AI context (`llms.txt`)** | **Built-in** | - | - | - | Built-in |
| **MCP server** | **Built-in** | - | - | - | Built-in |
| **Agent skills** | **Built-in** | - | - | - | - |
| **Docker image** | **Official** | - | Official | - | - |
| **Self-hosted** | **Yes** | Yes | Yes | Yes | - |
| **Cost** | **Free (OSS)** | Free (OSS) | Free (OSS) | Free (OSS) | Freemium |
-->

**See Complete [Comparison with Docusaurus, Mintlify and others →](https://docs.docmd.io/comparison/)**

## Features

## configuration

Point docmd at any Markdown folder and it runs. Navigation is built automatically from your file structure. You can write your first doc and have it live in under a minute — no boilerplate, no build pipeline to configure, no decisions to make upfront.

### Tiny by default, fast everywhere
The default JavaScript payload is ~18 kb. Pages navigate as an instant SPA. The output is static HTML — SEO-optimised, with sitemap, canonical URLs, and Open Graph metadata included. Offline full-text search is built in, no cloud service required.

### AI-native
docmd treats AI as a first-class way to consume documentation — without replacing the documentation itself.
- **AI Assistant (`@docmd/plugin-ai`)** — RAG-powered chat grounded in your documentation. Use your own API key or connect a local AI provider, with support for a wide range of 100+ providers through AIPlug.
- **Cloud Relay** — enable the AI Assistant on static documentation without running your own AI backend. [Try it →](https://cloud.docmd.io)
- **MCP Server** — `docmd mcp` exposes your docs to AI agents over stdio, letting them search, read, and validate content directly.
- **Context (`llms.txt` / `llms-full.txt`)** — complete documentation context generated at build time.
- **Agent Skills** — modular instruction sets for LLMs and IDE agents.
- **Open Knowledge Format (OKF)** — structured, multi-locale knowledge bundles for AI systems.
- **Copy as Markdown / Copy Context** — one-click context extraction directly from the browser.

### Built to scale
- Internationalisation with multi-locale builds (per-locale search index, llms, okf, hreflang)
- Versioning for multiple doc releases (with auto-detection of the current version)
- Workspaces for monorepos and multi-project setups
- Plugin system for extending core behaviour (per-hook return-type validation, async-friendly)
- Full theming support, built-in templates, custom CSS/JS, light/dark mode

## CLI

```bash
docmd dev            # local development server
docmd build          # build for deployment
docmd live           # browser-based Live Editor
docmd init           # scaffold a new docmd.config.json in the current folder
docmd stop           # stop any running `docmd dev` / `docmd live` servers
docmd doctor         # pre-flight check: config + plugin install status
docmd migrate        # migrate to docmd from Docusaurus, VitePress, MkDocs, or Starlight
docmd deploy         # generate config for Docker, NGINX, Caddy, Vercel, Netlify
docmd validate       # check all internal links
docmd mcp            # run as an MCP server over stdio
docmd add <name>     # install a plugin or template
```

## Plugins

Core functionality is powered by a robust plugin system. The essentials are included by default, while optional plugins can be added for specific needs.

| Plugin | Status | Description |
| :--- | :---: | :--- |
| `ai` | Core | RAG-powered AI Assistant with BYOK, local providers, and Cloud Relay |
| `search` | Core | Offline full-text search (keyword + optional semantic via `docmd-search`) |
| `seo` | Core | SEO tags and Open Graph metadata |
| `sitemap` | Core | Generates `sitemap.xml` |
| `git` | Core | Git commit history and last-updated dates |
| `analytics` | Core | Lightweight analytics integration |
| `llms` | Core | AI context generation (`llms.txt` / `llms-full.txt`) |
| `okf` | Core | Open Knowledge Format bundles for AI agents (per-locale) |
| `mermaid` | Core | Mermaid diagram support |
| `openapi` | Core | Build-time OpenAPI 3.x spec renderer |
| `pwa` | Optional | Progressive Web App — offline navigation |
| `threads` | Optional | Inline discussion threads *(by @svallory)* |
| `math` | Optional | KaTeX / LaTeX math rendering |

Install optional plugins:

```bash
docmd add <plugin-name>
```

Build your own: [Plugin Development Guide](https://docs.docmd.io/development/building-plugins/)

## Configuration

No configuration is required to get started. Add a `docmd.config.json` (or `.ts` / `.js`) in your project root 

## tools

Use docmd in Node.js scripts, CI pipelines, or custom build steps. (Supports both CommonJS and ESM).

```javascript
import { build } from '@docmd/core';

await build('./docmd.config.json', { isDev: false });
```

Full reference: [Node API](https://docs.docmd.io/development/node-api-reference/)

## Community

- **Bugs & issues** → [GitHub Issues](https://github.com/docmd-io/docmd/issues)
- **Questions & ideas** → [Discussions](https://github.com/orgs/docmd-io/discussions)
- **Contributing** → [CONTRIBUTING.md](.github/CONTRIBUTING.md)
- **Roadmap** → [GitHub Discussions](https://github.com/orgs/docmd-io/discussions/2)

## Support

- Getting the word out is the most direct way to support docmd's development. [Share it on X](https://twitter.com/intent/tweet?url=https://github.com/docmd-io/docmd&text=docmd%20-%20Production-ready%20docs%20from%20Markdown%20in%20seconds.) with friends or give it a star.
- If docmd saves you time, a [GitHub sponsorship](https://github.com/sponsors/mgks) goes a long way.
- Got ideas or bugs? Open an issue or PR, feel free to contribute your own plugins.

## License

MIT License. See `LICENSE` for details.
