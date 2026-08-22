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

## Support This Project

<div align="center">
  <a href="https://github.com/sponsors/czlonkowski">
    <img src="https://img.shields.io/badge/Sponsor-❤️-db61a2?style=for-the-badge&logo=github-sponsors" alt="Sponsor n8n-mcp" />
  </a>
</div>

**n8n-mcp** started as a personal tool but now helps tens of thousands of developers automate their workflows efficiently. Maintaining and developing this project competes with my paid work. Your sponsorship helps me dedicate focused time to new features, respond quickly to issues, keep documentation up-to-date, and ensure compatibility with latest n8n releases. **[Become a sponsor](https://github.com/sponsors/czlonkowski)**

## Important Safety Warning

**NEVER edit your production workflows directly with AI!** Always:
- Make a copy of your workflow before using AI tools
- Test in development environment first
- Export backups of important workflows
- Validate changes before deploying to production

AI results can be unpredictable. Protect your work!

## installation

**The fastest way to try n8n-MCP** - no installation, no configuration:

**[dashboard.n8n-mcp.com](https://dashboard.n8n-mcp.com)**

- Free tier: 100 tool calls/day
- Instant access: Start building workflows immediately
- Always up-to-date: Latest n8n nodes and templates
- No infrastructure: We handle everything

Just sign up, get your API key, and connect your MCP client.

**Want to self-host?** See the [Self-Hosting Guide](./docs/SELF_HOSTING.md) for npx, Docker, Railway, and local installation options.

## n8n Integration

Want to use n8n-MCP with your n8n instance? Check out our comprehensive [n8n Deployment Guide](./docs/N8N_DEPLOYMENT.md) for:
- Local testing with the MCP Client Tool node
- Production deployment with Docker Compose
- Cloud deployment on Hetzner, AWS, and other providers
- Troubleshooting and security best practices

### Cloudflare Access Authentication

If your n8n instance sits behind Cloudflare Access (Zero Trust), provide your service token so n8n-MCP can authenticate:

- `N8N_CF_CLIENT_ID` - Cloudflare Access Client ID
- `N8N_CF_CLIENT_SECRET` - Cloudflare Access Client Secret

When set, these are sent as `CF-Access-Client-Id` / `CF-Access-Client-Secret` headers on n8n API requests, version/health probes, and webhook executions. The token is confined to the `N8N_API_URL` origin — webhook calls to a different host (e.g. a split `WEBHOOK_URL` origin) do not receive it, to avoid leaking the token.

## Connect your IDE

n8n-MCP works with multiple AI-powered IDEs and tools:

- [Claude Code](./docs/CLAUDE_CODE_SETUP.md) - Quick setup for Claude Code CLI
- [Visual Studio Code](./docs/VS_CODE_PROJECT_SETUP.md) - VS Code with GitHub Copilot integration
- [Cursor](./docs/CURSOR_SETUP.md) - Step-by-step Cursor IDE setup
- [Windsurf](./docs/WINDSURF_SETUP.md) - Windsurf integration with project rules
- [Codex](./docs/CODEX_SETUP.md) - Codex integration guide
- [Antigravity](./docs/ANTIGRAVITY_SETUP.md) - Antigravity integration guide

## Add Claude Skills (Optional)

Supercharge your n8n workflow building with specialized skills that teach AI how to build production-ready workflows!

[![n8n-mcp Skills Setup](./docs/img/skills.png)](https://www.youtube.com/watch?v=e6VvRqmUY2Y)

Learn more: [n8n-skills repository](https://github.com/czlonkowski/n8n-skills)

## Claude Project Setup

For the best results when using n8n-MCP with Claude Projects, use these enhanced system instructions:

````markdown
You are an expert in n8n automation software using n8n-MCP tools. Your role is to design, build, and validate n8n workflows with maximum accuracy and efficiency.

## Core Principles

### 1. Silent Execution
CRITICAL: Execute tools without commentary. Only respond AFTER all tools complete.

### 2. Parallel Execution
When operations are independent, execute them in parallel for maximum performance.

### 3. Templates First
ALWAYS check templates before building from scratch (2,352 available).

### 4. Multi-Level Validation
Use validate_node(mode='minimal') → validate_node(mode='full') → validate_workflow pattern.

### 5. Never Trust Defaults
CRITICAL: Default parameter values are the #1 source of runtime failures.
ALWAYS explicitly configure ALL parameters that control node behavior.

## Workflow Process

1. **Start**: Call `tools_documentation()` for best practices

2. **Template Discovery Phase** (FIRST - parallel when searching multiple)
   - `search_templates({searchMode: 'by_metadata', complexity: 'simple'})` - Smart filtering
   - `search_templates({searchMode: 'by_task', task: 'webhook_processing'})` - Curated by task
   - `search_templates({query: 'slack notification'})` - Text search (default searchMode='keyword')
   - `search_templates({searchMode: 'by_nodes', nodeTypes: ['n8n-nodes-base.slack']})` - By node type

   **Filtering strategies**:
   - Beginners: `complexity: "simple"` + `maxSetupMinutes: 30`
   - By role: `targetAudience: "marketers"` | `"developers"` | `"analysts"`
   - By time: `maxSetupMinutes: 15` 

## tools

- **Avoid when possible** - Prefer standard nodes
- **Only when necessary** - Use code node as last resort
- **AI tool capability** - ANY node can be an AI tool (not just marked ones)

### Most Popular n8n Nodes (for get_node):

1. **n8n-nodes-base.code** - JavaScript/Python scripting
2. **n8n-nodes-base.httpRequest** - HTTP API calls
3. **n8n-nodes-base.webhook** - Event-driven triggers
4. **n8n-nodes-base.set** - Data transformation
5. **n8n-nodes-base.if** - Conditional routing
6. **n8n-nodes-base.manualTrigger** - Manual workflow execution
7. **n8n-nodes-base.respondToWebhook** - Webhook responses
8. **n8n-nodes-base.scheduleTrigger** - Time-based triggers
9. **@n8n/n8n-nodes-langchain.agent** - AI agents
10. **n8n-nodes-base.googleSheets** - Spreadsheet integration
11. **n8n-nodes-base.merge** - Data merging
12. **n8n-nodes-base.switch** - Multi-branch routing
13. **n8n-nodes-base.telegram** - Telegram bot integration
14. **@n8n/n8n-nodes-langchain.lmChatOpenAi** - OpenAI chat models
15. **n8n-nodes-base.splitInBatches** - Batch processing
16. **n8n-nodes-base.openAi** - OpenAI legacy node
17. **n8n-nodes-base.gmail** - Email automation
18. **n8n-nodes-base.function** - Custom functions
19. **n8n-nodes-base.stickyNote** - Workflow documentation
20. **n8n-nodes-base.executeWorkflowTrigger** - Sub-workflow calls

**Note:** LangChain nodes use the `@n8n/n8n-nodes-langchain.` prefix, core nodes use `n8n-nodes-base.`

````

Save these instructions in your Claude Project for optimal n8n workflow assistance with intelligent template discovery.

## Available MCP Tools

### Core Tools (7 tools)
- **`tools_documentation`** - Get documentation for any MCP tool (START HERE!)
- **`search_nodes`** - Full-text search across all nodes. Use `source: 'community'|'verified'` for community nodes, `includeExamples: true` for configs
- **`get_node`** - Unified node information tool with multiple modes:
  - **Info mode** (default): `detail: 'minimal'|'standard'|'full'`, `includeExamples: true`
  - **Docs mode**: `mode: 'docs'` - Human-readable markdown documentation
  - **Property search**: `mode: 'search_properties'`, `propertyQuery: 'auth'`
  - **Versions**: `mode: 'versions'|'compare'|'breaking'|'migrations'`
- **`validate_node`** - Unified node validation:
  - `mode: 'minimal'` - Quick required fields check (<100ms)
  - `mode: 'full'` - Comprehensive validation with profiles (minimal, runtime, ai-friendly, strict)
- **`validate_workflow`** - Complete workflow validation including AI Agent validation
- **`search_templates`** - Unified template search:
  - `searchMode: 'keyword'` (default) - Text search with `query` parameter
  - `searchMode: 'by_nodes'` - Find templates using specific `nodeTypes`
  - `searchMode: 'by_task'` - Curated templates for common `task` types
  - `searchMode: 'by_metadata'` - Filter by `complexity`, `requiredService`, `targetAudience`
- **`get_template`** - Get complete workflow JSON (modes: nodes_only, structure, full)

### n8n Management Tools (16 tools - Requires API Configuration)
These tools require `N8N_API_URL` and `N8N_API_KEY` in your configuration.

#### Workflow Management
- **`n8n_create_workflow`** - Create new workflows with nodes and connections
- **`n8n_get_workflow`** - Unified workflow retrieval (modes: full, details, structure, minimal)
- **`n8n_update_full_workflow`** - Update entire workflow (complete replacement)
- **`n8n_update_partial_workflow`** - Update workflow using diff operations
- **`n8n_delete_workflow`** - Delete workflows permanently
- **`n8n_list_workflows`** - List workflows with filtering and pagination
- **`n8n_validate_workflow`** - Validate workflows in n8n by ID
- **`n8n_autofix_workflow`** - Automatically fix common workflow errors
- **`n8n_workflow_versions`** - Manage version history and rollback
- **`n8n_deploy_template`** - Deploy templates from n8n.io directly to your instance with auto-fix

#### Execution Management
- **`n8n_test_workflow`** - Test/trigger workflow exec
