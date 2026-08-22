# BerriAI/litellm

The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropi

## features

Managing LLM calls across providers gets complicated fast — different SDKs, auth patterns, request formats, and error types for every model. LiteLLM removes that friction:

- **Unified API** — one interface for 100+ LLMs, no provider-specific SDK juggling
- **Drop-in OpenAI compatibility** — swap providers without rewriting your code
- **Production-ready gateway** — virtual keys, spend tracking, guardrails, load balancing, and an admin dashboard out of the box
- **8ms P95 latency** at 1k RPS ([benchmarks](https://docs.litellm.ai/docs/benchmarks))

### OSS Adopters

<table>
  <tr>
    <td><img height="60" alt="Stripe" src="https://github.com/user-attachments/assets/f7296d4f-9fbd-460d-9d05-e4df31697c4b" /></td>
    <td><img height="60" alt="image" src="https://github.com/user-attachments/assets/436fca71-988b-40bb-b5fe-8450c80fdbd0" /></td>
    <td><img height="60" alt="Google ADK" src="https://github.com/user-attachments/assets/caf270a2-5aee-45c4-8222-41a2070c4f19" /></td>
    <td><img height="60" alt="Greptile" src="https://github.com/user-attachments/assets/3db0ae72-0843-4005-a56d-bba1dde2193d" /></td>
    <td><img height="60" alt="OpenHands" src="https://github.com/user-attachments/assets/a6150c4c-149e-4cae-888b-8b92be6e003f" /></td>
    <td><h2>Netflix</h2></td>
    <td><img height="60" alt="OpenAI Agents SDK" src="https://github.com/user-attachments/assets/c02f7be0-8c2e-4d27-aea7-7c024bfaebc0" /></td>
  </tr>
</table>

---

## Features

<details open>
<summary><b>LLMs</b> - Call 100+ LLMs (Python SDK + AI Gateway)</summary>

[**All Supported Endpoints**](https://docs.litellm.ai/docs/supported_endpoints) - `/chat/completions`, `/responses`, `/embeddings`, `/images`, `/audio`, `/batches`, `/rerank`, `/a2a`, `/messages` and more.

### Python SDK

```shell
uv add litellm
```

```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-key"

# OpenAI
response = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}])

# Anthropic  
response = completion(model="anthropic/claude-sonnet-4-20250514", messages=[{"role": "user", "content": "Hello!"}])
```

### AI Gateway (Proxy Server)

[**Getting Started - E2E Tutorial**](https://docs.litellm.ai/docs/proxy/docker_quick_start) - Setup virtual keys, make your first request

```shell
uv tool install 'litellm[proxy]'
litellm --model gpt-4o
```

```python
import openai

client = openai.OpenAI(api_key="anything", base_url="http://0.0.0.0:4000")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

[**Docs: LLM Providers**](https://docs.litellm.ai/docs/providers)

</details>

<details>
<summary><b>Agents</b> - Invoke A2A Agents (Python SDK + AI Gateway)</summary>

[**Supported Providers**](https://docs.litellm.ai/docs/a2a#add-a2a-agents) - LangGraph, Vertex AI Agent Engine, Azure AI Foundry, Bedrock AgentCore, Pydantic AI

### Python SDK - A2A Protocol

```python
from litellm.a2a_protocol import A2AClient
from a2a.types import SendMessageRequest, MessageSendParams
from uuid import uuid4

client = A2AClient(base_url="http://localhost:10001")

request = SendMessageRequest(
    id=str(uuid4()),
    params=MessageSendParams(
        message={
            "role": "user",
            "parts": [{"kind": "text", "text": "Hello!"}],
            "messageId": uuid4().hex,
        }
    )
)
response = await client.send_message(request)
```

### AI Gateway (Proxy Server)

**Step 1.** [Add your Agent to the AI Gateway](https://docs.litellm.ai/docs/a2a#adding-your-agent) — set `protocolVersion` to `1.0` or `0.3` per agent

**Step 2.** Call Agent via A2A SDK (requires `a2a-sdk>=1.1.0`)

```python
import httpx
from a2a.client import A2ACardResolver, ClientConfig, ClientFactory
from a2a.types import Message, Part, Role, SendMessageRequest
from a2a.utils.constants import TransportProtocol
from uuid import uuid4

base_url = "h

## installation

This requires uv to be installed.

```bash
git clone https://github.com/BerriAI/litellm.git
cd litellm
make install-dev    # Install development dependencies
make format         # Format your code
make lint           # Run all linting checks
make test-unit      # Run unit tests
make format-check   # Check formatting only
```

For detailed contributing guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

> **📖 Contributing to documentation?** The LiteLLM docs have moved to a separate repository: [BerriAI/litellm-docs](https://github.com/BerriAI/litellm-docs). Please open doc PRs there. Docs are served at [docs.litellm.ai](https://docs.litellm.ai).

## Code Quality / Linting

LiteLLM follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Our automated checks include:
- **Black** for code formatting
- **Ruff** for linting and code quality
- **MyPy** for type checking
- **Circular import detection**
- **Import safety checks**


All these checks must pass before your PR can be merged.


# Support / talk with founders

- [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
- [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
- [Community Slack 💭](https://www.litellm.ai/support)
- Our emails ✉️ ishaan@berri.ai / krrish@berri.ai

# Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<a href="https://github.com/BerriAI/litellm/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=BerriAI/litellm" />
</a>
