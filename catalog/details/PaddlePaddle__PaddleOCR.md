# PaddlePaddle/PaddleOCR

Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

## features

### 📄 Intelligent Document Parsing (LLM-Ready)
> *Transforming messy visuals into structured data for the LLM era.*

* **SOTA Document VLM**: Featuring **PaddleOCR-VL-1.6 (0.9B)**, the industry's leading lightweight vision-language model for document parsing. It achieves 96.3% accuracy on OmniDocBench v1.6, leads in text, formula, and table recognition, and shows significantly enhanced capabilities in ancient documents, rare characters, seals, and charts, with structured outputs in **Markdown** and **JSON** formats.
* **Structure-Aware Conversion**: Powered by **PP-StructureV3**, seamlessly convert complex PDFs and images into **Markdown** or **JSON**. Unlike the PaddleOCR-VL series models, it provides more fine-grained coordinate information, including table cell coordinates, text coordinates, and more.
* **Production-Ready Efficiency**: Achieve commercial-grade accuracy with an ultra-small footprint. Outperforms numerous closed-source solutions in public benchmarks while remaining resource-efficient for edge/cloud deployment.

### 🔍 Universal Text Recognition (Scene OCR)
> *The global gold standard for high-speed, multilingual text spotting.*

* **100+ Languages Supported**: Native recognition for a vast global library. **PP-OCRv6** supports 50 languages with a single unified model (Chinese, English, Japanese, and 46 Latin-script languages) — no model switching needed for multilingual documents.
* **Complex Element Mastery**: Beyond standard text recognition, we support **natural scene text spotting** across a wide range of environments, including IDs, street views, books, and industrial components
* **Performance Leap**: PP-OCRv6 achieves **+4.6% detection** and **+5.1% recognition** accuracy over PP-OCRv5, surpassing mainstream Vision-Language Models. 5.2× CPU inference speedup end-to-end.

<div align="center">
  <p>
      <img width="100%" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/Arch.jpg" alt="PaddleOCR Architecture">
  </p>
</div>

### 🛠️ Developer-Centric Ecosystem
* **Seamless Integration**: The premier choice for the AI Agent ecosystem—deeply integrated with **Dify, RAGFlow, Pathway, and Cherry Studio**.
* **LLM Data Flywheel**: A complete pipeline to build high-quality datasets, providing a sustainable "Data Engine" for fine-tuning Large Language Models.
* **One-Click Deployment**: Supports various hardware backends (NVIDIA GPU, Intel CPU, Kunlunxin XPU, and diverse AI Accelerators).


## 📣 Recent updates

### 🔥 2026.07.22: HPD-Parsing is now available
- **HPD-Parsing** is a lightweight vision-language model designed for high-throughput document parsing. It adopts a hierarchical parallel decoding paradigm and Progressive Multi-Token Prediction (P-MTP), achieving a peak throughput of 4,752 tokens/s on public benchmarks while maintaining competitive parsing accuracy.
- HPD-Parsing supports both OpenAI-compatible serving and local inference through a customized vLLM runtime, making it suitable for document parsing scenarios with high demands on inference efficiency and deployment throughput.
- See the [HPD-Parsing usage tutorial](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/HPD-Parsing.html) for environment setup, serving, and local inference instructions.

<details>
<summary><strong>2026.06.11: Release of PaddleOCR 3.7.0</strong></summary>

- PP-OCRv6 highlights:

    - **Accuracy boost**: Medium tier achieves +4.6% detection and +5.1% recognition over PP-OCRv5_server, surpassing mainstream VLMs (Qwen3-VL-235B, GPT-5.5) with only 34.5M parameters.
    - **50 languages unified**: Single model covers Chinese, English, Japanese, and 46 Latin-script languages — no model switching needed.
    - **Specialized scenarios**: Major improvements in digital displays, dot-matrix characters, tire prints, and industrial text recognition.
    - **Faster inference**: 5.2× CPU speedup (OpenVINO), 6.1× on Apple M4 (tiny), 0.13s on A100 GPU.
    - **Three tiers for 

## installation

### Step 1: Try Online
PaddleOCR official website provides interactive **Experience Center** and **APIs**—no setup required, just one click to experience.

👉 [Visit Official Website](https://www.paddleocr.com)

### Step 2: Local Deployment
For local usage, please refer to the following documentation based on your needs:

- **PP-OCR Series**: See [PP-OCR Documentation](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/OCR.html)
- **PaddleOCR-VL Series**: See [PaddleOCR-VL Documentation](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html)
- **PP-StructureV3**: See [PP-StructureV3 Documentation](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html)
- **More Capabilities**: See [More Capabilities Documentation](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/pipeline_overview.html)
