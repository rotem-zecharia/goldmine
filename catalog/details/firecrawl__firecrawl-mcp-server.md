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

### Hosted MCP (keyless free tier)

Connect to the remote hosted server with no setup:

```
https://mcp.firecrawl.dev/v2/mcp
```

On the keyless free tier, `scrape`, `search`, and `parse` work without an API key (rate-limited). Other tools such as `crawl`, `map`, and `agent` still need a key.

Prefer OAuth or an API key whenever the human can sign up. It unlocks the full tool set and higher limits.

For an interactive account connection, configure your MCP client to use this server URL. This is an MCP endpoint, **not a browser page**; use the client's account-connection flow and do not add a second Firecrawl server entry when reconnecting:

```
https://mcp.firecrawl.dev/v2/mcp-oauth
```

For an API-key connection (for example, an unattended integration), keep the server URL as:

```
https://mcp.firecrawl.dev/v2/mcp
```

Then configure the client's secure header or secret setting with:

```
Authorization: Bearer <FIRECRAWL_API_KEY>
```

Never put an API key in the server URL. Never put an API key in an agent chat. Configure it directly in the client or secret manager. See the [hosted MCP setup guide](https://docs.firecrawl.dev/mcp-server) and the [agent onboarding guide](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for client-specific instructions.

#### Search-only endpoint

A read-only, search-only surface is also hosted at:

```
https://mcp.firecrawl.dev/v2/mcp-search
```

It exposes a fixed set of six read-only tools: `firecrawl_search` and the five `firecrawl_research_*` tools. It performs no page-content fetching and has its own OAuth identity; the full endpoint above is unchanged. See [docs/search-profile.md](docs/search-profile.md) for the full contract.

### Running with npx

```bash
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

### Manual Installation

```bash
npm install -g firecrawl-mcp
```

### Running on Cursor

Configuring Cursor 🖥️
Note: Requires Cursor version 0.45.6+
For the most up-to-date configuration instructions, please refer to the official Cursor documentation on configuring MCP servers:
[Cursor MCP Server Configuration Guide](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers)

To configure Firecrawl MCP in Cursor **v0.48.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add new global MCP server"
4. Enter the following code:
   ```json
   {
     "mcpServers": {
       "firecrawl-mcp": {
         "command": "npx",
         "args": ["-y", "firecrawl-mcp"],
         "env": {
           "FIRECRAWL_API_KEY": "YOUR-API-KEY"
         }
       }
     }
   }
   ```

To configure Firecrawl MCP in Cursor **v0.45.6**

1. Open Cursor Settings
2. Go to Features > MCP Servers
3. Click "+ Add New MCP Server"
4. Enter the following:
   - Name: "firecrawl-mcp" (or your preferred name)
   - Type: "command"
   - Command: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> If you are using Windows and are running into issues, try `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

Replace `your-api-key` with your Firecrawl API key. If you don't have one yet, you can create an account and get it from https://www.firecrawl.dev/app/api-keys

After adding, refresh the MCP server list to see the new tools. The Composer Agent will automatically use Firecrawl MCP when appropriate, but you can explicitly request it by describing your web scraping needs. Access the Composer via Command+L (Mac), select "Agent" next to the submit button, and enter your query.

### Running on Windsurf

Add this to your `./codeium/windsurf/model_config.json`:

```json
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Running with Streamable HTTP Local Mode

To run the server using Streamable HTTP locally instead of the default stdio transport:

```bash
env HTTP_STREAMABLE_SERVER=true FIRECRAWL_API_KE

## configuration

### Environment Variables

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
# Required for self-hosted
export FIRECRAWL_API_URL=https://firecrawl.your-domain.com

# Optional authentication for self-hosted
export FIRECRAWL_API_KEY=your-api-key  # If your instance requires auth
```

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

## How to Choose a Tool

Use this guide to select the right tool for your task:

- **If you know the exact URL you want:** use **scrape** (with JSON format for structured data)
- **If you have multiple known URLs:** call **scrape** for each URL. If you specifically need one bulk API operation, use the Firecrawl API batch endpoint outside MCP.
- **If you need to discover URLs on a site:** use **map**
- **If you want to search the web for info:** use **search**
- **If you have a programming question** (a library, an API contract, an error message, a known bug): use **developer search**
- **If you need scientific papers** (biomedical, life-science, clinical, or arXiv literature): use **research tools** — they search paper abstracts and full text. `search` with `categories: ["research"]` is a different thing: a website filter over ordinary web results.
- **If you need complex research across multiple unknown sources:** use **agent**
- **If you want to analyze a whole site or section:** use **crawl** (with limits!)
- **If you need interactive browser automation** (click, type, navigate): use **interact** with a URL for a fresh page, or **scrape** + **interact** when you already scraped the page or need tighter scrape control

### Quick Reference Table

| Tool         | Best for                                       | Returns                        |
| ------------ | ---------------------------------------------- | ------------------------------ |
| scrape       | Single page content                            | JSON (preferred) or markdown   |
| interact     | Interact with a URL or scraped page            | Execution result + scrapeId for URL mode |
| map          | Discovering URLs on a site                     | URL[]                          |
| crawl        | Multi-page extraction (with limits)            | final crawl status/data after internal polling |
| parse        | Files and hosted upload refs                   | markdown, JSON, or document output |
| search       | Web search for info                            | results[]                      |
| developer    | Programming questions over developer sources   | results[] with passages        |
| agent        | Complex multi-source research                  | JSON (structured data)         |
| monitor      | Recurring page checks                          | monitor/check metadata and diffs |
| research     | Paper and GitHub repository research           | research results and repo matches |

### Format Selection Guide

When using `scrape`, choose the right format:

- **JSON format (recommended for most cases):** Use when you need specific data from a page. Define a schema based on what you need to extract. This keeps responses small and avoids context window overflow.
- **Markdown format (use sparingly):** Only when you genuinely need the full page content, such as reading an entire article for summarization or analyzing page structure.

## Available Tools

### 1. Scrape Tool (`firecrawl_scrape`)

Scrape content from a single URL with advanced options.

**Best for:**

- Single page content extraction, when you know exactly which page contains the information.

**Not recommended for:**

- Extracting content from multiple pages (use repeated scrape calls for known URLs, or map + scrape to discover URLs first, or crawl for full page content)
- When you're unsure which page contains 
