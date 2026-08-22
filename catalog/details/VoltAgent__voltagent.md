# VoltAgent/voltagent

AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

## installation

Create a new VoltAgent project in seconds using the `create-voltagent-app` CLI tool:

```bash
npm create voltagent-app@latest
```

This command guides you through setup.

You'll see the starter code in `src/index.ts`, which now registers both an agent and a comprehensive workflow example found in `src/workflows/index.ts`.

```typescript
import { VoltAgent, Agent, Memory } from "@voltagent/core";
import { LibSQLMemoryAdapter } from "@voltagent/libsql";
import { createPinoLogger } from "@voltagent/logger";
import { honoServer } from "@voltagent/server-hono";
import { openai } from "@ai-sdk/openai";
import { expenseApprovalWorkflow } from "./workflows";
import { weatherTool } from "./tools";

// Create a logger instance
const logger = createPinoLogger({
  name: "my-agent-app",
  level: "info",
});

// Optional persistent memory (remove to use default in-memory)
const memory = new Memory({
  storage: new LibSQLMemoryAdapter({ url: "file:./.voltagent/memory.db" }),
});

// A simple, general-purpose agent for the project.
const agent = new Agent({
  name: "my-agent",
  instructions: "A helpful assistant that can check weather and help with various tasks",
  model: openai("gpt-4o-mini"),
  tools: [weatherTool],
  memory,
});

// Initialize VoltAgent with your agent(s) and workflow(s)
new VoltAgent({
  agents: {
    agent,
  },
  workflows: {
    expenseApprovalWorkflow,
  },
  server: honoServer(),
  logger,

## tools

For more examples, visit our [examples repository](https://github.com/VoltAgent/voltagent/tree/main/examples).

- **[Airtable Agent](https://voltagent.dev/recipes-and-guides/airtable-agent)** - React to new records and write updates back into Airtable with VoltOps actions.
- **[Slack Agent](https://voltagent.dev/recipes-and-guides/slack-agent)** - Respond to channel messages and reply via VoltOps Slack actions.
- **[ChatGPT App With VoltAgent](https://voltagent.dev/examples/agents/chatgpt-app)** - Deploy VoltAgent over MCP and connect to ChatGPT Apps.
- **[WhatsApp Order Agent](https://voltagent.dev/examples/agents/whatsapp-ai-agent)** - Build a WhatsApp chatbot that handles food orders through natural conversation. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-whatsapp))
- **[YouTube to Blog Agent](https://voltagent.dev/examples/agents/youtube-blog-agent)** - Convert YouTube videos into Markdown blog posts using a supervisor agent with MCP tools. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-youtube-to-blog))
- **[AI Ads Generator Agent](https://voltagent.dev/examples/agents/ai-instagram-ad-agent)** - Generate Instagram ads using BrowserBase Stagehand and Google Gemini AI. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-ad-creator))
- **[AI Recipe Generator Agent](https://voltagent.dev/examples/agents/recipe-generator)** - Create personalized cooking suggestions based on ingredients and preferences. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-recipe-generator) | [Video](https://youtu.be/KjV1c6AhlfY))
- **[AI Research Assistant Agent](https://voltagent.dev/examples/agents/research-assistant)** - Multi-agent research workflow for generating comprehensive reports. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-research-assistant) | [Video](https://youtu.be/j6KAUaoZMy4))

<h2 id="voltops-console">VoltOps Console: LLM Observability - Automation - Deployment</h2>

VoltOps Console is the platform side of VoltAgent, providing observability, automation, and deployment so you can monitor and debug agents in production with real-time execution traces, performance metrics, and visual dashboards.

🎬 [Try Live Demo](https://console.voltagent.dev/demo)

📖 [VoltOps Documentation](https://voltagent.dev/voltops-llm-observability-docs/)

🚀 [VoltOps Platform](https://voltagent.dev/voltops-llm-observability/)
