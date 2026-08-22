# modelcontextprotocol/typescript-sdk

The official TypeScript SDK for Model Context Protocol servers and clients

## features

The Model Context Protocol (MCP) allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction.

This repository contains the TypeScript SDK implementation of the MCP specification. It runs on **Node.js**, **Bun**, and **Deno**, and ships:

- MCP **server** libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)
- MCP **client** libraries (transports, high-level helpers, OAuth helpers)
- Optional **middleware packages** for specific runtimes/frameworks (Express, Fastify, Hono, Node.js HTTP)
- Runnable **examples** (under [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples))

## installation

Here is what an MCP server looks like. This minimal example exposes a single `greet` tool over stdio:

```typescript
import { McpServer } from '@modelcontextprotocol/server';
import { StdioServerTransport } from '@modelcontextprotocol/server/stdio';
import * as z from 'zod/v4';

const server = new McpServer({ name: 'greeting-server', version: '1.0.0' });

server.registerTool(
    'greet',
    {
        description: 'Greet someone by name',
        inputSchema: z.object({ name: z.string() })
    },
    async ({ name }) => ({
        content: [{ type: 'text', text: `Hello, ${name}!` }]
    })
);

async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
}

main();
```

Ready to build something real? Follow the step-by-step tutorials:

- [Build your first server](docs/get-started/first-server.md) — a stdio weather-alert server, from `npm init` to a tool call
- [Build your first client](docs/get-started/first-client.md) — connect to that server, list its tools, and call them

For runnable, end-to-end examples beyond the tutorials, see:

- [`examples/README.md`](examples/README.md) — runnable, self-verifying client/server example pairs (one story per directory)
