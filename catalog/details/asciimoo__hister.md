# asciimoo/hister

Your own search engine

## installation

1. Download the binary for your platform from the [latest release](https://github.com/asciimoo/hister/releases/latest), then rename it to `hister` (`hister.exe` on Windows).

2. On Linux or macOS, make it executable:

   ```bash
   chmod +x hister
   ```

3. Start Hister on Linux or macOS:

   ```bash
   ./hister listen
   ```

   On Windows, run `.\hister.exe listen` in PowerShell.

4. Open <http://127.0.0.1:4433> and install the browser extension for [Firefox](https://addons.mozilla.org/en-US/firefox/addon/hister/) or [Chrome](https://chromewebstore.google.com/detail/hister/cciilamhchpmbdnniabclekddabkifhb).

No configuration is required for a local personal setup. See the [complete quickstart](https://hister.org/docs/quickstart) to import existing browser history and choose what Hister indexes.

## features

- **Privacy focused**: No telemetry or mandatory cloud service. Run Hister locally or on infrastructure you control.
- **Full text indexing**: Search the actual contents of visited pages and local files, not only titles and URLs.
- **Automatic browser indexing**: Save newly visited pages with the Firefox or Chrome extension.
- **Powerful queries**: Use field filters, phrases, wildcards, negation, aliases, and result priorities.
- **Optional semantic search**: Find documents by meaning through an embeddings endpoint you configure.
- **Crawler and browser import**: Index websites or bring in existing browser history.
- **Web, terminal, and MCP clients**: Search from the browser, TUI, command line, or an AI assistant.
- **Multi user support**: Keep each user's documents and search results separate on a shared server.

![Hister terminal interface](webui/website/src/lib/assets/demo.gif)
