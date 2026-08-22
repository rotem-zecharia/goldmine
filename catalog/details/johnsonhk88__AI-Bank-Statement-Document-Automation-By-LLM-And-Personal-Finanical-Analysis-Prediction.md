# johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction

AI Bank Statement Document Automation By LLM model and Personal Finanical Analysis

## features

- **Advanced PDF Parsing** — YOLO layout detection + OCR + LLM-based table extraction
- **Multi-harness agents** — CrewAI baseline, LangChain **Deep Agents** (agentskills.io), **Hermes** (Docker sandbox)
- **Agent Skills** — Domain skills for bank-statement parsing, PII redaction, financial analysis, RAG, and output format
- **Local LLM First** — LM Studio and Ollama via LiteLLM (async `acompletion`)
- **Reasoning Model Support** — Handles models that return content in `reasoning_content`
- **Secure RAG Pipeline** — PII redaction **before** embedding into vector database (Qdrant / Chroma)
- **Financial Intelligence** — Income/expense categorization, trend analysis, natural language querying
- **Full-Stack API** — FastAPI + PostgreSQL + Celery + React SPA (REST auth, async document processing, agent runs)
- **GPU Acceleration** — NVIDIA GPU support for PyTorch embeddings and LLM inference (<2× build time vs CPU)
- **Development Notebook** — Jupyter notebook for CrewAI experimentation
- **MLflow Integration** — Trace LLM calls and agent workflows (CrewAI path)

---

## installation

```bash
git clone https://github.com/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction.git
cd AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## requirements

- Docker 24+ with BuildKit (`DOCKER_BUILDKIT=1`)
- Docker Compose v2+
- NVIDIA Container Toolkit (for GPU support — see below)
- NVIDIA driver ≥ 580 (RTX Pro 4500 Blackwell tested; works with most RTX 20+ GPUs)

## configuration

cp infra/.env.example infra/.env

## tools

cd infra && DOCKER_BUILDKIT=1 docker compose --profile prod up -d --build

## limitations

- Production FastAPI backend (harness-selectable)
- Multi-document collections / workspaces
- Advanced financial forecasting
- Docker + Kubernetes deployment
- Improved Streamlit dashboard with charts
- Shared skill sync tooling across harnesses
- Stronger PII (names/addresses) and production embeddings for Deep Agents

---
