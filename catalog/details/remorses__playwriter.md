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

## Quick Start

```bash
playwriter browser start  # starts Chrome for Testing/Chromium with bundled Playwriter extension
playwriter session new  # creates stateful sandbox, outputs session id (e.g. 1)
playwriter -s 1 -e 'await page.goto("https://example.com")'
playwriter -s 1 -e 'console.log(await snapshot({ page }))'
playwriter -s 1 -e 'await page.locator("aria-ref=e5").click()'
```

> **Tip:** Always use single quotes for `-e` to prevent bash from interpreting `$`, backticks, and `\` in your JS code. Use double quotes for strings inside the JS.

## tools

Each session has **isolated state**. Browser tabs are **shared** across sessions.

```bash
# Browser management
playwriter browser start             # auto-finds Chrome for Testing or Chromium, with recording flags enabled
playwriter browser start /path/to/browser-binary

# Session management
playwriter session new              # creates stateful sandbox, outputs id (e.g. 1)
playwriter session list             # show sessions + state keys
playwriter session reset <id>       # fix connection issues

# Execute (always use -s)
playwriter -s 1 -e 'await page.goto("https://example.com")'
playwriter -s 1 -e 'await page.click("button")'
playwriter -s 1 -e 'console.log(await page.title())'
```

Create your own page to avoid interference from other agents:

```bash
playwriter -s 1 -e 'state.myPage = await context.newPage(); await state.myPage.goto("https://example.com")'
```

Multiline:

```bash
playwriter -s 1 -e $'
const title = await page.title();
console.log({ title, url: page.url() });
'
```

## Examples

Variables in scope: `page`, `context`, `state` (persists between calls), `require`, `importModule`, native `import()`, and Node.js globals. Relative imports resolve from the session working directory.

**Persist data in state:**

```bash
playwriter -e "state.users = await page.$$eval('.user', els => els.map(e => e.textContent))"
playwriter -e "console.log(state.users)"
```

**Intercept network requests:**

```bash
playwriter -e "state.requests = []; page.on('response', r => { if (r.url().includes('/api/')) state.requests.push(r.url()) })"
playwriter -e "await Promise.all([page.waitForResponse(r => r.url().includes('/api/')), page.click('button')])"
playwriter -e "console.log(state.requests)"
```

**Set breakpoints and debug:**

```bash
playwriter -e "state.cdp = await getCDPSession({ page }); state.dbg = createDebugger({ cdp: state.cdp }); await state.dbg.enable()"
playwriter -e "state.scripts = await state.dbg.listScripts({ search: 'app' }); console.log(state.scripts.map(s => s.url))"
playwriter -e "await state.dbg.setBreakpoint({ file: state.scripts[0].url, line: 42 })"
```

**Live edit page code:**

```bash
playwriter -e "state.cdp = await getCDPSession({ page }); state.editor = createEditor({ cdp: state.cdp }); await state.editor.enable()"
playwriter -e "await state.editor.edit({ url: 'https://example.com/app.js', oldString: 'const DEBUG = false', newString: 'const DEBUG = true' })"
```

**Screenshot with labels:**

```bash
playwriter -e "await screenshotWithAccessibilityLabels({ page })"
```

**Live stream a tab to X Live / Twitch (RTMP, runs 24/7):**

```bash
playwriter -s 1 -e "await page.goto('https://example.com')"
playwriter stream start -s 1 --rtmp rtmp://va.pscp.tv:80/x/<stream-key>
playwriter stream status -s 1
playwriter stream stop -s 1
```

## limitations

- If all pages return `about:blank`, restart Chrome (Chrome bug in `chrome.debugger` API)
- Browser may switch to light mode on connect ([Playwright issue](https://github.com/microsoft/playwright/issues/37627))

## Sponsor — Bloome

<div align="center">
<a href="https://bloome.im/app?utm_medium=github&utm_source=remorses-playwriter-ivor-202607">
  <img src="bloome-home.png" alt="Bloome" width="480" />
</a>
</div>

Building agents that drive the browser with Playwriter? [**Bloome**](https://bloome.im/app?utm_medium=github&utm_source=remorses-playwriter-ivor-202607) gives them a home for your whole team — an AI-agent IM platform where agents are real members of the chat. Run them in the cloud, have them hand off tasks and collaborate, and share working agents with your team. Zero setup, on web and mobile.
