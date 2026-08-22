# czlonkowski/n8n-mcp

A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you

## features

n8n-MCP serves as a bridge between n8n's workflow automation platform and AI models, enabling them to understand and work with n8n nodes effectively. It provides structured access to:

- **2,541 n8n nodes** - 832 core nodes + 1,709 community nodes (1,441 verified)
- **Node properties** - 99% coverage with detailed schemas
- **Node operations** - 66.5% coverage of available actions
- **Documentation** - 86% coverage from official n8n docs (including AI nodes)
- **AI tools** - 267 AI-capable tool variants detected with full documentation
- **Real-world examples** - 156 ranked configurations extracted from popular templates
- **Template library** - 2,352 workflow templates with 99.96% AI metadata coverage
- **Community nodes** - Search verified community integrations with `source` filter

## installation

**The fastest way to try n8n-MCP** - no installation, no configuration:

**[dashboard.n8n-mcp.com](https://dashboard.n8n-mcp.com)**

- Free tier: 100 tool calls/day
- Instant access: Start building workflows immediately
- Always up-to-date: Latest n8n nodes and templates
- No infrastructure: We handle everything

Just sign up, get your API key, and connect your MCP client.

**Want to self-host?** See the [Self-Hosting Guide](./docs/SELF_HOSTING.md) for npx, Docker, Railway, and local installation options.

## tools

- **Avoid when possible** - Prefer standard nodes
- **Only when necessary** - Use code node as last resort
- **AI tool capability** - ANY node can be an AI tool (not just marked ones)
