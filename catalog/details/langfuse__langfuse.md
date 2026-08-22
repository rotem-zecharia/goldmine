# langfuse/langfuse

🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23

## features

<img width="2400" alt="features" src="https://github.com/user-attachments/assets/0fad3dee-f3ad-423c-9f0d-7ccd0f26cc2d" />

- [LLM Application Observability](https://langfuse.com/docs/tracing): Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions. Try the interactive [demo](https://langfuse.com/docs/demo) to see this in action.

- [Prompt Management](https://langfuse.com/docs/prompt-management/get-started) helps you centrally manage, version control, and collaboratively iterate on your prompts. Thanks to strong caching on server and client side, you can iterate on prompts without adding latency to your application.

- [Evaluations](https://langfuse.com/docs/evaluation/overview) are key to the LLM application development workflow, and Langfuse adapts to your needs. It supports LLM-as-a-judge, Code evaluators, user feedback collection, manual labeling, and custom evaluation pipelines via APIs/SDKs.

- [Datasets](https://langfuse.com/docs/evaluation/dataset-runs/datasets) enable test sets and benchmarks for evaluating your LLM application. They support continuous improvement, pre-deployment testing, structured experiments, flexible evaluation, and seamless integration with frameworks like LangChain and LlamaIndex.

- [LLM Playground](https://langfuse.com/docs/playground) is a tool for testing and iterating on your prompts and model configurations, shortening the feedback loop and accelerating development. When you see a bad result in tracing, you can directly jump to the playground to iterate on it.

- [Comprehensive API](https://langfuse.com/docs/api): Langfuse is frequently used to power bespoke LLMOps workflows while using the building blocks provided by Langfuse via the API. OpenAPI spec, Postman collection, and typed SDKs for Python, JS/TS are available.

## 📦 Deploy Langfuse

<img width="2400" alt="deploy" src="https://github.com/user-attachments/assets/cf72e7f8-db7f-4e11-a2a1-ecfbe46f262c" />

### Langfuse Cloud

Managed deployment by the Langfuse team, generous free-tier, no credit card required.

<div align="center">
    <a href="https://cloud.langfuse.com" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/»%20Sign%20up%20for%20Langfuse%20Cloud-8A2BE2?&color=black">
    </a>
</div>

### Self-Host Langfuse

Run Langfuse on your own infrastructure:

- [Local (docker compose)](https://langfuse.com/self-hosting/local): Run Langfuse on your own machine in 5 minutes using Docker Compose.

  ```bash
  # Get a copy of the latest Langfuse repository
  git clone --depth=1 https://github.com/langfuse/langfuse.git
  cd langfuse

  # Run the langfuse docker compose
  docker compose up
  ```

- [VM](https://langfuse.com/self-hosting/docker-compose): Run Langfuse on a single Virtual Machine using Docker Compose.
- [Kubernetes (Helm)](https://langfuse.com/self-hosting/kubernetes-helm): Run Langfuse on a Kubernetes cluster using Helm. This is the preferred production deployment.
- Terraform Templates: [AWS](https://langfuse.com/self-hosting/aws), [Azure](https://langfuse.com/self-hosting/azure), [GCP](https://langfuse.com/self-hosting/gcp)

See [self-hosting documentation](https://langfuse.com/self-hosting) to learn more about architecture and configuration options.

> [!TIP]
> **Self-hosting Langfuse?** Subscribe to the [self-hosting update list](https://langfuse.com/self-hosting#subscribe) to get an email about important features and new releases for open source Langfuse — self-hosting updates only, no marketing.

## 🔌 Integrations

<img width="2400" alt="integrations" src="https://github.com/user-attachments/assets/b85c9a45-68f0-4f76-b545-0e8632abef9f" />

### Main Integrations:

| Integration                                                                  | Supports                   | Description                                        

## installation

Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions.

### 1️⃣ Create new project

1.  [Create Langfuse account](https://cloud.langfuse.com/auth/sign-up) or [self-host](https://langfuse.com/self-hosting)
2.  Create a new project
3.  Create new API credentials in the project settings

### 2️⃣ Log your first LLM call

The [`@observe()` decorator](https://langfuse.com/docs/sdk/python/decorators) makes it easy to trace any Python LLM application. In this quickstart we also use the Langfuse [OpenAI integration](https://langfuse.com/integrations/model-providers/openai-py) to automatically capture all model parameters.

> [!TIP]
> Not using OpenAI? Visit [our documentation](https://langfuse.com/docs/get-started#log-your-first-llm-call-to-langfuse) to learn how to log other models and frameworks.

```bash
pip install langfuse openai
```

```bash filename=".env"
LANGFUSE_SECRET_KEY="sk-lf-..."
LANGFUSE_PUBLIC_KEY="pk-lf-..."
LANGFUSE_BASE_URL="https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL="https://us.cloud.langfuse.com" # 🇺🇸 US region
```

```python /@observe()/ /from langfuse.openai import openai/ filename="main.py"
from langfuse import observe
from langfuse.openai import openai # OpenAI integration

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "What is Langfuse?"}],
    ).choices[0].message.content

@observe()
def main():
    return story()

main()
```

### 3️⃣ See traces in Langfuse

See your language model calls and other application logic in Langfuse.

<img width="1600" alt="example-trace-for-github" src="https://github.com/user-attachments/assets/8f6995b7-285f-441a-b52f-1331d13ceb45" />

_[Public example trace in Langfuse](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/db22d0a442216b485abd83cc9df6d9ee)_

## 💭 Support

Finding an answer to your question:

- Our [documentation](https://langfuse.com/docs) is the best place to start looking for answers. It is comprehensive, and we invest significant time into maintaining it. You can also suggest edits to the docs via GitHub.
- [Langfuse FAQs](https://langfuse.com/faq) where the most common questions are answered.
- Use "[Ask AI](https://langfuse.com/docs/ask-ai)" to get instant answers to your questions.

Support Channels:

- **Ask any question in our [public Q&A](https://github.com/orgs/langfuse/discussions/categories/support) on GitHub Discussions.** Please include as much detail as possible (e.g. code snippets, screenshots, background information) to help us understand your question.
- [Request a feature](https://github.com/orgs/langfuse/discussions/categories/ideas) on GitHub Discussions.
- [Report a Bug](https://github.com/langfuse/langfuse/issues) on GitHub Issues.
- For time-sensitive queries, ping us via the in-app chat widget.

## 🤝 Contributing

Your contributions are welcome!

- Vote on [Ideas](https://github.com/orgs/langfuse/discussions/categories/ideas) in GitHub Discussions.
- Raise and comment on [Issues](https://github.com/langfuse/langfuse/issues).
- Open a PR - see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to setup a development environment.

## 🥇 License

This repository is MIT licensed, except for the `ee` folders. See [LICENSE](LICENSE) and [docs](https://langfuse.com/docs/open-source) for more details.

## requirements

We deploy this code base in Docker containers based on the Linux Alpine Image ([source](https://github.com/nodejs/docker-node)). You may find the Dockerfiles in [web/Dockerfile](web/Dockerfile) and [worker/Dockerfile](worker/Dockerfile).

## ⭐️ Star History

<a href="https://star-history.com/#langfuse/langfuse&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=langfuse/langfuse&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=langfuse/langfuse&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=langfuse/langfuse&type=Date" style="border-radius: 15px;" />
 </picture>
</a>

## ❤️ Open Source Projects Using Langfuse

Top open-source Python projects that use Langfuse, ranked by stars ([Source](https://github.com/langfuse/langfuse-docs/blob/main/components-mdx/dependents)):

| Repository                                                                                                                                                                                                                                                                                                     |  Stars |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -----: |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/85702467?s=40&v=4" width="20" height="20" alt=""> &nbsp; [langflow-ai](https://github.com/langflow-ai) / [langflow](https://github.com/langflow-ai/langflow)                                                                             | 116251 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/158137808?s=40&v=4" width="20" height="20" alt=""> &nbsp; [open-webui](https://github.com/open-webui) / [open-webui](https://github.com/open-webui/open-webui)                                                                           | 109642 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/23818?s=40&v=4" width="20" height="20" alt=""> &nbsp; [abi](https://github.com/abi) / [screenshot-to-code](https://github.com/abi/screenshot-to-code)                                                                                    |  70877 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/131470832?s=40&v=4" width="20" height="20" alt=""> &nbsp; [lobehub](https://github.com/lobehub) / [lobe-chat](https://github.com/lobehub/lobe-chat)                                                                                      |  65454 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/69962740?s=40&v=4" width="20" height="20" alt=""> &nbsp; [infiniflow](https://github.com/infiniflow) / [ragflow](https://github.com/infiniflow/ragflow)                                                                                  |  64118 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/135057108?s=40&v=4" width="20" height="20" alt=""> &nbsp; [firecrawl](https://github.com/firecrawl) / [firecrawl](https://github.com/firecrawl/firecrawl)                                                                                |  56713 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/130722866?s=40&v=4" width="20" height="20" alt=""> &nbsp; [run-llama](https://github.com/run-llama) / [llama_index](https://github.com/run-llama/llama_index)                                                                            |  44203 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/128289781?s=40&v=4" width="20" height="20" alt=""> &nbsp; [FlowiseAI](https://github.com/FlowiseAI) / [Flowise](https://github.com
