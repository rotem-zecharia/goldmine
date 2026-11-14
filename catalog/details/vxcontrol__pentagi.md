# vxcontrol/pentagi

Fully autonomous AI Agents system capable of performing complex penetration testing tasks

## features

PentAGI is an open-source, self-hosted multi-agent system for autonomous penetration testing. You describe a target and a goal in plain language; a team of specialized AI agents plans the work, runs 20+ professional tools such as nmap, Metasploit and sqlmap inside an isolated Docker sandbox, remembers what it learned and hands you a report.

- **Who it is for.** Security engineers, penetration testers, researchers and red teams who want an autonomous assistant on their own infrastructure, for authorized testing only.
- **What sets it apart.** It runs on your own servers with the model of your choice: 10+ cloud LLM providers, your own OpenAI-compatible gateway, or local models through Ollama or vLLM. Results and successful approaches are kept in PostgreSQL with pgvector for later flows, an optional Neo4j knowledge graph tracks hosts, services and findings, execution monitoring and task planning help smaller open models, and REST and GraphQL APIs automate it. PentAGI Enterprise adds agent profiles, plugins and MCP servers, customer-ready reports and a real-time attack-chain view.
- **How to install.** An interactive installer for Linux, macOS and Windows sets PentAGI up with Docker Compose — see [Quick Start](#quick-start).

PentAGI is developed by [VXControl](https://vxcontrol.com), a security engineering company based in Dubai.

You can watch the video **PentAGI overview**:
[![PentAGI Overview Video](https://github.com/user-attachments/assets/0828dc3e-15f1-4a1d-858e-9696a146e478)](https://youtu.be/R70x5Ddzs1o)

## Features

- Secure & Isolated. All operations are performed in a sandboxed Docker environment with complete isolation.
- Fully Autonomous. AI-powered agent that automatically determines and executes penetration testing steps with optional execution monitoring and intelligent task planning for enhanced reliability.
- Professional Pentesting Tools. Built-in suite of 20+ professional security tools including nmap, metasploit, sqlmap, and more.
- Smart Memory System. Long-term storage of research results and successful approaches for future use.
- Optional Knowledge Graph Integration. Graphiti-powered knowledge graph using Neo4j for semantic relationship tracking and advanced context understanding.
- Web Intelligence. Built-in browser via [scraper](https://hub.docker.com/r/vxcontrol/scraper) for gathering latest information from web sources.
- External Search Systems. Integration with advanced search APIs including [Tavily](https://tavily.com), [Firecrawl](https://www.firecrawl.dev), [Traversaal](https://traversaal.ai), [Perplexity](https://www.perplexity.ai), [DuckDuckGo](https://duckduckgo.com/), [Google Custom Search](https://programmablesearchengine.google.com/), [Sploitus Search](https://sploitus.com) and [SearXNG](https://searxng.org) for comprehensive information gathering.
- Team of Specialists. Delegation system with specialized AI agents for research, development, and infrastructure tasks, enhanced with optional execution monitoring and intelligent task planning for optimal performance with smaller models.
- Comprehensive Monitoring. Detailed logging and integration with Grafana/Prometheus for real-time system observation.
- Detailed Reporting. Generation of thorough vulnerability reports with exploitation guides.
- Smart Container Management. Automatic Docker image selection based on specific task requirements.
- Modern Interface. Clean and intuitive web UI for system management and monitoring.
- Comprehensive APIs. Full-featured REST and GraphQL APIs with Bearer token authentication for automation and integration.
- Persistent Storage. All commands and outputs are stored in PostgreSQL with [pgvector](https://hub.docker.com/r/vxcontrol/pgvector) extension.
- Scalable Architecture. Microservices-based design supporting horizontal scaling.
- Self-Hosted Solution. Complete control over your deployment and data.
- Flexible Authentication. Support for 10+ LLM providers ([OpenAI](https://platform.openai.com/), [Anth

## configuration

| Parameter             | Environment Variable             | Default | Description                                                |
| --------------------- | -------------------------------- | ------- | ---------------------------------------------------------- |
| Preserve Last         | `SUMMARIZER_PRESERVE_LAST`       | `true`  | Whether to keep all messages in the last section intact    |
| Use QA Pairs          | `SUMMARIZER_USE_QA`              | `true`  | Whether to use QA pair summarization strategy              |
| Summarize Human in QA | `SUMMARIZER_SUM_MSG_HUMAN_IN_QA` | `false` | Whether to summarize human messages in QA pairs            |
| Last Section Size     | `SUMMARIZER_LAST_SEC_BYTES`      | `51200` | Maximum byte size for last section (50KB)                  |
| Max Body Pair Size    | `SUMMARIZER_MAX_BP_BYTES`        | `16384` | Maximum byte size for a single body pair (16KB)            |
| Max QA Sections       | `SUMMARIZER_MAX_QA_SECTIONS`     | `10`    | Maximum QA pair sections to preserve                       |
| Max QA Size           | `SUMMARIZER_MAX_QA_BYTES`        | `65536` | Maximum byte size for QA pair sections (64KB)              |
| Keep QA Sections      | `SUMMARIZER_KEEP_QA_SECTIONS`    | `1`     | Number of recent QA sections to keep without summarization |

### Assistant Summarizer Configuration Options

Assistant instances can use customized summarization settings to fine-tune context management behavior:

| Parameter          | Environment Variable                    | Default | Description                                                          |
| ------------------ | --------------------------------------- | ------- | -------------------------------------------------------------------- |
| Preserve Last      | `ASSISTANT_SUMMARIZER_PRESERVE_LAST`    | `true`  | Whether to preserve all messages in the assistant's last section     |
| Last Section Size  | `ASSISTANT_SUMMARIZER_LAST_SEC_BYTES`   | `76800` | Maximum byte size for assistant's last section (75KB)                |
| Max Body Pair Size | `ASSISTANT_SUMMARIZER_MAX_BP_BYTES`     | `16384` | Maximum byte size for a single body pair in assistant context (16KB) |
| Max QA Sections    | `ASSISTANT_SUMMARIZER_MAX_QA_SECTIONS`  | `7`     | Maximum QA sections to preserve in assistant context                 |
| Max QA Size        | `ASSISTANT_SUMMARIZER_MAX_QA_BYTES`     | `76800` | Maximum byte size for assistant's QA sections (75KB)                 |
| Keep QA Sections   | `ASSISTANT_SUMMARIZER_KEEP_QA_SECTIONS` | `3`     | Number of recent QA sections to preserve without summarization       |

The assistant summarizer configuration provides more memory for context retention compared to the global settings, preserving more recent conversation history while still ensuring efficient token usage.

### Summarizer Environment Configuration

```bash
# Default values for global summarizer logic
SUMMARIZER_PRESERVE_LAST=true
SUMMARIZER_USE_QA=true
SUMMARIZER_SUM_MSG_HUMAN_IN_QA=false
SUMMARIZER_LAST_SEC_BYTES=51200
SUMMARIZER_MAX_BP_BYTES=16384
SUMMARIZER_MAX_QA_SECTIONS=10
SUMMARIZER_MAX_QA_BYTES=65536
SUMMARIZER_KEEP_QA_SECTIONS=1

# Default values for assistant summarizer logic
ASSISTANT_SUMMARIZER_PRESERVE_LAST=true
ASSISTANT_SUMMARIZER_LAST_SEC_BYTES=76800
ASSISTANT_SUMMARIZER_MAX_BP_BYTES=16384
ASSISTANT_SUMMARIZER_MAX_QA_SECTIONS=7
ASSISTANT_SUMMARIZER_MAX_QA_BYTES=76800
ASSISTANT_SUMMARIZER_KEEP_QA_SECTIONS=3
```

</details>

<a id="advanced-agent-supervision"></a>
<details>
<summary><b>Advanced Agent Supervision</b> (click to expand)</summary>

PentAGI includes sophisticated multi-layered agent supervision mechanisms to ensure efficient task execution, prevent infinite loops, and provide intelligent recovery from stuck states:

### Execution Monitoring (Beta)
- **Automatic Mentor Intervention**: Adviser agent (mentor) is automatically invoked when execution patterns indicate potential issues
- **Pattern Detection**: Monitors

## installation

For a step-by-step walkthrough that connects installation, configuration, LLM and embedding provider testing, and your first login, see the [Installing and Configuring PentAGI](examples/guides/installation_configuration.md) guide. The sections below remain the detailed reference for each step.

## requirements

- Docker and Docker Compose (or Podman - see [Podman configuration](#running-pentagi-with-podman))
- Minimum 2 vCPU
- Minimum 4GB RAM
- 20GB free disk space
- Internet access for downloading images and updates

## tools

# Optional: Chinese AI providers
# DEEPSEEK_API_KEY=your_deepseek_key             # DeepSeek (strong reasoning)
# GLM_API_KEY=your_glm_key                       # GLM (Zhipu AI)
# KIMI_API_KEY=your_kimi_key                     # Kimi (Moonshot AI, ultra-long context)
# QWEN_API_KEY=your_qwen_key                     # Qwen (Alibaba Cloud, multimodal)
# MINIMAX_API_KEY=your_minimax_key               # MiniMax

# Optional: European and US providers
# MISTRAL_API_KEY=your_mistral_key               # Mistral
# XAI_API_KEY=your_xai_key                       # xAI (Grok)

# Optional: Local LLM provider (zero-cost inference)
OLLAMA_SERVER_URL=http://localhost:11434
OLLAMA_SERVER_MODEL=your_model_name

## limitations

Each provider has specific limitations and supported features:

- **OpenAI**: Supports all configuration options
- **Ollama**: Does not support `EMBEDDING_KEY` as it uses local models
- **Mistral**: Supports all configuration options
- **Jina**: Supports all configuration options
- **HuggingFace**: Requires `EMBEDDING_KEY` and supports all other options
- **GoogleAI**: Does not support `EMBEDDING_URL`, requires `EMBEDDING_KEY`
- **VoyageAI**: Supports all configuration options

If `EMBEDDING_URL` and `EMBEDDING_KEY` are both left empty, the system uses the corresponding LLM provider's server and key together (e.g., `OPEN_AI_SERVER_URL` and `OPEN_AI_KEY` when `EMBEDDING_PROVIDER=openai`). A key set in `EMBEDDING_KEY` without `EMBEDDING_URL` goes to the provider's public endpoint, and an `EMBEDDING_URL` set without a key receives the LLM provider's key only when it is that provider's own server. So an OpenAI-compatible endpoint of another vendor needs its key in `EMBEDDING_KEY`, and a keyless local server (LocalAI, vLLM, TEI) takes any non-empty value there. Whenever the Mistral embedder uses `MISTRAL_SERVER_URL`, it also names the model the way that server expects: `MISTRAL_PROVIDER=mistral` turns `mistral-embed` into `mistral/mistral-embed`, and a model that already starts with `mistral/` is sent as is.
