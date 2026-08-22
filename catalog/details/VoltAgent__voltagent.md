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
});
```

Afterwards, navigate to your project and run:

```bash
npm run dev
```

When you run the dev command, tsx will compile and run your code. You should see the VoltAgent server startup message in your terminal:

```
══════════════════════════════════════════════════
VOLTAGENT SERVER STARTED SUCCESSFULLY
══════════════════════════════════════════════════
✓ HTTP Server: http://localhost:3141

Test your agents with VoltOps Console: https://console.voltagent.dev
══════════════════════════════════════════════════
```

Your agent is now running! To interact with it:

1. Open the Console: Click the [VoltOps LLM Observability Platform](https://console.voltagent.dev) link in your terminal output (or copy-paste it into your browser).
2. Find Your Agent: On the VoltOps LLM Observability Platform page, you should see your agent listed (e.g., "my-agent").
3. Open Agent Details: Click on your agent's name.
4. Start Chatting: On the agent detail page, click the chat icon in the bottom right corner to open the chat window.
5. Send a Message: Type a message like "Hello" and press Enter.

[![VoltAgent Demo](thumbnail.png)](https://github.com/user-attachments/assets/26340c6a-be34-48a5-9006-e822bf6098a7)

### Running Your First Workflow

Your new project also includes a powerful workflow engine.

The expense approval workflow demonstrates human-in-the-loop automation with suspend/resume capabilities:

```typescript
import { createWorkflowChain } from "@voltagent/core";
import { z } from "zod";

export const expenseApprovalWorkflow = createWorkflowChain({
  id: "expense-approval",
  name: "Expense Approval Workflow",
  purpose: "Process expense reports with manager approval for high amounts",

  input: z.object({
    employeeId: z.string(),
    amount: z.number(),
    category: z.string(),
    description: z.string(),
  }),
  result: z.object({
    status: z.enum(["approved", "rejected"]),
    approvedBy: z.string(),
    finalAmount: z.number(),
  }),
})
  // Step 1: Validate expense and check if approval needed
  .andThen({
    id: "check-approval-needed",
    resumeSchema: z.object({
      approved: z.boolean(),
      managerId: z.string(),
      comments: z.string().optional(),
      adjustedAmount: z.number().optional(),
    }),
    execute: async ({ data, suspend, resumeData }) => {
      // If we're resuming with manager's decision
      if (resumeData) {
        return {
          ...data,
          approved: resumeData.approved,
          approvedBy: resumeData.managerId,
          finalAmount: resumeData.adjustedAmount || data.amount,


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

### Observability & Tracing

Deep dive into agent execution flow with detailed traces and performance metrics.

<img alt="1" src="https://github.com/user-attachments/assets/21c6d05d-f333-4c61-9218-8862d16110fd" />

### Dashboard

Get a comprehensive overview of all your agents, workflows, and system performance metrics.

<img alt="dashboar" src="https://github.com/user-attachments/assets/c88a5543-219e-4cf0-8f41-14a68ca297fb" />

### Logs

Track detailed execution logs for every agent interaction and workflow step.

![VoltOps Logs](https://cdn.voltagent.dev/console/logs.png)

### Memory Management

Inspect and manage agent memory, context, and conversation history.

![VoltOps Memory Overview](https://cdn.voltagent.dev/console/memory.png)

### Traces

Analyze complete execution traces to understand agent behavior and optimize performance.

![VoltOps Traces](https://cdn.voltagent.dev/console/traces.png)

### Prompt Builder

Design, test, and refine prompts directly in the console.

<img  alt="prompts" src="https://github.com/user-attachments/assets/fb6d71eb-8f81-4443-a494-08c33ec9bcc4" />

### Deployment

Deploy your agents to production with one-click GitHub integration and managed infrastructure.

<img alt="deployment" src="https://github.com/user-attachments/assets/e329ab4b-7464-435a-96cc-90214e8a3cfa" />

📖 [VoltOps Deploy Documentation](https://voltagent.dev/docs/deployment/voltops/)

### Triggers & Actions

Automate agent workflows with webhooks, schedules, and custom triggers to react to external events.

