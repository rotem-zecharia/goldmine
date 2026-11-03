# langgenius/dify

Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without reb

## installation

> Before installing Dify, make sure your machine meets the following minimum system requirements:
>
> - CPU >= 2 Core
> - RAM >= 4 GiB

<br/>

The easiest way to start the Dify server is through [Docker Compose](docker/docker-compose.yaml). Install [Docker](https://docs.docker.com/get-docker/) with a running daemon, Docker Compose v2.35.0 or later, and OpenSSL.

For a new deployment, run the following commands from the repository root. For an existing deployment, preserve your `.env` and follow the [upgrade guidance](docker/README.md#review-configuration-after-an-upgrade).

```bash
cd docker
cp .env.example .env
openssl rand -hex 32
```

Open `.env` and set `DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN` to the generated value. Keep the default `COMPOSE_PROFILES` value for the bundled services. Service defaults load automatically; no additional configuration files are required.

From the same `docker` directory, start the services:

```bash
docker compose up -d
docker compose ps --all
```

Once the services are running, open [http://localhost/install](http://localhost/install) to complete the initial setup. The one-time `init_permissions` service is expected to exit with code `0`.

For optional settings and service overrides, see the [Docker deployment guide](docker/README.md#configure-dify).

### Seeking help

Please refer to our [FAQ](https://docs.dify.ai/getting-started/install-self-hosted/faqs) if you encounter problems setting up Dify. Reach out to [the community and us](#community--contact) if you are still having issues.

> If you'd like to contribute to Dify or do additional development, refer to our [guide to deploying from source code](https://docs.dify.ai/getting-started/install-self-hosted/local-source-code)

## features

**1. Workflow**:
Build and test powerful AI workflows on a visual canvas, leveraging all the following features and beyond.

**2. Comprehensive model support**:
Seamless integration with hundreds of proprietary / open-source LLMs from dozens of inference providers and self-hosted solutions, covering GPT, Mistral, Llama3, and any OpenAI API-compatible models. A full list of supported model providers can be found [here](https://docs.dify.ai/getting-started/readme/model-providers).

![providers-v5](https://github.com/langgenius/dify/assets/13230914/5a17bdbe-097a-4100-8363-40255b70f6e3)

**3. Prompt IDE**:
Intuitive interface for crafting prompts, comparing model performance, and adding additional features such as text-to-speech to a chat-based app.

**4. RAG Pipeline**:
Extensive RAG capabilities that cover everything from document ingestion to retrieval, with out-of-box support for text extraction from PDFs, PPTs, and other common document formats.

**5. Agent**: Autonomous agents with a sandbox of their own: they run commands, install software, and handle files to get open-ended tasks done. Describe the agent you want and it builds itself. Give it skills, connect tools from [Dify Marketplace](https://marketplace.dify.ai/?category=tool), MCP servers, or your own APIs, and put it to work as a chat app or as a step in any workflow.

**6. LLMOps**:
Monitor and analyze application logs and performance over time. You could continuously improve prompts, datasets, and models based on production data and annotations.

**7. Backend-as-a-Service**:
All of Dify's offerings come with corresponding APIs, so you could effortlessly integrate Dify into your own business logic.

## Using Dify

- **Cloud <br/>**
  We host [Dify Cloud](https://cloud.dify.ai) so you can try Dify without managing a server. See the [pricing page](https://dify.ai/pricing) for current plans and usage allowances. If you run into issues, [contact our Cloud support team](mailto:cloud@dify.ai?subject=%5BGitHub%5DDify%20Cloud%20Support).

- **Self-hosting Dify Community Edition<br/>**
  Quickly get Dify running in your environment with this [starter guide](#quick-start).
  Use our [documentation](https://docs.dify.ai) for further references and more in-depth instructions.

- **[Dify Enterprise](https://dify.ai/dify-enterprise)<br/>**
  For organizations requiring self-hosting, SSO, RBAC Security and Enterprise Support SLAs, please fill out [this form](https://share-na2.hsforms.com/14-09ff5HS92Sh4m3f4yrcw40s9fk) to speak to a solution representative. <br/>

## Staying ahead

Star Dify on GitHub and be instantly notified of new releases.

<img width="1344" height="720" alt="star" src="https://github.com/user-attachments/assets/dcd086d1-af0f-471b-ae52-1ad2fa040595" />
