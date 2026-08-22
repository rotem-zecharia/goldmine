# simstudioai/sim

Sim is the collaborative workspace to build, deploy, and monitor AI agents and workflows. Used by 100,000+ builders.

## installation

### Cloud-hosted: [sim.ai](https://sim.ai)

<a href="https://sim.ai" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Open-sim.ai-3B3B3B?labelColor=1A1A1A" alt="Open sim.ai"></a>

### Self-hosted

```bash
npx sim-setup
```

Open [http://localhost:3000](http://localhost:3000)

<p align="center">
  <img src="apps/sim/public/static/readme-platform.png" alt="The Sim platform — chat on the left, the visual workflow builder on the right" width="100%"/>
</p>

## features

- Connect 1,000+ integrations and every major LLM
- Add Slack, Notion, HubSpot, Salesforce, databases, and more
- Build agents visually, conversationally, or with code
- Ingest files, knowledge bases, and structured table data
- Monitor runs, logs, schedules, and workflow activity

## One workspace, every surface

<p align="center">Chat and workflows are just the start — tables, files, and knowledge all live in the same workspace.</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="apps/sim/public/static/readme-tables.png" alt="Tables in Sim — structured data your agents can query" width="100%"/>
      <p align="center"><b>Tables</b> — a database, built in</p>
    </td>
    <td width="50%" valign="top">
      <img src="apps/sim/public/static/readme-files.png" alt="Files in Sim — documents for your team and every agent" width="100%"/>
      <p align="center"><b>Files</b> — one store for your team and every agent</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="apps/sim/public/static/readme-knowledge.png" alt="Knowledge bases in Sim — synced docs your agents can search" width="100%"/>
      <p align="center"><b>Knowledge</b> — your agents' memory</p>
    </td>
    <td width="50%" valign="top"></td>
  </tr>
</table>

## Self-hosting

**Requirements:** [Node.js 20+](https://nodejs.org/) and [Docker](https://www.docker.com/).

`npx sim-setup` is an interactive wizard that creates a small `sim/` deployment directory, provisions the database, generates secrets, writes `.env`, connects a Chat API key, and starts the published Sim images with Docker Compose. It does not clone the repository.

When it finishes, open [http://localhost:3000](http://localhost:3000).

Inside a cloned Sim repository, run `bun run sim-setup` to unlock the source-only local development and Kubernetes modes.

Reconfigure an optional capability without rerunning the full wizard:

```bash
npx sim-setup config
npx sim-setup add email
npx sim-setup add storage
npx sim-setup add sandbox
npx sim-setup add jobs
npx sim-setup add cache
npx sim-setup add knowledge
npx sim-setup add llm
npx sim-setup add integration slack
```

`npx sim-setup config` detects the effective local-dev, Docker Compose, or current-context
Helm configuration and reports configured, missing, or invalid capabilities and OAuth
integrations without printing credential values. This is separate from `npx sim-setup status`,
which reports whether installed services are running and healthy.

Manage your install from its directory:

```bash
npx sim-setup start | stop | restart   # bring your install up / down / cycle
npx sim-setup update                   # pull and apply Compose images
npx sim-setup status                   # what's installed and healthy
npx sim-setup logs                     # follow logs
npx sim-setup doctor                   # diagnose configuration problems
npx sim-setup down                     # remove containers (data kept)
npx sim-setup reset                    # archive .env and wipe managed data
```

The setup package detects how you're running and acts accordingly. Use `--dir <path>` to create or manage a deployment somewhere other than `./sim`.

Sim also supports local models via [Ollama](https://ollama.ai) and [vLLM](https://docs.vllm.ai/). See the [self-hosting docs](https://docs.sim.ai/self-hosting/docker) for details.

## tools

Chat is a Sim-managed service. `npx sim-setup` connects a Chat API key for you — sign in when it opens your browser and the key is stored automatically. To view, create, or revoke keys later, go to [sim.ai/selfhost/settings/chat-keys](https://sim.ai/selfhost/settings/chat-keys).

## configuration

See the [environment variables reference](https://docs.sim.ai/self-hosting/environment-variables) for the full list, or [`apps/sim/.env.example`](apps/sim/.env.example) for defaults.

## Tech Stack

<details>
<summary>Next.js · Bun · PostgreSQL · Drizzle · Better Auth · Tailwind — and the rest of the stack</summary>

- **Framework**: [Next.js](https://nextjs.org/) (App Router)
- **Runtime**: [Bun](https://bun.sh/)
- **Database**: PostgreSQL with [Drizzle ORM](https://orm.drizzle.team)
- **Authentication**: [Better Auth](https://better-auth.com)
- **Schema Validation**: [Zod](https://zod.dev)
- **UI**: [Shadcn](https://ui.shadcn.com/), [Tailwind CSS](https://tailwindcss.com)
- **Streaming Markdown**: [Streamdown](https://github.com/vercel/streamdown)
- **State Management**: [Zustand](https://zustand-demo.pmnd.rs/), [TanStack Query](https://tanstack.com/query)
- **Flow Editor**: [ReactFlow](https://reactflow.dev/)
- **Docs**: [Fumadocs](https://fumadocs.vercel.app/)
- **Monorepo**: [Turborepo](https://turborepo.org/)
- **Realtime**: [Socket.io](https://socket.io/)
- **Background Jobs**: [Trigger.dev](https://trigger.dev/)
- **Remote Code Execution**: [E2B](https://www.e2b.dev/)
- **Isolated Code Execution**: [isolated-vm](https://github.com/laverdet/isolated-vm)

</details>

## Contributing

We welcome contributions! Please see our [Contributing Guide](.github/CONTRIBUTING.md) for details.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

<p align="center">
  <img src="apps/sim/public/static/readme-built-by-sim-team.png" alt="Built by the Sim team in San Francisco" width="100%"/>
</p>
