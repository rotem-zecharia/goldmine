# ComposioHQ/composio

Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.

## installation

Create a session for a user, hand its tools to your agent, and let the agent take action across 1000+ apps. Grab a `COMPOSIO_API_KEY` from the [dashboard](https://dashboard.composio.dev/settings) first.

### TypeScript

```bash
npm install @composio/core @composio/openai-agents @openai/agents
```

> `@composio/core` intentionally packages its TypeScript source and SDK docs so the installed package is inspectable to coding agents. If you want a smaller install with the same API, use [`@composio/slim`](ts/packages/slim).

```typescript
import { Composio } from "@composio/core";
import { OpenAIAgentsProvider } from "@composio/openai-agents";
import { Agent, run } from "@openai/agents";

const composio = new Composio({ provider: new OpenAIAgentsProvider() });

// Each session is scoped to one of your users
const session = await composio.create("user_123");
const tools = await session.tools();

const agent = new Agent({
  name: "Personal Assistant",
  instructions: "You are a helpful assistant. Use Composio tools to take action.",
  tools,
});

const result = await run(agent, "Summarize my emails from today");
console.log(result.finalOutput);
```

### Python

```bash
pip install composio composio-openai-agents openai-agents
```

```python
from composio import Composio
from composio_openai_agents import OpenAIAgentsProvider
from agents import Agent, Runner

composio = Composio(provider=OpenAIAgentsProvider())

# Each session is scoped to one of your users
session = composio.create(user_id="user_123")
tools = session.tools()

agent = Agent(
    name="Personal Assistant",
    instructions="You are a helpful assistant. Use Composio tools to take action.",
    tools=tools,
)

result = Runner.run_sync(starting_agent=agent, input="Summarize my emails from today")
print(result.final_output)
```

By default a session gets meta tools that discover, authenticate, and execute app tools at runtime, so you don't load hundreds of tool definitions into context. Store `session.session_id` and reuse it with `composio.use()` across turns. See [what a session is](https://docs.composio.dev/docs/how-composio-works) and [configuring sessions](https://docs.composio.dev/docs/configuring-sessions) for restricting toolkits, auth configs, and connected accounts.

**Prefer MCP?** Every session also exposes a hosted MCP endpoint. Pass `mcp: true` to `composio.create()` and point Claude, Cursor, or any MCP client at `session.mcp.url`. See [sessions via MCP](https://docs.composio.dev/docs/sessions-via-mcp).

## CLI

The `composio` CLI runs Composio from your shell and gives coding agents like Claude Code a local tool surface.

```bash
curl -fsSL https://composio.dev/install | sh
```

The installer puts `composio` on your `PATH` for future terminals. Open a new terminal, then run `composio login`. See [INSTALL.md](INSTALL.md) for shell setup overrides, including `COMPOSIO_INSTALL_SHELL=none` for install-only runs.

Use `composio search` to find tools, `composio execute` to run them, `composio link` to connect accounts, and `composio run` to script workflows in TypeScript. See the [CLI docs](https://docs.composio.dev/docs/cli).

## Providers

A provider adapts Composio tools to your agent framework's native tool format:

| Provider | TypeScript | Python |
|----------|:----------:|:------:|
| OpenAI | [`@composio/openai`](ts/packages/providers/openai) | [`composio-openai`](python/providers/openai) |
| OpenAI Agents | [`@composio/openai-agents`](ts/packages/providers/openai-agents) | [`composio-openai-agents`](python/providers/openai_agents) |
| Anthropic | [`@composio/anthropic`](ts/packages/providers/anthropic) | [`composio-anthropic`](python/providers/anthropic) |
| Claude Agent SDK | [`@composio/claude-agent-sdk`](ts/packages/providers/claude-agent-sdk) | [`composio-claude-agent-sdk`](python/providers/claude_agent_sdk) |
| Vercel AI SDK | [`@composio/vercel`](ts/packages/providers/vercel) | — |
| Google GenAI | [`@composio/google`](ts/packages/providers/google) |
