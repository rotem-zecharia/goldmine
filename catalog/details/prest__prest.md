# prest/prest

PostgreSQL ➕ REST, low-code, simplify and accelerate development, ⚡ instant, realtime, high-performance on any Postgres application, existing or new, MCP server

## installation

Install and run options (Docker, Homebrew, or Go) are documented in [Get pREST](https://docs.prestd.com/get-prest). Point pREST at Postgres (`PREST_PG_URL` or `pg.*` / `DATABASE_URL`), then call:

```http
GET /{database}/{schema}/{table}
```

See [Configuring pREST](https://docs.prestd.com/get-started/configuring-prest) for auth, ACL, custom queries, and MCP.
