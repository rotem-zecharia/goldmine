# Zipstack/unstract

LLM-Driven Extraction of Unstructured Data — Built for API Deployments & ETL Pipeline Workflows

## features

**Prompt Studio** — Define document extraction schemas with natural language. [Docs →](https://docs.unstract.com/unstract/unstract_platform/features/prompt_studio/prompt_studio_intro/)

![Prompt Studio](docs/assets/prompt_studio.gif)

**API Deployment** — Send a document over REST API, get JSON back. [Docs →](https://docs.unstract.com/unstract/unstract_platform/api_deployment/unstract_api_deployment_intro/)

![API Deployment](docs/assets/api_deployment.gif)

**ETL Pipeline** — Pull documents from a folder, process them, load to your warehouse. [Docs →](https://docs.unstract.com/unstract/unstract_platform/etl_pipeline/unstract_etl_pipeline_intro/)

**MCP Server** — Connect to AI agents (Claude, etc.) via Model Context Protocol. [Docs →](https://docs.unstract.com/unstract/unstract_platform/mcp/unstract_platform_mcp_server/)

**n8n Node** — Drop into existing automation workflows. [Docs →](https://docs.unstract.com/unstract/unstract_platform/api_deployment/unstract_api_deployment_n8n_custom_node/)

## requirements

- Linux or macOS (Intel or M-series)
- Docker & Docker Compose
- 8 GB RAM minimum
- Git

### Run Locally

```bash
# Clone and start
git clone https://github.com/Zipstack/unstract.git
cd unstract
./run-platform.sh
```

That's it!

- Visit [http://frontend.unstract.localhost](http://frontend.unstract.localhost) in your browser
- Login with username: `unstract` password: `unstract`
- Start extracting data!

## configuration

### Docker Compose

```bash
# Pull and run entire Unstract platform with default env config.
./run-platform.sh

# Pull and run docker containers with a specific version tag.
./run-platform.sh -v v0.1.0

## installation

./run-platform.sh -u

# Upgrade existing Unstract platform setup by pulling a specific version.
./run-platform.sh -u -v v0.2.0

# Build docker images locally as a specific version tag.
./run-platform.sh -b -v v0.1.0

# Build docker images locally from working branch as `current` version tag.
./run-platform.sh -b -v current

# Display the help information.
./run-platform.sh -h

# Only do setup of environment files.
./run-platform.sh -e

# Only do docker images pull with a specific version tag.
./run-platform.sh -p -v v0.1.0

# Only do docker images pull by building locally with a specific version tag.
./run-platform.sh -p -b -v v0.1.0

# Upgrade existing Unstract platform setup with docker images built locally from working branch as `current` version tag.
./run-platform.sh -u -b -v current

# Pull and run docker containers in detached mode.
./run-platform.sh -d -v v0.1.0
```

## 🔐 Backup Encryption Key

> [!WARNING]
> This key encrypts adapter credentials — losing it makes existing adapters inaccessible!

Copy the value of `ENCRYPTION_KEY` from `backend/.env` or `platform-service/.env` to a secure location.

## 🏗️ Unstract Architecture

```text
┌────────────────────────────────────────────────────────────┐
│                          Unstract                          │
├─────────────┬─────────────┬─────────────┬──────────────────┤
│  Frontend   │   Backend   │   Worker    │ Platform Service │
│  (React)    │  (Django)   │  (Celery)   │   (FastAPI)      │
├─────────────┴─────────────┴─────────────┴──────────────────┤
│                      Cache (Redis)                         │
├────────────────────────────────────────────────────────────┤
│                  Message Queue (RabbitMQ)                  │
├────────────────────────────────────────────────────────────┤
│                   Database (PostgreSQL)                    │
├────────────────────────────────────────────────────────────┤
│  LLM Adapters    │  Vector DBs    │  Text Extractors       │
│  (OpenAI, etc.)  │ (Qdrant, etc.) │  (LLMWhisperer)        │
└────────────────────────────────────────────────────────────┘
```

Also see [architecture](docs/ARCHITECTURE.md).

## 📄 Document File Formats

| Category | Formats |
|----------|---------|
| Documents | PDF, DOCX, DOC, ODT, TXT, CSV, JSON |
| Spreadsheets | XLSX, XLS, ODS |
| Presentations | PPTX, PPT, ODP |
| Images | PNG, JPG, JPEG, TIFF, BMP, GIF, WEBP |

## 🔌 Connectors & Adapters

### LLM Providers

| Provider | Status | Provider | Status |
|----------|--------|----------|--------|
| OpenAI | ✅ | Azure OpenAI | ✅ |
| OpenAI Compatible | ✅ | Anthropic Claude | ✅ |
| AWS Bedrock | ✅ | Google Gemini | ✅ |
| Ollama (local) | ✅ | Mistral AI | ✅ |
| Anyscale | ✅ | | |

### Vector Databases

| Provider | Status | Provider | Status |
|----------|--------|----------|--------|
| Qdrant | ✅ | Pinecone | ✅ |
| Weaviate | ✅ | PostgreSQL | ✅ |
| Milvus | ✅ | | |

### Text Extractors

| Provider | Status |
|----------|--------|
| LLMWhisperer | ✅ |
| Unstructured.io | ✅ |
| LlamaIndex Parse | ✅ |

### ETL Sources & Destinations

**Sources:** AWS S3, MinIO, Google Cloud Storage, Azure Blob, Google Drive, Dropbox, SFTP

**Destinations:** Snowflake, Amazon Redshift, Google BigQuery, PostgreSQL, MySQL, MariaDB, SQL Server, Oracle

[Full Connector List](https://docs.unstract.com/unstract/unstract_platform/setup_accounts/whats_needed)

## 🛠️ Development

### Change Default Credentials

Follow [these steps](backend/README.md#authentication) to change the default username and password.

### Local Development

```bash
# Install pre-commit hooks
./dev-env-cli.sh -p

# Run pre-commit checks
./dev-env-cli.sh -r
```

[Local Development Guide](https://docs.unstract.com/unstract/unstract_platform/user_guides/run_platform)

## 🏢 Use Cases by Industry

[Finance & Banking →](https://unstract.com/finance-automation/) | [Insurance →](https://unstract.com/insurance-automation/) | [Healthcare →](https://unstract.com/healthcare-automation/) | [Income Tax
