# mcp-use/mcp-use

The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.

## installation

The scaffold gives you the server, TypeScript configuration, development scripts, Inspector, and a React view pipeline. Start it once and the MCP endpoint also serves a client-ready landing page with its connection URL and setup instructions.

Replace its `index.ts` with a view-bound tool like this:

<table><tr><td>
<details>
<summary><strong><code>index.ts</code></strong> — Server entry file for tool definition and metadata</summary>

```typescript
import { MCPServer } from "mcp-use";
import { z } from "zod";

const server = new MCPServer({
  name: "weather-app",
  title: "Weather App",
  version: "1.0.0",
});

const weatherInput = z.object({
  city: z.string().describe("City to look up"),
});

const weatherOutput = z.object({
  city: z.string(),
  temperature: z.number(),
  conditions: z.string(),
});

export const getWeather = server.tool(
  {
    name: "get-weather",
    title: "Get weather",
    description: "Get the current weather for a city",
    inputSchema: weatherInput,
    outputSchema: weatherOutput,
    view: { name: "weather-card" },
    annotations: {
      readOnlyHint: true,
      destructiveHint: false,
      openWorldHint: true,
    },
  },
  async ({ city }) => {
    const weather = {
      city,
      temperature: 22,
      conditions: "Sunny",
    };

    return {
      content: [
        {
          type: "text",
          text: `Weather in ${city}: ${weather.conditions}, ${weather.temperature}°C`,
        },
      ],
      structuredContent: weather,
    };
  },
);

export default server;
```

</details>
</td></tr></table>

[Explore MCP server tools →](https://mcp-use.com/docs/typescript/server/tools)

## tools

Create `views/weather-card/view.tsx`. The directory name matches `view.name` on the tool:

<table><tr><td>
<details>
<summary><strong><code>view.tsx</code></strong> — Return a view from your tools: React weather card</summary>

```tsx
import { useCallTool, useToolContext } from "mcp-use/react";

export default function WeatherCard() {
  const { status, toolOutput, toolInput } =
    useToolContext<"get-weather">();
  const refresh = useCallTool("get-weather");

  if (status === "pending") {
    return <p>Checking the weather in {toolInput?.city ?? "your city"}…</p>;
  }
  if (status === "error") return <p>Could not load the weather.</p>;

  const weather = refresh.data?.structuredContent ?? toolOutput;

  return (
    <main style={{ padding: 24 }}>
      <h2>{weather.city}</h2>
      <p>
        {weather.temperature}°C · {weather.conditions}
      </p>
      <button
        disabled={refresh.isPending}
        onClick={() => void refresh.callTool({ city: weather.city })}
      >
        {refresh.isPending ? "Refreshing…" : "Refresh"}
      </button>
      {refresh.error && <p>{refresh.error.message}</p>}
    </main>
  );
}
```

</details>
</td></tr></table>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-use/mcp-use/main/static/readme/chatgpt-hello-world.jpg" alt="Hello World MCP App rendered in a ChatGPT conversation" width="100%" />
  <br />
  <sub>Build interactive UI experiences within ChatGPT with mcp-use.</sub>
</p>

[Build your first MCP App →](https://mcp-use.com/docs/typescript/mcp-apps/quickstart)

## Build

Create the production build:

```bash
npm run build
```

## Inspect

Start development mode to serve the MCP endpoint at [`http://localhost:3000/mcp`](http://localhost:3000/mcp). The Inspector is automatically available at [`http://localhost:3000/mcp/inspector`](http://localhost:3000/mcp/inspector):

```bash
npm run dev
```

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-use/mcp-use/main/static/readme/inspector-hello-world.jpg" alt="Hello World MCP App rendered in the mcp-use Inspector" width="100%" />
  <br />
  <sub>Invoke tools, validate inputs, and inspect interactive Views in the same development loop.</sub>
</p>

Start a tunnel from the Inspector UI or run `mcp-use dev --tunnel` to get a public URL for your local MCP server and test it with ChatGPT and Claude before deployment. [Learn more about tunneling →](https://docs.mcp-use.com/tunneling)

Inspect the same server headlessly from the terminal, invoke representative tools, and capture a View screenshot:

```bash
npm install --save-dev @mcp-use/client
npx mcp-use client connect local http://localhost:3000/mcp
npx mcp-use client local tools list
npx mcp-use client local tools call get-weather city=Tokyo
npx mcp-use screenshot \
  --server local \
  --tool get-weather \
  city=Tokyo \
  --output weather-card.png
```

## Deploy

Ship to [Manufact](https://manufact.com) and get observability, analytics, evals, submission readiness, and Git-based preview environments for free.

```bash
npm run deploy
```

Prefer to run it yourself? Follow the [self-hosting guide →](https://docs.mcp-use.com/typescript/server/deployment/runtime-patterns).

## How mcp-use compares

mcp-use builds on the official TypeScript SDK v2 and adds first-class Views, typed tool-to-UI contracts, an optimized stateless runtime, the Inspector, screenshot verification, agent-first CLI workflows, and deployment.

```mermaid
block-beta
  columns 7

  metric["Metric"] mcp["mcp-use v2"] fastmcp["FastMCP TS"] official["Official SDK v2*"] xmcp["xmcp"] skybridge["Skybridge"] handler["mcp-handler"]

  speed["Speed"] speedMcp["10,982 ops/s"] speedFast["6,628 ops/s"] speedOfficial["8,050 ops/s"] speedXmcp["6,585 ops/s"] speedSkybridge["8,116 ops/s"] speedHandler["6,324 ops/s"]
  install["MCP App<br/>dev stack"] installMcp["74.4 MiB"] installFast["122.5 MiB"] installOfficial["99.0 MiB"] installXmcp["121.9 MiB"] installSkybridge["137.5 MiB"] installHandler["388.0
