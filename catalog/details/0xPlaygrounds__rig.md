# 0xPlaygrounds/rig

⚙️🦀 Build modular and scalable LLM Applications in Rust

## features

- Agentic workflows that can handle multi-turn streaming and prompting
- A classic agent runtime enabled by default
- Full [GenAI Semantic Convention](https://opentelemetry.io/docs/specs/semconv/gen-ai/) compatibility
- 20+ model providers, all under one singular unified interface
- 10+ vector store integrations, all under one singular unified interface
- Full support for LLM completion and embedding workflows
- Support for transcription, audio generation and image generation model capabilities
- Integrate LLMs in your app with minimal boilerplate
- Browser-WASM (`wasm32-unknown-unknown`) support for the portable core and
  classic runtime — see [target support](crates/rig-agent/README.md#target-support)
  for the full matrix (WASI is not supported; `rig-rmcp`/MCP is native-only)

## Runtime choices

Rig separates portable provider/backend contracts from agent orchestration:

- `rig-core` contains provider-neutral messages, completion models, portable tools,
  memory and vector-store contracts, and built-in provider mappings.
- `rig-agent` contains the classic builder, prompt/streaming traits, typed hooks,
  contextual tools, extraction, and the serializable `AgentRun` state machine. It
  remains enabled by default.

The root `rig` facade re-exports both at their familiar paths, so most code
depends only on `rig`.

## Who is using Rig?
Below is a non-exhaustive list of companies and people who are using Rig:
- [St Jude](https://www.stjude.org/) - Using Rig for a chatbot utility as part of [`proteinpaint`](https://github.com/stjude/proteinpaint), a genomics visualisation tool.
- [Coral Protocol](https://www.coralprotocol.org/) - Using Rig extensively, both internally as well as part of the [Coral Rust SDK.](https://github.com/Coral-Protocol/coral-rs)
- [VT Code](https://github.com/vinhnx/vtcode) - VT Code is a Rust-based terminal coding agent with semantic code intelligence via Tree-sitter and ast-grep. VT Code uses `rig` for simplifying LLM calls and implementing the model picker.
- [Con](https://github.com/nowledge-co/con) - Con is a GPU-accelerated terminal emulator with a built-in AI agent harness. It uses Rig as the provider abstraction layer for its integrated coding agents.
- [Dria](https://dria.co/) - a decentralised AI network. Currently using Rig as part of their [compute node.](https://github.com/firstbatchxyz/dkn-compute-node)
- [Nethermind](https://www.nethermind.io/) - Using Rig as part of their [Neural Interconnected Nodes Engine](https://github.com/NethermindEth/nine) framework.
- [Neon](https://neon.com) - Using Rig for their [app.build](https://github.com/neondatabase/appdotbuild-agent) V2 reboot in Rust.
- [Listen](https://github.com/piotrostr/listen) - A framework aiming to become the go-to framework for AI portfolio management agents. Powers [the Listen app.](https://app.listen-rs.com/)
- [Cairnify](https://cairnify.com/) - helps users find documents, links, and information instantly through an intelligent search bar. Rig provides the agentic foundation behind Cairnify’s AI search experience, enabling tool-calling, reasoning, and retrieval workflows.
- [Ryzome](https://ryzome.ai) - Ryzome is a visual AI workspace that lets you build interconnected canvases of thoughts, research, and AI agents to orchestrate complex knowledge work.
- [deepwiki-rs](https://github.com/sopaco/deepwiki-rs) - Turn code into clarity. Generate accurate technical docs and AI-ready context in minutes—perfectly structured for human teams and intelligent agents.
- [Cortex Memory](https://github.com/sopaco/cortex-mem) - The production-ready memory system for intelligent agents. A complete solution for memory management, from extraction and vector search to automated optimization, with a REST API, MCP, CLI, and insights dashboard out-of-the-box.
- [Ironclaw](https://github.com/nearai/ironclaw) - A secure personal AI assistant
- [ilert](https://www.ilert.com/) - Incident management & alerting platform. Uses Rig as the multi-provider abstr
