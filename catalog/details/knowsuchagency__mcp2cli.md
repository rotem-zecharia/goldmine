# knowsuchagency/mcp2cli

Turn any MCP, OpenAPI, or GraphQL server into a CLI — at runtime, with zero codegen

## installation

```bash
# Run directly without installing
uvx mcp2cli --help

# Or install globally
uv tool install mcp2cli
```

## AI Agent Skill

mcp2cli ships with an installable [skill](https://skills.sh) that teaches AI coding agents (Claude Code, Cursor, Codex) how to use it. Once installed, your agent can discover and call any MCP server or OpenAPI endpoint — and even generate new skills from APIs.

```bash
npx skills add knowsuchagency/mcp2cli --skill mcp2cli
```

After installing, try prompts like:
- `mcp2cli --mcp https://mcp.example.com/sse` — interact with an MCP server
- `mcp2cli create a skill for https://api.example.com/openapi.json` — generate a skill from an API

## tools

### MCP HTTP/SSE mode

```bash
# Connect to an MCP server over HTTP
mcp2cli --mcp https://mcp.example.com/sse --list

# Call a tool
mcp2cli --mcp https://mcp.example.com/sse search --query "test"

# With auth header
mcp2cli --mcp https://mcp.example.com/sse --auth-header "x-api-key:sk-..." \
  query --sql "SELECT 1"

# Force a specific transport (skip streamable HTTP fallback dance)
mcp2cli --mcp https://mcp.example.com/sse --transport sse --list

# Search tools by name or description (case-insensitive substring match)
mcp2cli --mcp https://mcp.example.com/sse --search "task"
```

`--search` implies `--list` and works across all modes (`--mcp`, `--spec`, `--graphql`, `--mcp-stdio`).

### OAuth authentication

APIs that require OAuth are supported out of the box — across MCP, OpenAPI, and GraphQL modes.
mcp2cli handles token acquisition, caching, and refresh automatically.

```bash
# Authorization code + PKCE flow (opens browser for login)
mcp2cli --mcp https://mcp.example.com/sse --oauth --list
mcp2cli --spec https://api.example.com/openapi.json --oauth --list
mcp2cli --graphql https://api.example.com/graphql --oauth --list

# Client credentials flow (machine-to-machine, no browser)
mcp2cli --spec https://api.example.com/openapi.json \
  --oauth-client-id "my-client-id" \
  --oauth-client-secret "my-secret" \
  list-pets

# With specific scopes
mcp2cli --graphql https://api.example.com/graphql --oauth --oauth-scope "read write" users

# Local spec file — use --base-url for OAuth discovery
mcp2cli --spec ./openapi.json --base-url https://api.example.com --oauth --list
```

Tokens are persisted in `~/.cache/mcp2cli/oauth/` so subsequent calls reuse existing tokens
and refresh automatically when they expire.

#### Headless hosts — no browser on the machine running mcp2cli

The default authorization-code flow starts a callback server on `127.0.0.1`, which only
works when the browser runs on the same machine. On a VPS over SSH or in a container,
add `--oauth-manual-callback`: mcp2cli prints the authorization URL instead of opening a
browser, and reads the redirect back from stdin.

```bash
mcp2cli --mcp https://mcp.linear.app/mcp --oauth --oauth-manual-callback --list
```

Open the printed URL in a browser on any machine, authorize, then paste the URL you land
on. That page will fail to load — nothing is listening on the loopback port — which is
expected; only its address matters, because it carries the `code` and `state` parameters.
PKCE and state verification are unchanged, so paste the URL unmodified.

## configuration

Sensitive values (`--auth-header` values, `--oauth-client-id`, `--oauth-client-secret`) support
`env:` and `file:` prefixes to avoid passing secrets as CLI arguments (which are visible in
process listings):

```bash
# Read from environment variable
mcp2cli --mcp https://mcp.example.com/sse \
  --auth-header "Authorization:env:MY_API_TOKEN" \
  --list

# Read from file
mcp2cli --mcp https://mcp.example.com/sse \
  --oauth-client-secret "file:/run/secrets/client_secret" \
  --oauth-client-id "my-client-id" \
  --list

# Works with secret managers that inject env vars
fnox exec -- mcp2cli --mcp https://mcp.example.com/sse \
  --oauth-client-id "env:OAUTH_CLIENT_ID" \
  --oauth-client-secret "env:OAUTH_CLIENT_SECRET" \
  --list
```

### MCP stdio mode

```bash
