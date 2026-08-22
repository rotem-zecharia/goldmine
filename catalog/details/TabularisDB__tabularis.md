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

### Database support

PostgreSQL, MySQL/MariaDB and SQLite ship built in. Everything else is a plugin. Current coverage, mirroring the [driver & plugin coverage](https://tabularis.dev/#driver-coverage) on the website:

[ClickHouse](https://github.com/TabularisDB/tabularis-clickhouse-plugin) (shipped), [Cloudflare D1](https://github.com/josejorge/tabularis_cloudflare_d1_plugin) (shipped), [DM / Dameng](https://github.com/haos666/tabularis-dameng-plugin) (shipped), [DuckDB](https://github.com/TabularisDB/tabularis-duckdb-plugin) (shipped), [DynamoDB](https://github.com/TabularisDB/tabularis-dynamodb-plugin) (shipped), [Elasticsearch](https://github.com/TabularisDB/tabularis-elasticsearch-plugin) (shipped), [Firestore](https://codeberg.org/NewtTheWolf/firestore-tabularis) (shipped), [IBM Db2](https://github.com/TabularisDB/tabularis-db2-plugin) (shipped), [IBM Informix](https://github.com/danielnuld/tabularis-informix-plugin) (shipped), [MongoDB](https://github.com/danielnuld/tabularis-mongodb-plugin) (shipped), Redis (shipped, in [Go](https://github.com/gzamboni/tabularis-redis-plugin-go) and [Rust](https://github.com/nicholas-papachriston/tabularis-redis-plugin)), [CSV Folder](https://github.com/TabularisDB/tabularis-csv-plugin) (shipped), [Google Sheets](https://github.com/TabularisDB/tabularis-google-sheets-plugin) (shipped), [HackerNews](https://github.com/TabularisDB/tabularis-hackernews-plugin) (shipped), Google BigQuery (claimed), [LibSQL / Turso](https://github.com/TabularisDB/tabularis-libsql-plugin) (claimed), Meilisearch (claimed), [Oracle](https://github.com/TabularisDB/tabularis-oracle-plugin) (claimed), [SQL Server](https://github.com/TabularisDB/tabularis-sqlserver-plugin) (claimed), Amazon Redshift (scoped), CockroachDB (scoped), TiDB (scoped), Snowflake (coming soon), Cassandra (open), Etcd (open), Firebird (open), ScyllaDB (open), SQL Anywhere (open), SurrealDB (open), Trino / Presto (open).

> **Shipped** drivers are installable from the [plugin registry](https://tabularis.dev/plugins). Everything else is on the [bounty board](https://tabularis.dev/plugins/bounties): claim one, sponsor one, or [request a database](https://github.com/TabularisDB/tabularis/discussions). The SQL Server driver is in active development in its own repository, [tabularis-sqlserver-plugin](https://github.com/TabularisDB/tabularis-sqlserver-plugin).

## installation

### Windows

#### WinGet (Recommended)

```bash
winget install Debba.Tabularis
```

#### Direct Download

Download the installer from the [Releases page](https://github.com/TabularisDB/tabularis/releases) and run it:

```
tabularis_x.x.x_x64-setup.exe
```

Follow the on-screen instructions to complete the installation.

### macOS

#### Homebrew (Recommended)

To add our tap, run:

```bash
brew tap TabularisDB/tabularis
```

Then install:

```bash
brew install --cask tabularis
```

[![Homebrew](https://img.shields.io/badge/Homebrew-Repository-orange?logo=homebrew)](https://github.com/debba/homebrew-tabularis)

#### Direct Download

Builds from **v0.13.1** onward are signed and notarized by Apple, so they open without any extra steps.

The notes below only apply to **older releases (before v0.13.1)** downloaded directly:

- You need to allow accessibility access (Privacy & Security) to the tabularis app. If you are upgrading and already have tabularis on the allowed list, remove it manually before accessibility access can be granted to the new version.
- You may need to run `xattr -c /Applications/tabularis.app` after copying the app to the Applications directory.

### Linux (Snap)

```bash
sudo snap install tabularis
```

[![Snap Store](https://img.shields.io/badge/snap-tabularis-blue?logo=snapcraft)](https://snapcraft.io/tabularis)

### Linux (Flatpak)

```bash
flatpak remote-add --if-not-exists flatpark https://dl.flatpark.org/flatpark.flatpakrepo
flatpak install flatpark dev.tabularis.Tabularis
```

[![Flatpak (Flatpark)](https://img.shields.io/badge/flatpak-tabularis-4A90D9?logo=flatpak&logoColor=white)](https://flatpark.org/apps/dev.tabularis.Tabularis/)

### Linux (AppImage)

Download the `.AppImage` file from the [Releases page](https://github.com/TabularisDB/tabularis/releases), make it executable and run it:

```bash
chmod +x tabularis_x.x.x_amd64.AppImage
./tabularis_x.x.x_amd64.AppImage
```

### Arch Linux (AUR)

```bash
yay -S tabularis-bin
```

## Updates

Tabularis checks for updates automatically on startup and notifies you when a new version is available. You can also download the latest version directly from the [Releases page](https://github.com/TabularisDB/tabularis/releases).

## Discord

Join our [Discord server](https://discord.com/invite/K2hmhfHRSt) to talk with the maintainers, share feedback, suggest features, or get help from the community.

## [Changelog](./CHANGELOG.md)

## configuration

> [Full reference on tabularis.dev →](https://tabularis.dev/wiki/configuration)

Configuration is stored in `~/.config/tabularis/` (Linux), `~/Library/Application Support/tabularis/` (macOS), or `%APPDATA%\tabularis\` (Windows): connection profiles, saved queries, app settings (`config.json`), custom themes, and per-connection editor preferences. Tabs and queries are restored when you reopen a connection. The wiki covers the full file layout and every `config.json` option, including custom AI model overrides.

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

## Contributing

Contributions are welcome, see [CONTRIBUTING.md](./CONTRIBUTING.md). Good places to start:

- [SQL Server driver plugin: test the driver and claim open issues](https://github.com/TabularisDB/tabularis-sqlserver-plugin)
- [UI design system & visual identity: call for contributors](https://github.com/TabularisDB/tabularis/issues/195)
- Write a driver plugin in any language with the [Plugin Guide](./plugins/PLUGIN_GUIDE.md)

<!-- SPONSORS:START -->

## Sponsors and supporters

- <a href="https://www.serversmtp.com/?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor" target="_blank"><img src="https://tabularis.dev/img/sponsors/turbosmtp_compact.png" height="28" alt="turboSMTP" /></a> **[turboSMTP](https://www.serversmtp.com/?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor)** — Professional SMTP relay — your emails delivered straight to the inbox, never to spam
- <a href="https://www.kilo.ai/?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor" target="_blank"><img src="https://tabularis.dev/img/sponsors/kilocode_compact.png" height="28" alt="Kilo Code" /></a> **[Kilo Code](https://www.kilo.ai/?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor)** — Open source AI coding agent — build, ship, and iterate faster with 500+ models
- <a href="https://openai.com/codex/?utm_source=tabularis&utm_medium=referral&utm_campaign=supporter" target="_blank"><img src="https://tabularis.dev/img/sponsors/openai_compact.svg" height="28" alt="OpenAI" /></a> **[OpenAI](https://openai.com/codex/?utm_source=tabularis&utm_medium=referral&utm_campaign=supporter)** — Supporting Tabularis through the Codex for Open Source program.
- <a href="https://m.do.co/c/f6ab3d158275?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor" target="_blank"><img src="https://tabularis.dev/img/sponsors/digitalocean_compact.png" height="28" alt="DigitalOcean" /></a> **[DigitalOcean](https://m.do.co/c/f6ab3d158275?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor)** — Simple, predictable cloud infrastructure for developers and growing teams.
- <a href="https://vercel.com/?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor" target="_blank"><img src="https://tabularis.dev/img/sponsors/vercel_compact.svg" height="28" alt="Vercel" /></a> **[Vercel](https://vercel.com/?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor)** — The platform for the modern web — ship, preview, and scale frontend apps with zero config.
- <a href="https://usero.io/?utm_source=tabularis&utm_medium=referral&utm_campaign=sponsor"
