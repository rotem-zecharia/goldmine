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
