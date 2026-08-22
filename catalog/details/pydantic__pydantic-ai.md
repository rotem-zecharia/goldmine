# pydantic/pydantic-ai

How Python does AI: agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.

## features

- **Any model, one Python API.** [Virtually every model and provider](https://ai.pydantic.dev/models/overview) (OpenAI, Anthropic, Google, Bedrock, Azure AI Foundry, Groq, Mistral, xAI, Ollama, and dozens more), swappable with a string, or through the [Pydantic AI Gateway](https://ai.pydantic.dev/gateway): one key for all of them, with failover and cost monitoring built in. No flagship feature is locked to one vendor.

- **Typed end to end.** [Structured outputs](https://ai.pydantic.dev/output), typed [dependency injection](https://ai.pydantic.dev/dependencies), [typed tools](https://ai.pydantic.dev/tools): your IDE, type checker, and coding agent all know what your agent returns, moving whole classes of errors from runtime to write-time. When plain control flow isn't enough, [Pydantic Graph](https://ai.pydantic.dev/graph) brings the same typing to graph-based workflows.

- **Measured, not vibes.** OpenTelemetry-native [instrumentation](https://ai.pydantic.dev/logfire) works with any OTel backend; one line lights up [Pydantic Logfire](https://pydantic.dev/logfire/llm-observability?utm_source=github&utm_medium=readme&utm_campaign=pydantic-ai) for real-time debugging, tracing, and cost tracking backed by [genai-prices](https://github.com/pydantic/genai-prices). [Pydantic Evals](https://ai.pydantic.dev/evals) tests agent behavior the way pytest tests code.

- **Batteries, composably.** One primitive, the [capability](https://ai.pydantic.dev/capabilities/overview/), bundles [tools](https://ai.pydantic.dev/tools), [instructions](https://ai.pydantic.dev/agents/#instructions), [hooks](https://ai.pydantic.dev/hooks), and [model settings](https://ai.pydantic.dev/agents/#model-run-settings) into reusable units. Core ships fundamentals like [MCP](https://ai.pydantic.dev/capabilities/mcp/) and [web search](https://ai.pydantic.dev/capabilities/web-search/), the [Harness](https://github.com/pydantic/pydantic-ai-harness) ships everything else, and complete agents like [Coder](https://pydantic.dev/docs/ai/harness/coder/) and [Researcher](https://pydantic.dev/docs/ai/harness/researcher/) are just capabilities composed: they come apart the way they went together. Or skip code entirely with [YAML/JSON agent specs](https://ai.pydantic.dev/agent-spec).

- **[Every interface](https://ai.pydantic.dev/interfaces).** One agent definition runs as a [CLI](https://ai.pydantic.dev/cli), a [built-in web chat](https://ai.pydantic.dev/web), or [realtime speech](https://ai.pydantic.dev/realtime) (OpenAI Realtime, Gemini Live, Azure, xAI Grok Voice); [UI event streams](https://ai.pydantic.dev/ui/overview) (AG-UI, Vercel AI) connect it to your own frontend or anything else; and [ACP](https://pydantic.dev/docs/ai/harness/acp/) *(experimental)* serves it as an editor agent.

- **Durable execution.** First-party, co-maintained [durable execution](https://ai.pydantic.dev/durable_execution/overview/) on Temporal, DBOS, or Prefect, with [Restate, Kitaru, and Airflow](https://ai.pydantic.dev/durable_execution/overview/) integrations and more coming. Agents survive restarts and run for days on the engine you already operate, with [human-in-the-loop approval](https://ai.pydantic.dev/deferred-tools#human-in-the-loop-tool-approval) built in.

Built by the [Pydantic](https://docs.pydantic.dev) team: [Pydantic Validation](https://pydantic.dev/docs/) is the validation layer of the OpenAI SDK, the Anthropic SDK, the Google ADK, LangChain, and most of the AI ecosystem (and the foundation FastAPI was built on). Pydantic AI brings that same feeling to agents.
