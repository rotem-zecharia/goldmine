# katanaml/sparrow

Structured data extraction, instruction calling and agentic workflows with ML, LLM and Vision LLM

## features

The web UI provides a visual interface on top of the same API:

- **Drag & Drop**: Upload documents directly
- **Real-time Processing**: See results instantly
- **Data Query**: JSON based schema for data query
- **Structured Output**: JSON structured output

## 📑 Table of Contents

- [✨ Key Features](#-key-features)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quickstart](#-quickstart)
- [🛠️ Installation](#️-installation)
- [📚 Examples](#-examples)
- [💻 CLI Usage](#-cli-usage)
- [🌐 API Usage](#-api-usage)
- [🤖 Sparrow Agent](#-sparrow-agent)
- [📊 Dashboard](#-dashboard)
- [🔧 Pipeline Comparison](#-pipeline-comparison)
- [⚡ Performance Tips](#-performance-tips)
- [🔍 Troubleshooting](#-troubleshooting)
- [⭐ Star History](#-star-history)
- [📜 License](#-license)

## ✨ Key Features

🎯 **Universal Document Processing**: Handle invoices, receipts, forms, bank statements, tables    
🔧 **Pluggable Architecture**: Mix and match different pipelines (Sparrow Parse, Instructor, Agents)  
🖥️ **Multiple Backends**: MLX, Ollama, vLLM, Docker, Hugging Face Cloud GPU, Mistral OCR  
📱 **Multi-format Support**: Images (PNG, JPG) and multi-page PDFs  
🎨 **Schema Validation**: JSON schema-based extraction with automatic validation  
🌐 **API-First Design**: RESTful APIs for easy integration  
💬 **Instruction Calling**: Text processing, validation, decision making with Gemma, Mistral, Qwen 3.6, etc.  
📊 **Visual Monitoring**: Built-in dashboard and agent workflow tracking  
🔒 **Enterprise Ready**: Rate limiting, usage analytics, commercial licensing available  
🚀 **Local Vision LLMs**: Mistral, Qwen 3.6, DeepSeek OCR, dots.ocr, Gemma 4, etc.  
☁️ **Cloud OCR Backend**: Mistral OCR for cloud document extraction

## 🏗️ Architecture

![Sparrow Architecture](https://github.com/katanaml/sparrow/blob/main/sparrow-ui/assets/sparrow_architecture.jpeg)

### Core Components

| Component | Purpose | Use Case |
|-----------|---------|----------|
| **[Sparrow ML LLM](https://github.com/katanaml/sparrow/tree/main/sparrow-ml/llm)** | Main API engine | Document processing pipelines |
| **[Sparrow Parse](https://github.com/katanaml/sparrow/tree/main/sparrow-data/parse)** | Vision LLM library | Structured JSON extraction |
| **[Sparrow Agents](https://github.com/katanaml/sparrow/tree/main/sparrow-ml/agents)** | Workflow orchestration | Complex multi-step processing |
| **[Sparrow OCR](https://github.com/katanaml/sparrow/tree/main/sparrow-data/ocr)** | Text recognition | OCR preprocessing |
| **[Sparrow UI](https://github.com/katanaml/sparrow/tree/main/sparrow-ui/)** | Web interface | Interactive document processing |

## requirements

- **Python 3.12.10+** (use `pyenv` for version management)
- **macOS** (for MLX backend) or **Linux/Windows** (for other backends)
- **GPU** (make sure GPU have enough memory to run selected Vision LLM)

## installation

```bash
# 1. Install pyenv and Python 3.12.10
pyenv install 3.12.10
pyenv global 3.12.10

## configuration

python -m venv .env_sparrow_parse
source .env_sparrow_parse/bin/activate  # Linux/Mac
# or .env_sparrow_parse\Scripts\activate  # Windows

## tools

python api.py
```

Before running `pip install -r requirements_sparrow_parse.txt`, check your platform. If you are on macOS and want to run MLX backend, go to `requirements_sparrow_parse.txt` and make sure `sparrow-parse[mlx]` libary reference is defined. If you are running Sparrow on Linux/Windows, make sure to use `sparrow-parse` library reference, this will skip MLX related libraries.

### First Document Extraction

```bash
# Extract data from a bonds table
./sparrow.sh '[{"instrument_name":"str", "valuation":0}]' \
  --pipeline "sparrow-parse" \
  --options mlx \
  --options mlx-community/Qwen2.5-VL-72B-Instruct-4bit \
  --file-path "data/bonds_table.png"
```

**Result:**
```json
{
  "data": [
    {"instrument_name": "UNITS BLACKROCK...", "valuation": 19049},
    {"instrument_name": "UNITS ISHARES...", "valuation": 83488}
  ],
  "valid": "true"
}
```

Use `--options mlx` for MLX backend, `--options ollama` for Ollama backend, `--options vllm` for vLLM backend, `--options mistral` for Mistral OCR cloud backend. Make sure to provide correct Vision LLM model name, download model first separately with MLX, vLLM or Ollama.
