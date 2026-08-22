# huggingface/datasets

🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools

## features

🤗 Datasets is designed to let the community easily add and share new datasets, and provides powerful capabilities for data manipulation:

| Feature | Description |
|---------|-------------|
| 📦 **One-line dataset loading** | Load AI-ready datasets from the [Hugging Face Hub](https://huggingface.co/datasets) or local files with `load_dataset()` |
| 🔍 **Multiple formats** | Native support for CSV, JSON, JSONL, Parquet, Arrow, XML, Text, Webdataset, and more |
| 🖼️ **Multi-modal data** | Built-in support for text, audio, image, video, PDF, and NIfTI (3D medical) data |
| 🚀 **Streaming mode** | Stream datasets without downloading — iterate over data on-the-fly with `streaming=True` (now up to **100x faster** with Xet backend) |
| 💾 **HF Storage Buckets** | Read and write directly from/to [Hugging Face Storage Buckets](https://huggingface.co/docs/hub/storage-buckets) for mutable, large-scale raw data |
| 🧠 **AI Agent Traces** | Load and process AI agent traces (prompts, tool calls, responses) from the Hub |
| ⚡ **Apache Arrow backend** | Zero-copy memory-mapped storage — datasets naturally free you from RAM limitations |
| 🔄 **Smart caching** | Never wait for your data to process twice — cached results are automatically reused |
| 📊 **Multi-framework interoperability** | Native conversion to/from NumPy, Pandas, Polars, Arrow, PyTorch, TensorFlow, JAX, and Spark |
| 🏎️ **Multi-processing** | Fast parallel data processing with `map(num_proc=N)` |
| 🔎 **Search & index** | Built-in FAISS and Elasticsearch index support for similarity search |
| 📦 **JSON type** | Flexible JSON/structured data support with `Json()` feature type |

## requirements

🤗 Datasets supports various optional features via extras:

```bash

## installation

🤗 Datasets is made to be very simple to use — the API is centered around a single function, `datasets.load_dataset(dataset_name, **kwargs)`, that instantiates a dataset.

Here is a quick example:

```python
from datasets import load_dataset
