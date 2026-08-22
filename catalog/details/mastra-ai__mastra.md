# mastra-ai/mastra

Mastra is the modern TypeScript framework for AI-powered applications and agents.

## features

Purpose-built for TypeScript and designed around established AI patterns, Mastra gives you everything you need to build great AI applications out-of-the-box.

Some highlights include:

- [**Model routing**](https://mastra.ai/models) - Connect to 40+ providers through one standard interface. Use models from OpenAI, Anthropic, Gemini, and more.

- [**Agents**](https://mastra.ai/docs/agents/overview) - Build autonomous agents that use LLMs and tools to solve open-ended tasks. Agents reason about goals, decide which tools to use, and iterate internally until the model emits a final answer or an optional stopping condition is met.

- [**Workflows**](https://mastra.ai/docs/workflows/overview) - When you need explicit control over execution, use Mastra's graph-based workflow engine to orchestrate complex multi-step processes. Mastra workflows use an intuitive syntax for control flow (`.then()`, `.branch()`, `.parallel()`).

- [**Human-in-the-loop**](https://mastra.ai/docs/workflows/suspend-and-resume) - Suspend an agent or workflow and await user input or approval before resuming. Mastra uses [storage](https://mastra.ai/docs/server-db/storage) to remember execution state, so you can pause indefinitely and resume where you left off.

- **Context management** - Give your agents the right context at the right time. Provide [conversation history](https://mastra.ai/docs/memory/conversation-history), [retrieve](https://mastra.ai/docs/rag/overview) data from your sources (APIs, databases, files), and add human-like memory with [Observational Memory](https://mastra.ai/docs/memory/observational-memory) so your agents behave coherently.

- **Integrations** - Bundle agents and workflows into existing React, Next.js, or Node.js apps, or ship them as standalone endpoints. When building UIs, integrate with agentic libraries like Vercel's AI SDK UI and CopilotKit to bring your AI assistant to life on the web.

- [**MCP servers**](https://mastra.ai/docs/tools-mcp/mcp-overview) - Author Model Context Protocol servers, exposing agents, tools, and other structured resources via the MCP interface. These can then be accessed by any system or agent that supports the protocol.

- **Production essentials** - Shipping reliable agents takes ongoing insight, evaluation, and iteration. With built-in [evals](https://mastra.ai/docs/evals/overview) and [observability](https://mastra.ai/docs/observability/overview), Mastra gives you the tools to observe, measure, and refine continuously.
