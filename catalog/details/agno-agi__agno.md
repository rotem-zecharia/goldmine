# agno-agi/agno

Build, run, and manage agent platforms.

## features

- [Production API](https://docs.agno.com/runtime/serve-as-api). 50+ endpoints with SSE and websockets to build a product on top.
- [Storage](https://docs.agno.com/runtime/storage). Store sessions, memory, knowledge, and traces in your own database.
- [100+ integrations](https://docs.agno.com/tools/toolkits/overview). Connect to GitHub, Slack, Postgres, and more using pre-built toolkits.
- [Context Providers](https://docs.agno.com/runtime/context). Access live data from Slack, Drive, wikis, MCP, and custom sources.
- [Human approval](https://docs.agno.com/runtime/human-approval). Pause runs for user confirmation. Block tools that require admin approval.
- [Observability](https://docs.agno.com/runtime/observability). Monitor with OpenTelemetry tracing, run history, and audit logs.
- [Security](https://docs.agno.com/runtime/security-and-auth). Get JWT-based RBAC and multi-user, multi-tenant isolation out of the box.
- [Interfaces](https://docs.agno.com/runtime/interfaces). Expose your agents via Slack, Telegram, WhatsApp, Discord, AG-UI, A2A.
- [Scheduling](https://docs.agno.com/runtime/scheduling). Cron-based scheduling and background jobs with no external infrastructure.
- [Deploy anywhere](https://docs.agno.com/runtime/deploy). Run on any cloud platform that runs containers. Docker, Railway, AWS, GCP.

## Use Agno with your coding agent

Two options:

1. Recommended: Add Agno docs as an MCP server. Add [docs.agno.com/mcp](https://docs.agno.com/mcp) to your favourite coding agent.
2. Add Agno docs as an indexed source. In Cursor: Settings → Indexing & Docs → Add `https://docs.agno.com/llms-full.txt`. Also works in VSCode, Windsurf, and similar tools.

Read the full guide [here](https://docs.agno.com/coding-agents).

## Community

- [X](https://x.com/AgnoAgi): follow for releases and demos
- [Newsletter](https://www.agno.com/the-agno-loop-newsletter): monthly updates on what's shipping

## Contributing

See the [contributing guide](https://github.com/agno-agi/agno/blob/main/CONTRIBUTING.md).

## License

Agno is distributed under the [Apache-2.0 license](LICENSE).

## Telemetry

Agno sends a telemetry event per agent run so we know which model providers to prioritize. Prompts, messages, and outputs are never sent. Disable by setting `AGNO_TELEMETRY=false`.

<p align="right"><a href="#top">↑ Back to top</a></p>
