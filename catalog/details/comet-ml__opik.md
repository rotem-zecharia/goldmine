# comet-ml/opik

Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards.

## installation

Install the Python SDK and configure it:

```bash
pip install opik
opik configure
```

Wrap any function with the `@track` decorator to start logging traces:

```python
from opik import track

@track
def my_function(input: str) -> str:
    return input
```

Every call to `my_function` is now logged to Opik, including nested calls, so this works for full agent and pipeline traces, not just single LLM calls. See the [Quickstart guide](https://www.comet.com/docs/opik/quickstart?from=llm&utm_source=opik&utm_medium=github&utm_content=quickstart_hero_link&utm_campaign=opik) for the TypeScript SDK and other setup options.

<br>

<a id="-how-opik-compares"></a>
## 📊 How Does Opik Compare?

Opik competes in the **LLM observability / AI agent evaluation** category alongside **LangSmith, Arize (Phoenix and Arize AX), Weights & Biases (Weave), Langfuse, and Braintrust**.

| Capability | Opik | LangSmith | Phoenix | Arize AX | Weights & Biases (Weave) | Langfuse | Braintrust |
|---|---|---|---|---|---|---|---|
| Open source | Yes, Apache-2.0 (full platform) | No | Source-available (Elastic License 2.0, not OSI-approved) | No | Open-source SDK/toolkit; self-managed platform requires a commercial license | MIT-licensed core platform; commercial enterprise modules | No |
| Self-hosted deployment | Yes | Enterprise only | Yes | Enterprise only | Enterprise only for Weave itself | Yes, core | Enterprise only |
| Free tier available (cloud or self-hosted) | Yes, both | Yes, cloud | Yes, self-hosted | Yes, cloud | Yes, cloud | Yes, both | Yes, cloud |
| Agent / multi-step tracing | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| LLM-as-a-judge evaluation | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Prompt management | Yes | Yes | Partly | Partly | Partly | Yes | Yes |
| Framework-agnostic | Yes | Partly, built around LangChain | Yes | Yes | Yes | Yes | Yes |

**When teams choose Opik:** Opik's full observability, evaluation, and optimization platform is Apache-2.0 licensed and free to self-host. Unlike closed platforms whose self-hosted deployment requires an Enterprise plan, Opik can be deployed without a commercial license, and it's framework-agnostic so it won't lock you into a single agent ecosystem. See the table above for where self-hosting and licensing differ across alternatives.

<br>

<a id="-frequently-asked-questions"></a>
## ❓ Frequently Asked Questions

#### Is Opik open source?
Opik is licensed under Apache 2.0. Its server, web application, and core observability and evaluation capabilities can be self-hosted without a commercial license.

#### Can I self-host Opik?
Yes. Opik can be deployed locally or in your own infrastructure using the documented self-hosting options.

#### Does Opik support AI agent tracing?
Yes. Opik captures multi-step traces containing LLM calls, tool executions, retrieval steps, and other agent activity.

#### Does Opik support LLM evaluation?
Yes. Opik supports datasets, experiments, code-based metrics, LLM-as-a-judge evaluation, and online evaluation.

#### Is Opik tied to a specific agent framework?
No. Opik is framework-agnostic and supports its SDK, OpenTelemetry, and framework-specific integrations.

<br>

<a id="%EF%B8%8F-opik-server-installation"></a>
## 🛠️ Opik Server Installation

Get your Opik server running in minutes. Choose the option that best suits your needs:

### Option 1: Comet.com Cloud (Easiest & Recommended)

Access Opik instantly without any setup. Ideal for quick starts and hassle-free maintenance.

👉 [Create your free Comet account](https://www.comet.com/signup?from=llm&utm_source=opik&utm_medium=github&utm_content=install_create_link&utm_campaign=opik)

### Option 2: Self-Host Opik for Full Control

Deploy Opik in your own environment. Choose between Docker for local setups or Kubernetes for scalability.

#### Self-Hosting with Docker Compose (for Local Development & Testing)

This is the simplest way to get a local Opik instance running. Note the new `./opik.sh` installation script:


## configuration

./opik.sh --help
```

Use the `--help` or `--info` options to troubleshoot issues. Dockerfiles now ensure containers run as non-root users for enhanced security. Once all is up and running, you can now visit [localhost:5173](http://localhost:5173) on your browser! For detailed instructions, see the [Local Deployment Guide](https://www.comet.com/docs/opik/self-host/local_deployment?from=llm&utm_source=opik&utm_medium=github&utm_content=self_host_link&utm_campaign=opik).

#### Self-Hosting with Kubernetes & Helm (for Scalable Deployments)

For production or larger-scale self-hosted deployments, Opik can be installed on a Kubernetes cluster using our Helm chart. Click the badge for the full [Kubernetes Installation Guide using Helm](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik).

[![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326ce5.svg?&logo=kubernetes&logoColor=white)](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik)

<a id="-opik-client-sdk"></a>
## 💻 Opik Client SDK

Opik provides a suite of client libraries and a REST API to interact with the Opik server. This includes SDKs for Python and TypeScript, plus first-party [OpenTelemetry](https://www.comet.com/docs/opik/tracing/opentelemetry/overview?from=llm&utm_source=opik&utm_medium=github&utm_content=otel_link&utm_campaign=opik) support: any language with an OpenTelemetry SDK — including [Java](https://www.comet.com/docs/opik/integrations/spring-ai?from=llm&utm_source=opik&utm_medium=github&utm_content=java_link&utm_campaign=opik), [Ruby](https://www.comet.com/docs/opik/integrations/opentelemetry-ruby-sdk?from=llm&utm_source=opik&utm_medium=github&utm_content=ruby_link&utm_campaign=opik), and .NET — can send traces to Opik. For detailed API and SDK references, see the [Opik Client Reference Documentation](https://www.comet.com/docs/opik/reference/overview?from=llm&utm_source=opik&utm_medium=github&utm_content=reference_link&utm_campaign=opik).
