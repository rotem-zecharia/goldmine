# t8y2/dbx

20 MB lightweight cross-platform database client for 90+ databases, including MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, SQL Server, and Dameng. Built-in AI, MCP Server, CLI, desktop and Docke

## features

<table>
  <tr>
    <td width="50%">
      <h3>🪶 20 MB, zero runtime bloat</h3>
      <p>No Java JRE. No Python venv. No bundled Chromium. DBX ships as a single small binary — download, install, connect. DBeaver needs Java; TablePlus is macOS-only. DBX runs everywhere with nothing extra.</p>
    </td>
    <td width="50%">
      <h3>🤖 AI that lives in your editor</h3>
      <p>Highlight a table, describe what you want, get SQL back — no copy-paste between tools. Works with Claude, OpenAI, or local models via Ollama. Built-in safety checks review AI-generated SQL before it runs.</p>
    </td>
  </tr>
  <tr>
    <td>
      <h3>🔌 MCP: your databases, AI-ready</h3>
      <p>DBX speaks the Model Context Protocol. Claude Code, Cursor, Windsurf, and other AI coding agents can query your databases through connections you already set up. One config, everywhere.</p>
    </td>
    <td>
      <h3>🌐 Desktop + Docker + Web</h3>
      <p>Native app on macOS, Windows, and Linux. Self-host via Docker for team access. Web version for browser-only environments. Same feature set. Same connections.</p>
    </td>
  </tr>
</table>

## tools

- **Schema browser** — databases, schemas, tables, columns, indexes, foreign keys, triggers, with sidebar search & pin
- **Object browser** — grouped procedures, functions, views, and source editing where supported
- **Table structure editor** — reviewable column and index changes for supported engines
- **ER diagram** — visualize table relationships
- **Schema diff** — compare structures across connections
- **Explain plan** — visual query execution plan
- **Field lineage** — column-level lineage analysis
- **Database search** — find objects across large schemas

## installation

Download the latest release from the [Releases](https://github.com/t8y2/dbx/releases/latest) page.

**Homebrew (macOS):**

```bash
brew install --cask dbx
```

**Scoop (Windows):**

```bash
scoop bucket add dbx https://github.com/t8y2/scoop-bucket
scoop install dbx
```

**WinGet (Windows):**

```
winget install t8y2.dbx
```

**Flatpak (Linux):**

```bash
flatpak remote-add --if-not-exists flatpark https://dl.flatpark.org/flatpark.flatpakrepo
flatpak install flatpark com.dbxio.dbx
```

Updates then arrive through the regular `flatpak update`. See the [DBX page on FlatPark](https://flatpark.org/apps/com.dbxio.dbx/) for details.

## requirements

- [Node.js](https://nodejs.org/) >= 18
- [pnpm](https://pnpm.io/)
- [Rust](https://www.rust-lang.org/tools/install) >= 1.88

#### System Dependencies

**macOS:**

No additional dependencies required.

**Linux (Ubuntu/Debian):**

```bash
sudo apt-get install -y libwebkit2gtk-4.1-dev libgtk-3-dev libappindicator3-dev librsvg2-dev patchelf libssl-dev
```

**NIXOS/NIX :** 

<a href="README-NIX.md">See README-NIX.md</a>

**Windows:**

No additional dependencies required.
