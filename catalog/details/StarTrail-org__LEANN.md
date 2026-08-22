# StarTrail-org/LEANN

[MLsys2026]: RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application on your personal device.

## features

<p align="center">
  <img src="assets/effects.png" alt="LEANN vs Traditional Vector DB Storage Comparison" width="70%">
</p>

> **The numbers speak for themselves:** Index 60 million text chunks in just 6GB instead of 201GB. From emails to browser history, everything fits on your laptop. [See detailed benchmarks for different applications below ↓](#-storage-comparison)


🔒 **Privacy:** Your data never leaves your laptop. No OpenAI, no cloud, no "terms of service".

🪶 **Lightweight:** Graph-based recomputation eliminates heavy embedding storage, while smart graph pruning and CSR format minimize graph storage overhead. Always less storage, less memory usage!

📦 **Portable:** Transfer your entire knowledge base between devices (even with others) with minimal cost - your personal AI memory travels with you.

📈 **Scalability:** Handle messy personal data that would crash traditional vector DBs, easily managing your growing personalized data and agent generated memory!

✨ **No Accuracy Loss:** Maintain the same search quality as heavyweight solutions while using 97% less storage.

## installation

### 📦 Prerequisites: Install uv

[Install uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) first if you don't have it. Typically, you can install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🚀 Quick Install

Clone the repository to access all examples and try amazing applications,

```bash
git clone https://github.com/yichuan-w/LEANN.git leann
cd leann
```

and install LEANN from [PyPI](https://pypi.org/project/leann/) to run them immediately:

```bash
uv venv
source .venv/bin/activate
uv pip install leann

# CPU-only (Linux): use the `cpu` extra (e.g. `leann[cpu]`)
```

<!--
> Low-resource? See "Low-resource setups" in the [Configuration Guide](docs/configuration-guide.md#low-resource-setups). -->

<details>
<summary>
<strong>🔧 Build from Source (Recommended for development)</strong>
</summary>



```bash
git clone https://github.com/yichuan-w/LEANN.git leann
cd leann
git submodule update --init --recursive
```

**macOS:**

Note: DiskANN requires MacOS 13.3 or later.

```bash
brew install libomp boost protobuf zeromq pkgconf
uv sync --extra diskann
```

**Linux (Ubuntu/Debian):**

Note: On Ubuntu 20.04, you may need to build a newer Abseil and pin Protobuf (e.g., v3.20.x) for building DiskANN. See [Issue #30](https://github.com/yichuan-w/LEANN/issues/30) for a step-by-step note.

You can manually install [Intel oneAPI MKL](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html) instead of `libmkl-full-dev` for DiskANN. You can also use `libopenblas-dev` for building HNSW only, by removing `--extra diskann` in the command below.

```bash
sudo apt-get update && sudo apt-get install -y \
  libomp-dev libboost-all-dev protobuf-compiler libzmq3-dev \
  pkg-config libabsl-dev libaio-dev libprotobuf-dev \
  libmkl-full-dev

uv sync --extra diskann
```

**Linux (Arch Linux):**

```bash
sudo pacman -Syu && sudo pacman -S --needed base-devel cmake pkgconf git gcc \
  boost boost-libs protobuf abseil-cpp libaio zeromq

# For MKL in DiskANN
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/paru-bin.git
cd paru-bin && makepkg -si
paru -S intel-oneapi-mkl intel-oneapi-compiler
source /opt/intel/oneapi/setvars.sh

uv sync --extra diskann
```

**Linux (RHEL / CentOS Stream / Oracle / Rocky / AlmaLinux):**

See [Issue #50](https://github.com/yichuan-w/LEANN/issues/50) for more details.

```bash
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y libomp-devel boost-devel protobuf-compiler protobuf-devel \
  abseil-cpp-devel libaio-devel zeromq-devel pkgconf-pkg-config

# For MKL in DiskANN
sudo dnf install -y intel-oneapi-mkl intel-oneapi-mkl-devel \
  intel-oneapi-openmp || sudo dnf install -y intel-oneapi-compiler
source /opt/intel/oneapi/setvars.sh

uv sync --extra diskann
```

**Windows:**

Requires [Visual Studio 2022 Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022) with the **C++ desktop development** workload, and [vcpkg](https://github.com/microsoft/vcpkg).

```powershell
# Install toolchain (if not already present)
choco install cmake swig pkgconfiglite nuget.commandline -y

# Install C++ dependencies via vcpkg
vcpkg install zeromq:x64-windows openblas:x64-windows lapack:x64-windows `
  boost-program-options:x64-windows protobuf:x64-windows

## configuration

$env:CMAKE_PREFIX_PATH = "$env:VCPKG_ROOT\installed\x64-windows"
$env:PKG_CONFIG_PATH = "$env:VCPKG_ROOT\installed\x64-windows\lib\pkgconfig"
$env:PKG_CONFIG_EXECUTABLE = "C:\ProgramData\chocolatey\bin\pkg-config.exe"
$env:OPENBLAS_LIB = "$env:VCPKG_ROOT\installed\x64-windows\lib\openblas.lib"
$env:PATH += ";$env:VCPKG_ROOT\installed\x64-windows\bin"
$env:PATH += ";$env:VCPKG_ROOT\installed\x64-windows\tools\protobuf"

uv sync --extra diskann
```

</details>

## tools

--index-dir DIR              # Directory to store the index (default: current directory)
--query "YOUR QUESTION"      # Single query mode. Omit for interactive chat (type 'quit' to exit), and now you can play with your index interactively
--max-items N                # Limit data preprocessing (default: -1, process all data)
--force-rebuild              # Force rebuild index even if it exists

# Embedding Parameters
--embedding-model MODEL      # e.g., facebook/contriever, text-embedding-3-small, mlx-community/Qwen3-Embedding-0.6B-8bit or nomic-embed-text
--embedding-mode MODE        # sentence-transformers, openai, mlx, or ollama

# LLM Parameters (Text generation models)
--llm TYPE                   # LLM backend: openai, ollama, hf, or anthropic (default: openai)
--llm-model MODEL            # Model name (default: gpt-4o) e.g., gpt-4o-mini, llama3.2:1b, Qwen/Qwen2.5-1.5B-Instruct
--thinking-budget LEVEL      # Thinking budget for reasoning models: low/medium/high (supported by o3, o3-mini, GPT-Oss:20b, and other reasoning models)

# Search Parameters
--top-k N                    # Number of results to retrieve (default: 20)
--search-complexity N        # Search complexity for graph traversal (default: 32)

# Chunking Parameters
--chunk-size N               # Size of text chunks (default varies by source: 256 for most, 192 for WeChat)
--chunk-overlap N            # Overlap between chunks (default varies: 25-128 depending on source)

# Index Building Parameters
--backend-name NAME          # Backend to use: hnsw or diskann (default: hnsw)
--graph-degree N             # Graph degree for index construction (default: 32)
--build-complexity N         # Build complexity for index construction (default: 64)
--compact / --no-compact     # Use compact storage (default: true). Must be `no-compact` for `no-recompute` build.
--recompute / --no-recompute # Enable/disable embedding recomputation (default: enabled). Should not do a `no-recompute` search in a `recompute` build.
```

</details>

### 📄 Personal Data Manager: Process Any Documents (`.pdf`, `.txt`, `.md`)!

Ask questions directly about your personal PDFs, documents, and any directory containing your files!

<p align="center">
  <img src="videos/paper_clear.gif" alt="LEANN Document Search Demo" width="600">
</p>

The example below asks a question about summarizing our paper (uses default data in `data/`, which is a directory with diverse data sources: two papers, Pride and Prejudice, and a Technical report about LLM in Huawei in Chinese), and this is the **easiest example** to run here:

```bash
source .venv/bin/activate # Don't forget to activate the virtual environment
python -m apps.document_rag --query "What are the main techniques LEANN explores?"
```

<details>
<summary><strong>📋 Click to expand: Document-Specific Arguments</strong></summary>

#### Parameters
```bash
--data-dir DIR           # Directory containing documents to process (default: data)
--file-types .ext .ext   # Filter by specific file types (optional - all LlamaIndex supported types if omitted)
```

#### Example Commands
```bash
# Process all documents with larger chunks for academic papers
python -m apps.document_rag --data-dir "~/Documents/Papers" --chunk-size 1024

# Filter only markdown and Python files with smaller chunks
python -m apps.document_rag --data-dir "./docs" --chunk-size 256 --file-types .md .py

# Enable AST-aware chunking for code files
python -m apps.document_rag --enable-code-chunking --data-dir "./my_project"

# Or use the specialized code RAG for better code understanding
python -m apps.code_rag --repo-dir "./my_codebase" --query "How does authentication work?"
```

</details>

### 🎨 ColQwen: Multimodal PDF Retrieval with Vision-Language Models

Search through PDFs using both text and visual understanding with ColQwen2/ColPali models. Perfect for research papers, technical documents, and any PDFs with complex layouts, figures, or diagrams.

> **🍎 Mac Users**: ColQwen is optimized for A

## limitations

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Core Contributors: [Yichuan Wang](https://yichuan-w.github.io/) & [Zhifei Li](https://github.com/andylizf).

Active Contributors: [Gabriel Dehan](https://github.com/gabriel-dehan), [Aakash Suresh](https://github.com/ASuresh0524)


We welcome more contributors! Feel free to open issues or submit PRs.

This work is done at [**Berkeley Sky Computing Lab**](https://sky.cs.berkeley.edu/).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yichuan-w/LEANN&type=Date)](https://www.star-history.com/#yichuan-w/LEANN&Date)
<p align="center">
  <strong>⭐ Star us on GitHub if Leann is useful for your research or applications!</strong>
</p>

<p align="center">
  Made with ❤️ by the Leann team
</p>

## 🤖 Explore LEANN with AI

LEANN is indexed on [DeepWiki](https://deepwiki.com/yichuan-w/LEANN), so you can ask questions to LLMs using Deep Research to explore the codebase and get help to add new features.
