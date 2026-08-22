# remorses/playwriter

Chrome extension & CLI to let agents control your browser. Runs Playwright snippets in a stateful sandbox. Available as CLI or MCP

## installation

1. [**Install Extension**](https://chromewebstore.google.com/detail/playwriter-mcp/jfeammnjpkecdekppnclgkkffahnhfhe) from Chrome Web Store

2. Click extension icon on a tab → turns green when connected

3. Install the CLI and start automating the browser:

   ```bash
   npm i -g playwriter
   playwriter -s 1 -e 'await page.goto("https://example.com")'
   ```

4. Install the skill so your agent knows how to use Playwriter:
   ```bash
   npx -y skills add remorses/playwriter
   ```

## tools

Each session has **isolated state**. Browser tabs are **shared** across sessions.

```bash

## limitations

- If all pages return `about:blank`, restart Chrome (Chrome bug in `chrome.debugger` API)
- Browser may switch to light mode on connect ([Playwright issue](https://github.com/microsoft/playwright/issues/37627))
