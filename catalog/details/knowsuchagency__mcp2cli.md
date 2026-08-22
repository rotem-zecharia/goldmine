# knowsuchagency/mcp2cli

Turn any MCP, OpenAPI, or GraphQL server into a CLI — at runtime, with zero codegen

## installation

```bash

## tools

mcp2cli --mcp https://mcp.example.com/sse --search "task"
```

`--search` implies `--list` and works across all modes (`--mcp`, `--spec`, `--graphql`, `--mcp-stdio`).

## configuration

Sensitive values (`--auth-header` values, `--oauth-client-id`, `--oauth-client-secret`) support
`env:` and `file:` prefixes to avoid passing secrets as CLI arguments (which are visible in
process listings):

```bash
