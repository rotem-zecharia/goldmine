# firecrawl/firecrawl-mcp-server

🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

## features

- Search the web and get full page content
- Search an index built for coding agents: GitHub issues, merged pull requests, READMEs, and docs
- Scrape any URL into clean, structured data
- Interact with pages — click, navigate, and operate
- Deep research with autonomous agent
- Automatic retries and rate limiting
- Cloud and self-hosted support
- SSE support

> Play around with [our MCP Server on MCP.so's playground](https://mcp.so/playground?server=firecrawl-mcp-server) or on [Klavis AI](https://www.klavis.ai/mcp-servers).

## installation

```bash
npm install -g firecrawl-mcp
```

## configuration

#### Required for Cloud API

- `FIRECRAWL_API_KEY`: Your Firecrawl API key
  - Required when using cloud API (default)
  - Optional when using self-hosted instance with `FIRECRAWL_API_URL`
- `FIRECRAWL_API_URL` (Optional): Custom API endpoint for self-hosted instances
  - Example: `https://firecrawl.your-domain.com`
  - If not provided, the cloud API will be used (requires API key)

#### MCP OAuth (Bearer access tokens)

Hosted Firecrawl can issue OAuth **access tokens** (`fco_…`) via the authorization server on [firecrawl.dev](https://firecrawl.dev). This MCP server forwards whichever credential it resolves to the Firecrawl API as `Authorization: Bearer …`.

- **HTTP stream transports** (`CLOUD_SERVICE=true`, `HTTP_STREAMABLE_SERVER=true`, or `SSE_LOCAL=true`): Clients should send `Authorization: Bearer <fco_access_token>` on MCP requests. An OAuth bearer token takes precedence over `x-firecrawl-api-key` / `x-api-key` when both are present.
- **stdio:** Use `FIRECRAWL_OAUTH_TOKEN` for a static access token, or keep using `FIRECRAWL_API_KEY` for an API key.

Use **access** tokens (`fco_…`) only. Refresh tokens (`fcr_…`) must be exchanged at the token endpoint, not passed to the scrape/search API.

#### Search-only surface (hosted)

In hosted mode (`CLOUD_SERVICE=true`) a second in-process instance serves the [search-only endpoint](#search-only-endpoint). The bundled service has a fixed deployment contract: nginx routes `/v2/mcp-search` to the instance on local port `3001`, and the OAuth protected-resource identifier is `https://mcp.firecrawl.dev/v2/mcp-search`.

`FIRECRAWL_MCP_SEARCH_ENABLED` (default `true`) is the supported operational toggle; set it to `false` to prevent the search instance from starting. The Node process also accepts `FIRECRAWL_MCP_SEARCH_PORT`, `FIRECRAWL_MCP_SEARCH_ENDPOINT`, and `FIRECRAWL_MCP_SEARCH_RESOURCE_URL` for isolated tests. Those overrides do not reconfigure the bundled nginx routes or the authorization server allowlist and must not be used independently in the hosted deployment.

The search instance requires authentication for every request (including `tools/list`) and rejects OAuth tokens whose audience does not match its own resource.

## tools

For cloud API usage:

```bash
export FIRECRAWL_API_KEY=your-api-key
```

For self-hosted instance:

```bash
