# upstash/context7

Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors

## installation

> [!NOTE]
> **API Key Recommended**: Get a free API key at [context7.com/dashboard](https://context7.com/dashboard) for higher rate limits.

Set up Context7 for your coding agents with a single command. The `ctx7` CLI requires Node.js 18 or newer.

```bash
npx ctx7 setup
```

Authenticates via OAuth, generates an API key, and installs the appropriate skill. You can choose between CLI + Skills or MCP mode. Use `--cursor`, `--claude`, or `--opencode` to target a specific agent.

To remove the generated setup later, run `npx ctx7 remove`. If you globally installed the CLI with `npm install -g ctx7`, remove that package separately with `npm uninstall -g ctx7`.

To configure manually, use the Context7 server URL `https://mcp.context7.com/mcp` with your MCP client and pass your API key via the `Authorization: Bearer YOUR_API_KEY` header. See the link below for client-specific setup instructions.

**[Manual Installation / Other Clients →](https://context7.com/docs/resources/all-clients)**

## tools

- `ctx7 library <name> <query>`: Searches the Context7 index by library name and returns matching libraries with their IDs.
- `ctx7 docs <libraryId> <query>`: Retrieves documentation for a library using a Context7-compatible library ID (e.g., `/mongodb/docs`, `/vercel/next.js`).
