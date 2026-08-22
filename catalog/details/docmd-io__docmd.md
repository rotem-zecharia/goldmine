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

## configuration

Point docmd at any Markdown folder and it runs. Navigation is built automatically from your file structure. You can write your first doc and have it live in under a minute — no boilerplate, no build pipeline to configure, no decisions to make upfront.

## tools

Use docmd in Node.js scripts, CI pipelines, or custom build steps. (Supports both CommonJS and ESM).

```javascript
import { build } from '@docmd/core';

await build('./docmd.config.json', { isDev: false });
```

Full reference: [Node API](https://docs.docmd.io/development/node-api-reference/)
