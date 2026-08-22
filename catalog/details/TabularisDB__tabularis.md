# TabularisDB/tabularis

Open-source desktop SQL workspace for PostgreSQL, MySQL/MariaDB, SQLite and 15+ more databases like DuckDB, ClickHouse, Redis and Firestore. Built-in MCP server for Claude, Cursor and Devin, SQL noteb

## features

|  | **tabularis** | DBeaver CE | TablePlus | Beekeeper Studio |
|---|---|---|---|---|
| License | Apache 2.0, free | Apache 2.0, free (Pro is paid) | Commercial | GPLv3 (paid editions) |
| SQL notebooks (SQL + Markdown cells, cross-cell variables, charts) | ✅ | ❌ | ❌ | ❌ |
| Built-in MCP server for AI agents | ✅ | ❌ | ❌ | ❌ |
| Plugins in **any language** (JSON-RPC over stdio) | ✅ | Java/Eclipse plugins | JavaScript plugins | ❌ |
| AI text-to-SQL with **local models** (Ollama) | ✅ | Cloud-based AI assistant | ❌ | ❌ |
| Visual EXPLAIN with interactive plan graphs | ✅ | ✅ | ❌ | ❌ |
| Databases out of the box | 3 built-in + 16 official plugins | 100+ | 20+ | ~10 |

> Comparison as of June 2026; features in other tools may have changed since. If you need dozens of drivers, use DBeaver. Tabularis focuses on doing a few databases well.

## configuration

> [Full reference on tabularis.dev →](https://tabularis.dev/wiki/configuration)

Configuration is stored in `~/.config/tabularis/` (Linux), `~/Library/Application Support/tabularis/` (macOS), or `%APPDATA%\tabularis\` (Windows): connection profiles, saved queries, app settings (`config.json`), custom themes, and per-connection editor preferences. Tabs and queries are restored when you reopen a connection. The wiki covers the full file layout and every `config.json` option, including custom AI model overrides.

## installation

```bash
pnpm install
pnpm tauri dev
```

## limitations

- [x] [[Feat]: Allow loading of multiple Databases per connection](https://github.com/TabularisDB/tabularis/issues/47)
- [x] [JSON/JSONB Editor & Viewer](https://github.com/TabularisDB/tabularis/issues/24)
- [x] [Visual Explain Analyze](https://github.com/TabularisDB/tabularis/issues/22)
- [x] [Plugin System](https://github.com/TabularisDB/tabularis/issues/19)
- [x] [Query History](https://github.com/TabularisDB/tabularis/issues/18)
- [ ] [Plugin registry platform: OAuth publishing, release sync, download analytics](https://github.com/TabularisDB/tabularis/issues/196)
- [ ] [UI design system & visual identity: call for contributors](https://github.com/TabularisDB/tabularis/issues/195)
- [ ] [SQL Server driver plugin, in development in its own repository](https://github.com/TabularisDB/tabularis-sqlserver-plugin)
- [ ] [Feature: Remote Control](https://github.com/TabularisDB/tabularis/issues/46)
- [ ] [Command Palette](https://github.com/TabularisDB/tabularis/issues/25)
- [ ] [SQL Formatting / Prettier](https://github.com/TabularisDB/tabularis/issues/23)
- [ ] [Data Compare / Diff Tool](https://github.com/TabularisDB/tabularis/issues/21)
- [ ] [Team Collaboration](https://github.com/TabularisDB/tabularis/issues/20)
- [ ] [Better SQLite Support](https://github.com/TabularisDB/tabularis/issues/17)
- [ ] [Better PostgreSQL Support](https://github.com/TabularisDB/tabularis/issues/16)
