# nrwl/nx

The Monorepo Platform that amplifies both developers and AI agents. Nx optimizes your builds, scales your CI, and fixes failed PRs automatically. Ship in half the time.

## installation

Visit the [Nx quickstart docs](https://nx.dev/docs/quickstart) to get started.

## features

- **Incremental by design -** Run `npx nx init` in any npm/pnpm/yarn workspace. Nx picks up your existing `package.json` scripts, caches their outputs, and runs only what's
  affected. No changes to your setup required.
- **AI-native tooling -** The Nx CLI is optimized for autonomous AI agents so they get the context they need and can operate just like a human. [Learn more &raquo;](https://github.com/nrwl/nx-ai-agents-config)
- **Polyglot plugin system -** Optional plugins auto-discover tasks, configure cache inputs/outputs, and scaffold code based on your actual tooling. Works with Vite, Webpack, Jest, Vitest, ESLint, Gradle, Maven, .NET, Go, and [more](https://nx.dev/technologies).
- **Integrated CI solution -** [Connect Nx to your CI provider](https://nx.dev/ci/intro/ci-with-nx) (GitHub Actions, GitLab, Azure, etc.) to enable remote caching, task distribution across machines, affected-only runs, and automatic e2e test splitting. [Learn more &raquo;](https://nx.dev/ci/intro/ci-with-nx)
- **Self-healing CI -** An AI agent on your CI pipeline that detects failures, analyzes root cause, proposes a fix, and verifies it automatically. Local agents connect to CI via MCP to autonomously detect and fix failures. [Learn more &raquo;](https://nx.dev/ci/features/self-healing)
