# langgenius/dify

Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without reb

## installation

> Before installing Dify, make sure your machine meets the following minimum system requirements:
>
> - CPU >= 2 Core
> - RAM >= 4 GiB

<br/>

The easiest way to start the Dify server is through [Docker Compose](docker/docker-compose.yaml). Before running Dify with the following commands, make sure that [Docker](https://docs.docker.com/get-docker/) and Docker Compose v2.24.0 or later are installed on your machine:

```bash
cd dify
cd docker
cp .env.example .env
docker compose up -d
```

After running, you can access the Dify dashboard in your browser at [http://localhost/install](http://localhost/install) and start the initialization process.

#### Seeking help

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

**5. Agent capabilities**:
You can define agents based on LLM Function Calling or ReAct, and add pre-built or custom tools for the agent. Dify provides 50+ built-in tools for AI agents, such as Google Search, DALL·E, Stable Diffusion and WolframAlpha.

**6. LLMOps**:
Monitor and analyze application logs and performance over time. You could continuously improve prompts, datasets, and models based on production data and annotations.

**7. Backend-as-a-Service**:
All of Dify's offerings come with corresponding APIs, so you could effortlessly integrate Dify into your own business logic.

## Using Dify

- **Cloud <br/>**
  We host a [Dify Cloud](https://dify.ai) service for anyone to try with zero setup. It provides all the capabilities of the self-deployed version, and includes 200 free GPT-4 calls in the sandbox plan. If you run into issues with Dify Cloud, [contact our Cloud support team](mailto:cloud@dify.ai?subject=%5BGitHub%5DDify%20Cloud%20Support).

- **Self-hosting Dify Community Edition<br/>**
  Quickly get Dify running in your environment with this [starter guide](#quick-start).
  Use our [documentation](https://docs.dify.ai) for further references and more in-depth instructions.

- **Dify for enterprise / organizations<br/>**
  We provide additional enterprise-centric features. [Send us an email](mailto:business@dify.ai?subject=%5BGitHub%5DBusiness%20License%20Inquiry) to discuss your enterprise needs. <br/>

## Staying ahead

Star Dify on GitHub and be instantly notified of new releases.

<img width="1344" height="720" alt="star" src="https://github.com/user-attachments/assets/dcd086d1-af0f-471b-ae52-1ad2fa040595" />
