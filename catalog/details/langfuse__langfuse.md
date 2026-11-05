# langfuse/langfuse

🪢 Open source agent evals & observability: Trace, evaluate, and improve LLM applications with one open platform.

## features

<img width="2400" alt="features" src="https://github.com/user-attachments/assets/0fad3dee-f3ad-423c-9f0d-7ccd0f26cc2d" />

- [AI Observability](https://langfuse.com/docs/observability/overview): Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions. Built on OpenTelemetry. Try the interactive [demo](https://langfuse.com/docs/demo) to see this in action.

- [Prompt Management](https://langfuse.com/docs/prompt-management/overview) helps you centrally manage, version control, and collaboratively iterate on your prompts. Thanks to strong caching on server and client side, you can iterate on prompts without adding latency to your application. The [LLM Playground](https://langfuse.com/docs/prompt-management/features/playground) lets you test prompts and model configurations; when you see a bad result in tracing, you can jump straight to the playground to iterate on it.

- [Skill Management](https://langfuse.com/docs/skill-management/overview) (beta) brings versioning and labels to agent skills: a `SKILL.md` with task instructions plus optional supporting files. Promote or roll back versions without changing application code, and link skill versions to the traces they produced.

- [Evaluations](https://langfuse.com/docs/evaluation/overview) are key to the AI agent development workflow, and Langfuse adapts to your needs. It supports LLM-as-a-judge, code evaluators, user feedback collection, manual labeling, and custom evaluation pipelines via APIs/SDKs. Use [Datasets and Experiments](https://langfuse.com/docs/evaluation/experiments/datasets) to build test sets and benchmarks for pre-deployment testing and continuous improvement.

- [AI Gateway](https://langfuse.com/docs/gateway/overview) (beta) gives your organization one endpoint for calls to your model providers. Keep provider credentials in one place, hand out per-user or service account gateway keys, approve models centrally, track AI spend per user, key, and model, and record every call as a Langfuse trace.

- [Metrics and Dashboards](https://langfuse.com/docs/metrics/overview): Track latency, cost, and quality across any dimension with [custom dashboards](https://langfuse.com/docs/metrics/features/custom-dashboards), the metrics API, and alerts.

- [Comprehensive API](https://langfuse.com/docs/api-and-data-platform/overview): Langfuse is frequently used to power bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API. An OpenAPI spec, typed SDKs for Python and JS/TS, the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli), and the [Langfuse Agent Skill](https://langfuse.com/docs/api-and-data-platform/features/agent-skill) for coding agents are available.

## 📦 Deploy Langfuse

<img width="2400" alt="deploy" src="https://github.com/user-attachments/assets/cf72e7f8-db7f-4e11-a2a1-ecfbe46f262c" />

### Langfuse Cloud

Managed deployment by the Langfuse team, generous free tier, no credit card required.

**[Sign up for Langfuse Cloud →](https://langfuse.com/cloud)**

### Self-Host Langfuse

Run Langfuse on your own infrastructure:

- [Docker Compose](https://langfuse.com/self-hosting/deployment/docker-compose): Run Langfuse on your own machine or a single virtual machine in 5 minutes. The guide also covers configuring Docker log rotation so container logs don't fill up the disk.

  ```bash
  # Get a copy of the latest Langfuse repository
  git clone --depth=1 https://github.com/langfuse/langfuse.git
  cd langfuse

  # Run the langfuse docker compose
  docker compose up
  ```

- [Kubernetes (Helm)](https://langfuse.com/self-hosting/deployment/kubernetes-helm): Run Langfuse on a Kubernetes cluster using Helm. This is the preferred production deployment.
- Terraform Templates: [AWS](https://langfuse.com/self-hosting/deployment/aws), [Azure](https://langfus

## installation

Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions.

### 🤖 Agentic installation (recommended)

Install the [Langfuse Agent Skill](https://github.com/langfuse/skills) to let your coding agent access all Langfuse features, then ask it to add tracing to your application:

```txt
Install the Langfuse Agent Skill from github.com/langfuse/skills
and use it to add tracing to this application with Langfuse
following best practices.
```

You can also install the skill with the [skills CLI](https://www.npmjs.com/package/skills) (`npx skills add langfuse/skills --skill "langfuse"`) or the [Langfuse Cursor plugin](https://cursor.com/marketplace/langfuse). If your agent supports MCP, add the [Langfuse Docs MCP server](https://langfuse.com/docs/docs-mcp) (`https://langfuse.com/api/mcp`, no authentication) so it can look up current documentation while it works. See the [get started guide](https://langfuse.com/docs/observability/get-started) for details.

### 🛠️ Manual installation

#### 1️⃣ Create new project

1.  [Create Langfuse account](https://langfuse.com/cloud) or [self-host](https://langfuse.com/self-hosting)
2.  Create a new project
3.  Create new API credentials in the project settings

#### 2️⃣ Log your first LLM call

The [`@observe()` decorator](https://langfuse.com/docs/observability/sdk/instrumentation#observe-wrapper) makes it easy to trace any Python LLM application. In this quickstart we also use the Langfuse [OpenAI integration](https://langfuse.com/integrations/model-providers/openai-py) to automatically capture all model parameters.

> [!TIP]
> Not using OpenAI? Visit [our documentation](https://langfuse.com/docs/observability/get-started) to learn how to log other models and frameworks.

```bash
pip install langfuse openai
```

```bash filename=".env"
LANGFUSE_SECRET_KEY="sk-lf-..."
LANGFUSE_PUBLIC_KEY="pk-lf-..."
LANGFUSE_BASE_URL="https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL="https://us.cloud.langfuse.com" # 🇺🇸 US region
# LANGFUSE_BASE_URL="https://jp.cloud.langfuse.com" # 🇯🇵 Japan region
# LANGFUSE_BASE_URL="https://hipaa.cloud.langfuse.com" # ⚕️ HIPAA region
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

#### 3️⃣ See traces in Langfuse

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
- [Report a Bug](https://github.com/langfuse/langfus

## requirements

We deploy this code base in Docker containers. See [web/Dockerfile](web/Dockerfile) and [worker/Dockerfile](worker/Dockerfile) for how the images are built, including the base images they use.

## ⭐️ Star History

<a href="https://star-history.com/#langfuse/langfuse&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=langfuse/langfuse&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=langfuse/langfuse&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=langfuse/langfuse&type=Date" style="border-radius: 15px;" />
 </picture>
</a>

## ❤️ Open Source Projects Using Langfuse

Top open-source projects that use the Langfuse Python or JS/TS SDK, ranked by stars ([Source](https://github.com/langfuse/langfuse-docs/blob/main/components-mdx/dependents)):

| Repository                                                                                                                                                                                                                                                                                                     |  Stars |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -----: |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/130738209?s=40&v=4" width="20" height="20" alt=""> &nbsp; [Significant-Gravitas](https://github.com/Significant-Gravitas) / [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)                                                   | 187903 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/127165244?s=40&v=4" width="20" height="20" alt=""> &nbsp; [langgenius](https://github.com/langgenius) / [dify](https://github.com/langgenius/dify)                                                                                       | 160407 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/85702467?s=40&v=4" width="20" height="20" alt=""> &nbsp; [langflow-ai](https://github.com/langflow-ai) / [langflow](https://github.com/langflow-ai/langflow)                                                                             | 156333 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/4158466?s=40&v=4" width="20" height="20" alt=""> &nbsp; [bytedance](https://github.com/bytedance) / [deer-flow](https://github.com/bytedance/deer-flow)                                                                                  |  84985 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/320819803?s=40&v=4" width="20" height="20" alt=""> &nbsp; [cheaper-inference](https://github.com/cheaper-inference) / [OmniRoute](https://github.com/cheaper-inference/OmniRoute)                                                        |  84532 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/131470832?s=40&v=4" width="20" height="20" alt=""> &nbsp; [lobehub](https://github.com/lobehub) / [lobehub](https://github.com/lobehub/lobehub)                                                                                          |  83873 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/23818?s=40&v=4" width="20" height="20" alt=""> &nbsp; [abi](https://github.com/abi) / [screenshot-to-code](https://github.com/abi/screenshot-to-code)                                                                                    |  81022 |
| <img class="avatar mr-2" src="https://avatars.githubusercontent.com/u/6154722?s=40&v=4" width="20" height="20" alt=""> &nbsp; [microsoft](https://github.com/microsoft) / [ai-agents-for-beginners](https://github.com/microsoft/ai-
