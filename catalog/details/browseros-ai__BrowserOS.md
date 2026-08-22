# browseros-ai/BrowserOS

🌐 The open-source Agentic browser; alternative to ChatGPT Atlas, Perplexity Comet, Dia.

## features

<table>
<tr>
<td width="40%" valign="middle">
<h4>Live dashboard</h4>
Your new tab shows every agent working right now: which site it's on, what it's doing, how far along. <a href="https://docs.browseros.com/neo/cockpit">Docs</a>
</td>
<td width="60%">
<img src="docs/images/browserclaw--dashboard-populated.png" alt="BrowserOS neo dashboard showing agent sessions and recent activity" width="100%" />
</td>
</tr>
<tr>
<td width="40%" valign="middle">
<h4>One-click connect</h4>
Automatically connects to every harness. We built tools optimized for web use! <a href="https://docs.browseros.com/neo/mcp">Docs</a>
</td>
<td width="60%">
<img src="docs/images/browserclaw--mcp-install-board.png" alt="BrowserOS neo MCP connect board with one-click install for supported AI tools" width="100%" />
</td>
</tr>
<tr>
<td width="40%" valign="middle">
<h4>Replay every session</h4>
Every session is saved as a scrubbable video on your disk with a step-by-step action timeline. Rewind and see exactly what happened. <a href="https://docs.browseros.com/neo/audit-and-replay">Docs</a>
</td>
<td width="60%">
<img src="docs/images/browserclaw--replay-scrubber.png" alt="BrowserOS neo replay view with video scrubber and action timeline" width="100%" />
</td>
</tr>
</table>

- **Your logins.** Agents automate your real work using your logged-in accounts, not a blank sandbox. [How it works](https://docs.browseros.com/neo/how-it-works)
- **Parallel agents.** Fire off several tasks at once. Each agent works in its own tab while you keep browsing.
- **Fewer tokens.** For the same task, BrowserOS neo consumes significantly less tokens compare to other solutions (like Claude's chrome extension, Codex browser).
- **Local-only, privacy-first.** Sessions, screenshots, and history live under `~/.browserclaw/` and never leave your machine. [Privacy](https://docs.browseros.com/neo/privacy)

### Why BrowserOS neo over the alternatives?

- **Not a headless driver.** Playwright and agent-browser spin up a fresh Chrome subprocess with no logins. Great for CI, useless for real work which requires your logged-in state like "read my inbox." BrowserOS neo imports your logins with one click and persists it across sessions.
- **Not a cloud browser.** Cloud browsers (like browser-use, browserbase) run in a datacenter, so logging into your accounts is a pain, and sites like Twitter and LinkedIn block you because you are on a datacenter IP. BrowserOS neo runs on your machine, on `127.0.0.1`.
- **Not a locked-in AI browser.** Atlas, Comet, and Dia only work with their own AI. BrowserOS neo works with the agents you already use and pay for -- Claude Code, Cowork, Codex, Cursor, etc.

</details>

<details>
<summary><h1><img src="packages/browseros/resources/browseros/icons/product_logo_192.png" alt="" width="28" /> BrowserOS: the AI browser for humans</h1></summary>

**What is BrowserOS?** BrowserOS is a free, open-source Chromium fork with an AI agent built into every new tab. Ask it to summarise a page, click through a flow, extract data, or run a scheduled task, and it uses 20+ built-in tools plus 40+ app integrations to get the work done. Bring your own AI keys or run everything locally with Ollama.

Every AI browser today asks you to sign into their cloud and hand over your data. BrowserOS is the one that doesn't. Same daily browser you already use, with a helpful agent one keystroke away.

[![Download for macOS](https://img.shields.io/badge/Download-macOS-black?style=flat&logo=apple&logoColor=white)](https://files.browseros.com/download/BrowserOS.dmg)
[![Download for Windows](https://img.shields.io/badge/Download-Windows-0078D4?style=flat&logo=windows&logoColor=white)](https://files.browseros.com/download/BrowserOS_installer.exe)
[![Download for Linux](https://img.shields.io/badge/Download-Linux-FCC624?style=flat&logo=linux&logoColor=black)](https://files.browseros.com/download/BrowserOS.AppImage)
[![Download for Debian](https://img.shields.io/badge/Download-Debian-D70A53?style=fla
