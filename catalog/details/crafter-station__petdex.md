# crafter-station/petdex

A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more.

## installation

Follow this checklist to get a pet installed, visible in Codex, and connected to the desktop app.

1. Install a known pet:

```sh
npx petdex install boba
```

You should see `~/.petdex/pets/boba/` with `pet.json` and a spritesheet.

2. Get the desktop app from [petdex.dev/download](https://petdex.dev/download). It
   runs on macOS, Linux and Windows.

3. Open it, then hit <kbd>Cmd</kbd>+<kbd>,</kbd> over the pet to open Settings.
   Pick your pet under **Pets**, and connect your coding agents under **Agents**
   with one click each. No terminal involved.

The pet floats above your workspace and animates on every tool call your agent
makes.

## For users

| You want to... | Do this |
| --- | --- |
| Browse pets | Visit [petdex.dev](https://petdex.dev) |
| Install a pet | `npx petdex install <slug>` |
| Switch active mascot | Open Settings in the desktop app (<kbd>Cmd</kbd>+<kbd>,</kbd>) |
| Run the desktop floater | Download it from [petdex.dev/download](https://petdex.dev/download) |
| Make a pet | Use the `hatch-pet` skill inside Codex, or build one with the [Petdex creator tools](https://petdex.dev/create) |
| Submit a pet | `npx petdex submit ./my-pet/` or drop it through the web submitter |
| Join the community | [Discord](https://discord.gg/byhubdyBTe) |

Full CLI reference: [`packages/petdex-cli/README.md`](./packages/petdex-cli/README.md).

## For builders

If you want to build on top of Petdex (a desktop client, a wearable, an SDK, a Discord bot, anything), you have two stable surfaces:

- **The HTTP API.** `petdex.dev/api/manifest` returns every approved pet with its slug, spritesheet URL, animation states, and metadata.
- **The pet package format.** Every pet is a `pet.json` plus a `spritesheet.{webp,png}` rendered as an 8x9 grid of 192x208 frames, or the v2 8x11 grid.

21 open-source and source-available projects already build on these. See [petdex.dev/built-with](https://petdex.dev/built-with) for the catalog, then [submit yours via the issue template](https://github.com/crafter-station/petdex/issues/new?template=built-with.yml).

## Architecture

```text
crafter-station/petdex
├── src/
│   ├── app/[locale]/          Public site: gallery, /pets/<slug>, /collections, /built-with, /community, /create, /download, /submit, /u/<handle>, ...
│   ├── app/api/cli/           CLI endpoints: OAuth config, submit (zip → presigned R2), dedup check, register
│   ├── app/api/manifest/      Public manifest: every approved pet with its spritesheet URL
│   ├── app/api/admin/         Admin review surface for submissions, edits, collection requests
│   └── lib/db/schema.ts       Drizzle schema (Postgres)
├── packages/
│   ├── petdex-cli/            npm `petdex` catalog client (auth, list, install, submit)
│   ├── petdex-desktop-native/ Native SDK floating mascot for macOS, Linux and Windows
│   ├── petdex-desktop-windows/ Legacy Tauri Windows implementation (not the release path)
│   └── discord-bot/           Discord.js bot for the Petdex server
├── public/built-with/         Screenshots for the community page
├── public/brand/              Logos, OS icons, Discord icon
└── drizzle/                   SQL migrations (Postgres schema history)
```

**Web stack**: Next.js 16, React 19, Tailwind, Drizzle, Postgres, Redis, Clerk, R2.<br />
**CLI**: Bun + TypeScript, ships as a single npm binary. Auth via Clerk OAuth + PKCE.<br />
**Desktop**: Native SDK app with an in-process Zig hook server on `127.0.0.1:7777`. The current release path has no WebView or Node sidecar.

## Develop locally

Two paths are supported.

| Goal | Command | Setup |
| --- | --- | --- |
| Local full stack | `bun run dev:docker` | Docker or Podman, ~30s warm-up. |
| Run against real services | `bun run dev` | `.env.local` filled (maintainers only). |

```sh
git clone https://github.com/crafter-station/petdex.git
cd petdex
bun install
bun run dev:docker
```

Open [localhost:3000](http://localhost:3000). Full guide in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Pet pac
