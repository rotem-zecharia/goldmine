# deepset-ai/haystack

Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, m

## installation

The simplest way to get Haystack is via pip:

```sh
pip install haystack-ai
```

Install nightly pre-releases to try the newest features:
```sh
pip install --pre haystack-ai
```

Haystack supports multiple installation methods, including Docker images. For a comprehensive guide, please refer
to the [documentation](https://docs.haystack.deepset.ai/docs/installation).

## Documentation

If you're new to the project, check out ["What is Haystack?"](https://haystack.deepset.ai/overview/intro) then go
through the ["Get Started Guide"](https://haystack.deepset.ai/overview/quick-start) and build your first LLM application
in a matter of minutes. Keep learning with the [tutorials](https://haystack.deepset.ai/tutorials). For more advanced
use cases, or just to get some inspiration, you can browse our Haystack recipes in the
[Cookbook](https://haystack.deepset.ai/cookbook).

At any given point, hit the [documentation](https://docs.haystack.deepset.ai/docs/intro) to learn more about Haystack, what it can do for you, and the technology behind.

## features

**Agents built for production**  
Extend agent behavior with lifecycle hooks (`before_llm`, `before_tool`, `on_exit`, …) for guardrails and custom logic, and track `step_count`, `token_usage`, and tool calls out of the box for monitoring and cost control. Get started fast with ready-made agents from [Agent Pack](https://github.com/deepset-ai/haystack-core-integrations/tree/main/integrations/agent_pack) (e.g., a deep research agent, or an advanced RAG agent) or give your own agents progressive skill discovery via `SkillToolset`, so skill descriptions only enter context when needed.

**Built for context engineering**  
Design flexible systems with explicit control over how information is retrieved, ranked, filtered, combined, structured, and routed before it reaches the model. Define pipelines and agent workflows where retrieval, memory, tools, and generation are transparent and traceable.

**Native Async Support**  
One `Pipeline` runs synchronously or asynchronously and streams token by token. `Agent` can run concurrent tool calls.  

**Modular and customizable**  
Use built-in components for retrieval, indexing, tool calling, memory, and evaluation, or create your own. Add loops, branches, and conditional logic to precisely control how context moves through your pipelines and agent workflows.

**Model- and vendor-agnostic**  
Integrate with OpenAI, Mistral, Anthropic, Cohere, Hugging Face, Google, Azure OpenAI, AWS Bedrock, local models, and many others. Swap models or infrastructure components without rewriting your system.

**Extensible ecosystem**  
Build and share custom components through a consistent interface that makes it easy for the community and third parties to extend Haystack and contribute to an open ecosystem.

> [!TIP]
>
> Would you like to deploy and serve Haystack pipelines as **REST APIs** or **MCP servers**? [Hayhooks](https://github.com/deepset-ai/hayhooks) provides a simple way for you to wrap pipelines and agents with custom logic and expose them through HTTP endpoints or MCP. It also supports OpenAI-compatible chat completion endpoints and works with chat UIs like [open-webui](https://openwebui.com/).

## Haystack Enterprise: Support & Platform

Get expert support from the Haystack team, build faster with enterprise-grade templates, and scale securely with deployment guides for cloud and on-prem environments with **Haystack Enterprise Starter**. Read more about it in the [announcement post](https://haystack.deepset.ai/blog/announcing-haystack-enterprise).

👉 [Get Haystack Enterprise Starter](https://www.deepset.ai/products-and-services/haystack-enterprise-starter?utm_source=github.com&utm_medium=referral&utm_campaign=haystack_enterprise)

Need a managed production setup for Haystack? The **Haystack Enterprise Platform** helps you build, test, deploy and operate Haystack pipelines with built-in observability, collaboration, governance, and access controls. It’s available as a managed cloud service or as a self-hosted solution.

👉 Learn more about [Haystack Enterprise Platform](https://www.deepset.ai/products-and-services/haystack-enterprise-platform?utm_campaign=developer-relations&utm_source=haystack&utm_medium=readme) or [try it free](https://www.deepset.ai/haystack-enterprise-platform-trial?utm_campaign=developer-relations&utm_source=haystack&utm_medium=readme)

## Telemetry

Haystack collects **anonymous** usage statistics of pipeline components. We receive an event every time these components are initialized. This way, we know which components are most relevant to our community.

Read more about telemetry in Haystack or how you can opt out in [Haystack docs](https://docs.haystack.deepset.ai/docs/telemetry).

## 🖖 Community

If you have a feature request or a bug report, feel free to open an [issue in GitHub](https://github.com/deepset-ai/haystack/issues). We regularly check these, so you can expect a quick response. If you'd like to discuss a topic or get more general advice on how to make Haystack
