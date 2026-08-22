# Effect-TS/effect

Build production-ready applications in TypeScript

## installation

```sh
npm install effect@rc
```

## requirements

- **TypeScript 5.9 or newer.** TypeScript 7 is recommended for the best performance and compatibility with [Effect's TypeScript tooling](https://github.com/Effect-TS/tsgo#installation).
- **Node.js 18 or newer** is the general minimum for running Effect on Node.js. Some integration packages require newer runtimes; for example, `@effect/sql-sqlite-node` requires Node.js 22.16 or newer.
- **Strict type-checking:** the `strict` flag must be enabled in your `tsconfig.json`.

## Effect v3

The Effect v3 source code is available on the [`v3`](https://github.com/Effect-TS/effect/tree/v3) branch, which is also where issues and pull requests meant for Effect v3 should be targeted.

## Packages

This monorepo contains the core `effect` package alongside integration packages that extend it. All v4 packages are published under the `rc` tag on npm.

| Package                                                               | Description                                              | API Reference                                                      |
| --------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------ |
| [`effect`](packages/effect)                                           | The core package                                         | [docs](https://effect.website/docs/v4/api/effect)                  |
| [`@effect/platform-browser`](packages/platform/browser)               | Platform services for the browser                        | [docs](https://effect.website/docs/v4/api/platform-browser)        |
| [`@effect/platform-bun`](packages/platform/bun)                       | Platform services for [Bun](https://bun.sh)              | [docs](https://effect.website/docs/v4/api/platform-bun)            |
| [`@effect/platform-deno`](packages/platform/deno)                     | Platform services for [Deno](https://deno.com)           | [docs](https://effect.website/docs/v4/api/platform-deno)           |
| [`@effect/platform-node`](packages/platform/node)                     | Platform services for [Node.js](https://nodejs.org)      | [docs](https://effect.website/docs/v4/api/platform-node)           |
| [`@effect/platform-node-shared`](packages/platform/node-shared)       | Shared services for Node.js-compatible runtimes          | [docs](https://effect.website/docs/v4/api/platform-node-shared)    |
| [`@effect/sql-clickhouse`](packages/sql/clickhouse)                   | SQL client for [ClickHouse](https://clickhouse.com)      | [docs](https://effect.website/docs/v4/api/sql-clickhouse)          |
| [`@effect/sql-d1`](packages/sql/d1)                                   | SQL client for Cloudflare D1                             | [docs](https://effect.website/docs/v4/api/sql-d1)                  |
| [`@effect/sql-libsql`](packages/sql/libsql)                           | SQL client for libSQL                                    | [docs](https://effect.website/docs/v4/api/sql-libsql)              |
| [`@effect/sql-mssql`](packages/sql/mssql)                             | SQL client for Microsoft SQL Server                      | [docs](https://effect.website/docs/v4/api/sql-mssql)               |
| [`@effect/sql-mysql2`](packages/sql/mysql2)                           | SQL client for MySQL                                     | [docs](https://effect.website/docs/v4/api/sql-mysql2)              |
| [`@effect/sql-pg`](packages/sql/pg)                                   | SQL client for PostgreSQL                                | [docs](https://effect.website/docs/v4/api/sql-pg)                  |
| [`@effect/sql-pglite`](packages/sql/pglite)                           | SQL client for [PGlite](https://pglite.dev)              | [docs](https://effect.website/docs/v4/api/sql-pglite)              |
| [`@effect/sql-sqlite-bun`](packages/sql/sqlite-bun)                   | SQL client for SQLite via `bun:sqlite`         
