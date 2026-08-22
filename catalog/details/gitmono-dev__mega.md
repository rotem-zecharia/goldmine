# gitmono-dev/mega

Mega is an open-source implementation of Google Piper — a Git-compatible monorepo engine built for the AI Agent era.

## features

AI coding agents are becoming first-class participants in software engineering. But today's version control systems were designed for human developers working in isolated branches — they lack the unified context, structured metadata, and programmatic interfaces that agents need to operate reliably at scale.

Monorepos solve the context problem. When an agent can see the entire codebase — dependencies, downstream consumers, build targets, and test coverage — it makes better decisions, produces fewer hallucinations, and delivers atomic cross-project changes in a single commit.

**Mega brings Google-scale monorepo infrastructure to the open-source world, purpose-built for the agentic future.**

## limitations

Mega is evolving toward deeper AI-native capabilities:

- **IntentSpec** — A structured, machine-readable intent contract that drives agent task execution with security policies and provenance binding.
- **Multi-Agent DAG Orchestration** — Pipeline architecture for coordinating multiple AI agents across complex, multi-step code generation workflows.
- **Code Attribution** — Line-level tracking of AI-generated vs. human-written code, enabling auditability and trust in agent contributions.

## installation

To facilitate a rapid deployment and hands-on experience with the Mega service, the following instructions are derived from the project's [documentation](https://github.com/web3infra-foundation/mega/tree/main/docker).

- **Docker demo (recommended):** [docker/README.md](docker/README.md)
- **Native development:** [docs/development.md](docs/development.md)
- **Architecture:** [docs/architecture.md](docs/architecture.md)

Related projects: [Libra](https://github.com/web3infra-foundation/libra) (Git-compatible agent client), [ScorpioFS](https://github.com/web3infra-foundation/scorpiofs) (FUSE monorepo mount).

## requirements

This project builds with Buck2. Please install both Buck2 and cargo-buckal before development:

```bash
