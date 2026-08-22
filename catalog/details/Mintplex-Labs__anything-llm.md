# Mintplex-Labs/anything-llm

Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience

## features

AnythingLLM is the all-in-one AI application that lets you build a private, fully-featured ChatGPT—without compromises. Connect your favorite local or cloud LLM, ingest your documents, and start chatting in minutes. Out of the box you get built-in agents, multi-user support, vector databases, and document pipelines — no extra configuration required.

AnythingLLM supports multiple users as well where you can control the access and experience per user without compromising the security or privacy of the instance or your intellectual property.

## Cool Features of AnythingLLM

- [Dynamic Model Routing](https://docs.anythingllm.com/model-router/overview) - Automatically route chats to the best provider & model for the conversation based on rules you define.
- [Automatic & User Managed Memories](https://docs.anythingllm.com/features/memories) - Have your LLM remember important information about you or your workspace.
- [Scheduled Tasks](https://docs.anythingllm.com/scheduled-jobs/overview) - Run recurring tasks or prompts on a cron schedule with full agent capabilities.
- [Intelligent Skill Selection](https://docs.anythingllm.com/agent/intelligent-tool-selection) Enable **unlimited** tools for your models while reducing token usage by up to 80% per query
- [No-code AI Agent builder](https://docs.anythingllm.com/agent-flows/overview)
- [MCP-compatibility](https://docs.anythingllm.com/mcp-compatibility/overview)
- [Multi-modal support (both closed and open-source LLMs!)](https://docs.anythingllm.com/features/multimodal)
- [Custom AI Agents](https://docs.anythingllm.com/agent/custom/introduction)
- 👤 Multi-user instance support and permissioning _Docker version only_
- 🦾 Agents inside your workspace (browse the web, etc)
- 💬 [Custom Embeddable Chat widget for your website](https://github.com/Mintplex-Labs/anythingllm-embed/blob/main/README.md) _Docker version only_
- 📖 Multiple document type support (PDF, TXT, DOCX, etc)
- Intuitive chat UI with drag-and-drop uploads and source citations.
- Production-ready for any cloud deployment.
- Works with all popular [closed and open-source LLM providers](#supported-llms-embedder-models-speech-models-and-vector-databases).
- Built-in optimizations for large document sets—lower costs and faster responses than other chat UIs.
- Full Developer API for custom integrations!
- ...and much more—install in minutes and see for yourself.

### Supported LLMs, Embedder Models, Speech models, and Vector Databases

**Large Language Models (LLMs):**

- [Any open-source llama.cpp compatible model](/server/storage/models/README.md#text-generation-llm-selection)
- [OpenAI](https://openai.com)
- [OpenAI (Generic)](https://openai.com)
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [Anthropic](https://www.anthropic.com/)
- [NVIDIA NIM (chat models)](https://build.nvidia.com/explore/discover)
- [Google Gemini Pro](https://ai.google.dev/)
- [Ollama (chat models)](https://ollama.ai/)
- [LM Studio (all models)](https://lmstudio.ai)
- [LocalAI (all models)](https://localai.io/)
- [Together AI (chat models)](https://www.together.ai/)
- [Fireworks AI (chat models)](https://fireworks.ai/)
- [Perplexity (chat models)](https://www.perplexity.ai/)
- [OpenRouter (chat models)](https://openrouter.ai/)
- [DeepSeek (chat models)](https://deepseek.com/)
- [Mistral](https://mistral.ai/)
- [Groq](https://groq.com/)
- [Cohere](https://cohere.com/)
- [KoboldCPP](https://github.com/LostRuins/koboldcpp)
- [LiteLLM](https://github.com/BerriAI/litellm)
- [Text Generation Web UI](https://github.com/oobabooga/text-generation-webui)
- [Apipie](https://apipie.ai/)
- [xAI](https://x.ai/)
- [Z.AI (chat models)](https://z.ai/model-api)
- [Novita AI (chat models)](https://novita.ai/model-api/product/llm-api?utm_source=github_anything-llm&utm_medium=github_readme&utm_campaign=link)
- [PPIO](https://ppinfra.com?utm_source=github_anything-llm)
- [Gitee AI](htt

## installation

- `yarn setup` To fill in the required `.env` files you'll need in each of the application sections (from root of repo).
  - Go fill those out before proceeding. Ensure `server/.env.development` is filled or else things won't work right.
- `yarn dev:server` To boot the server locally (from root of repo).
- `yarn dev:frontend` To boot the frontend locally (from root of repo).
- `yarn dev:collector` To then run the document collector (from root of repo).

[Learn about documents](./server/storage/documents/DOCUMENTS.md)

## Telemetry & Privacy

AnythingLLM by Mintplex Labs Inc contains a telemetry feature that collects anonymous usage information.

<details>
<summary><kbd>More about Telemetry & Privacy for AnythingLLM</kbd></summary>

### Why?

We use this information to help us understand how AnythingLLM is used, to help us prioritize work on new features and bug fixes, and to help us improve AnythingLLM's performance and stability.

### Opting out

Set `DISABLE_TELEMETRY` in your server or docker .env settings to "true" to opt out of telemetry. You can also do this in-app by going to the sidebar > `Privacy` and disabling telemetry.

### What do you explicitly track?

We will only track usage details that help us make product and roadmap decisions, specifically:

- Type of your installation (Docker or Desktop)

- When a document is added or removed. No information _about_ the document. Just that the event occurred. This gives us an idea of use.

- Type of vector database in use. This helps us prioritize changes when updates arrive for that provider.

- Type of LLM provider & model tag in use. This helps us prioritize changes when updates arrive for that provider or model, or combination thereof. eg: reasoning vs regular, multi-modal models, etc.

- When a chat is sent. This is the most regular "event" and gives us an idea of the daily-activity of this project across all installations. Again, only the **event** is sent - we have no information on the nature or content of the chat itself.

You can verify these claims by finding all locations `Telemetry.sendTelemetry` is called. Additionally these events are written to the output log so you can also see the specific data which was sent - if enabled. **No IP or other identifying information is collected**. The Telemetry provider is [PostHog](https://posthog.com/) - an open-source telemetry collection service.

We take privacy very seriously, and we hope you understand that we want to learn how our tool is used, without using annoying popup surveys, so we can build something worth using. The anonymous data is _never_ shared with third parties, ever.

[View all telemetry events in source code](https://github.com/search?q=repo%3AMintplex-Labs%2Fanything-llm%20.sendTelemetry(&type=code)

### Other outbound connections

If you disable telemetry, you would still see outbound connections to the following services:

- If using an external tool, LLM, Embedding models, or Vector databases, you will still see outbound connections to the respective service provider.
- `cdn.anythingllm.com` for pulling models from our mirror CDN. This is not tracked by telemetry and is actually useful for those in VPN restricted regions.
- `github/githubusercontent.com` There are some various flat files that are downloaded from these domains for context window caching.

Basically, if telemetry is disabled we don't collect anything. However, depending on your setup you may still see outbound connections and would be subject to the terms of service of the respective service provider.

</details>

## 👋 Contributing

- [Contributing to AnythingLLM](./CONTRIBUTING.md) - How to contribute to AnythingLLM.

## 💖 Sponsors

<!--
### Premium Sponsors
premium-sponsors (reserved for $100/mth sponsors who request to be called out here and/or are non-private sponsors) -->
<!-- premium-sponsors -->

### All Sponsors

<!-- all-sponsors --><a href="https://github.com/jaschadub"><img src="https:&#x2F;&#x2F;github.com&#x2F;jaschadu
