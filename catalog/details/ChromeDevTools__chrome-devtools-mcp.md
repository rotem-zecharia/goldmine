# ChromeDevTools/chrome-devtools-mcp

Chrome DevTools for coding agents

## tools

[![npm chrome-devtools-mcp package](https://img.shields.io/npm/v/chrome-devtools-mcp.svg)](https://npmjs.org/package/chrome-devtools-mcp)

Chrome DevTools for agents (`chrome-devtools-mcp`) lets your coding agent (such as Antigravity, Claude, Cursor or Copilot)
control and inspect a live Chrome browser. It is available as a
Model-Context-Protocol (MCP) server and as a [CLI][cli]. Both give your AI
coding assistant access to the full power of Chrome DevTools for reliable
automation, in-depth debugging, and performance analysis.

[Tool reference][tool-reference] | [CLI][cli] | [Skills][skills] | [Changelog][changelog] | [Contributing][contributing] | [Troubleshooting][troubleshooting] | [Design Principles][design-principles]

## features

- **Get performance insights**: Uses [Chrome
  DevTools](https://github.com/ChromeDevTools/devtools-frontend) to record
  traces and extract actionable performance insights.
- **Advanced browser debugging**: Analyze network requests, take screenshots and
  check browser console messages (with source-mapped stack traces).
- **Reliable automation**. Uses
  [puppeteer](https://github.com/puppeteer/puppeteer) to automate actions in
  Chrome and automatically wait for action results.

## Disclaimers

`chrome-devtools-mcp` exposes content of the browser instance to the MCP clients
allowing them to inspect, debug, and modify any data in the browser or DevTools.
Avoid sharing sensitive or personal information that you don't want to share with
MCP clients.

`chrome-devtools-mcp` officially supports Google Chrome and [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) only.
Other Chromium-based browsers may work, but this is not guaranteed, and you may encounter unexpected behavior. Use at your own discretion.
We are committed to providing fixes and support for the latest version of [Extended Stable Chrome](https://chromiumdash.appspot.com/schedule).

Performance tools may send trace URLs to the Google CrUX API to fetch real-user
experience data. This helps provide a holistic performance picture by
presenting field data alongside lab data. This data is collected by the [Chrome
User Experience Report (CrUX)](https://developer.chrome.com/docs/crux). To disable
this, run with the `--no-performance-crux` flag.

## requirements

- [Node.js](https://nodejs.org/) [LTS](https://github.com/nodejs/Release#release-schedule) version.
- [Chrome](https://www.google.com/chrome/) current stable version or newer.
- [npm](https://www.npmjs.com/)

## installation

Add the following config to your MCP client:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

> [!NOTE]
> Using `chrome-devtools-mcp@latest` ensures that your MCP client will always use the latest version of the Chrome DevTools MCP server.

## configuration

For setup instructions specific to your editor or agent (e.g. Antigravity, Claude Code, Cursor, VS Code), please see our [Client Configurations Guide][client-configurations-guide].

### Your first prompt

Enter the following prompt in your MCP Client to check if everything is working:

```
Check the performance of https://developers.chrome.com
```

Your MCP client should open the browser and record a performance trace.

> [!NOTE]
> The MCP server will start the browser automatically once the MCP client uses a tool that requires a running browser instance. Connecting to the Chrome DevTools MCP server on its own will not automatically start the browser.

## CLI

The package also includes the `chrome-devtools` CLI. Use it to control the browser from your terminal without MCP:

```sh
npm i chrome-devtools-mcp@latest -g
chrome-devtools navigate_page 1 --url "https://developers.chrome.com"
chrome-devtools take_screenshot 1 --filePath screenshot.png
chrome-devtools stop
```

See the [CLI guide][cli] for all commands and options.

## Skills

The package includes [skills](./skills) that teach your agent how to use Chrome DevTools:

| Skill                                                     | Use it to                                       |
| --------------------------------------------------------- | ----------------------------------------------- |
| [`chrome-devtools`](./skills/chrome-devtools)             | Debug and automate pages with the MCP tools.    |
| [`chrome-devtools-cli`](./skills/chrome-devtools-cli)     | Run the CLI and write shell scripts with it.    |
| [`a11y-debugging`](./skills/a11y-debugging)               | Audit and fix accessibility issues.             |
| [`cookie-debugging`](./skills/cookie-debugging)           | Debug cookies, sessions, and authentication.    |
| [`debug-optimize-lcp`](./skills/debug-optimize-lcp)       | Debug and improve Largest Contentful Paint.     |
| [`memory-leak-debugging`](./skills/memory-leak-debugging) | Find and fix memory leaks.                      |
| [`troubleshooting`](./skills/troubleshooting)             | Fix connection problems between MCP and Chrome. |
