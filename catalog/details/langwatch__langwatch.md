# langwatch/langwatch

The platform for LLM evaluations and AI agent testing

## features

The platform for LLM evaluations and AI agent testing.
We help teams test, simulate, evaluate, and monitor LLM-powered agents end-to-end — before release and in production.
Built for teams that need regression testing, simulations, and production observability without building custom tooling.

- [**End-to-end agent simulations**](https://langwatch.ai/scenario/)
  Run realistic scenarios against your **full stack** (tools, state, user simulator, judge) and pinpoint where your agents break, and why? down to each decision.

- **Eval + observability + prompts in one loop**
  [Trace](https://docs.langwatch.ai/integration/overview) → [dataset](https://docs.langwatch.ai/datasets/overview) → [evaluate](https://docs.langwatch.ai/llm-evaluation/offline-evaluation) → [optimize prompts/models](https://docs.langwatch.ai/optimization-studio/overview) → re-test. No glue code, no tool sprawl.

- [**Open standards, no lock-in**](https://docs.langwatch.ai/integration/opentelemetry/guide)
  OpenTelemetry/OTLP-native. Framework- and LLM-provider agnostic by design.

- [**AI Gateway for governance + cost control**](https://docs.langwatch.ai/ai-gateway/overview)
  OpenAI/Anthropic-compatible proxy with virtual keys, hierarchical budgets, inline guardrails, automatic fallback across providers, and Anthropic `cache_control` passthrough. ~700 ns hot-path overhead. Ships as a separate Go binary (`services/aigateway/`) + Helm sub-chart (`charts/gateway/`).

- [**Collaboration that doesn't slow shipping**](https://docs.langwatch.ai/features/annotations)
  Review runs, annotate failures, and ship fixes faster. Let domain experts label edge cases with [annotations & queues](https://docs.langwatch.ai/features/annotations), keep prompts in Git with the [GitHub integration](https://docs.langwatch.ai/prompt-management/features/essential/github-integration), and [link prompt versions to traces](https://docs.langwatch.ai/prompt-management/features/advanced/link-to-traces).

LangWatch gives you full visibility into agent behavior and the tools to systematically improve reliability, performance, and cost, while keeping you in control of your AI system

## installation

The fastest way to run LangWatch locally — only Node.js required:

```bash
npx @langwatch/server
```

The CLI installs `uv`, `postgres`, `redis`, `clickhouse`, the AI gateway binary, and the Langy assistant's runtime into `~/.langwatch/`, scaffolds a `.env` with locally-generated secrets, then starts every service in parallel and opens `http://localhost:5560`. Everything lives under `~/.langwatch/`; `rm -rf ~/.langwatch` is a clean reset.

Three pieces are yours to decide on, in `~/.langwatch/.env`:

| Variable | Default | What it changes |
|---|---|---|
| `LANGWATCH_ENABLE_LANGY` | `true` | The Langy assistant. Adds ~45MB for its runtime; the workers run unsandboxed as you, on your own machine. |
| `LANGWATCH_ENABLE_PRESIDIO` | `false` | The PII detection evaluator. Adds ~670MB of language model, larger than the rest of the evaluator environment put together. LangWatch's own secret and PII redaction of your traces does not depend on it. |
| `LANGWATCH_ENABLE_LINGUA` | `false` | The language detection evaluator. Adds ~95MB of language models. |

Every other evaluator is installed either way. Change any of these in `~/.langwatch/.env` and restart the server.

Prefer Docker? You can still use docker compose:

```bash
git clone https://github.com/langwatch/langwatch.git
cd platform/app
cp platform/app/.env.example platform/app/.env
docker compose up -d --wait --build
```
Once running, LangWatch will be available at `http://localhost:5560`, where you can create your first project and API key.

## configuration

Run LangWatch on your own infrastructure:

- [Docker Compose](https://docs.langwatch.ai/self-hosting/deployment/docker-compose) - Run LangWatch on your own machine.
- [Kubernetes (Helm)](https://docs.langwatch.ai/self-hosting/deployment/kubernetes-helm) - Run LangWatch on a Kubernetes cluster using Helm.
- [OnPrem](https://docs.langwatch.ai/self-hosting/onprem) - Cloud-specific setups for AWS, Google Cloud, and Azure.

<details>
<summary>Hybrid (OnPrem data) 🔀</summary>

For companies that have strict data residency and control requirements, without needing to go fully on-prem.

Read more about it on our [docs](https://docs.langwatch.ai/hybrid-setup/overview).

</details>

<details>
<summary>Local Development 👩‍💻</summary>

You can also run LangWatch locally without docker to develop and help contribute to the project.

Start just the databases using docker and leave it running:

```bash
docker compose up redis postgres opensearch
```

Then, on another terminal, install the dependencies and start LangWatch:

```bash
make install
make start
```

</details>
