# neuml/txtai

💡 All-in-one AI framework for semantic search, LLM orchestration and language model workflows

## features

![why](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/why.png#gh-light-mode-only)
![why](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/why-dark.png#gh-dark-mode-only)

New vector databases, LLM frameworks and everything in between are sprouting up daily. Why build with txtai?

- Up and running in minutes with [pip](https://neuml.github.io/txtai/install/) or [Docker](https://neuml.github.io/txtai/cloud/)
```python
# Get started in a couple lines
import txtai

embeddings = txtai.Embeddings()
embeddings.index(["Correct", "Not what we hoped"])
embeddings.search("positive", 1)
#[(0, 0.29862046241760254)]
```
- Built-in API makes it easy to develop applications using your programming language of choice
```yaml
# app.yml
embeddings:
    path: sentence-transformers/all-MiniLM-L6-v2
```
```bash
CONFIG=app.yml uvicorn "txtai.api:app"
curl -X GET "http://localhost:8000/search?query=positive"
```
- Run local - no need to ship data off to disparate remote services
- Work with micromodels all the way up to large language models (LLMs)
- Low footprint - install additional dependencies and scale up when needed
- [Learn by example](https://neuml.github.io/txtai/examples) - notebooks cover all available functionality

## Use Cases

The following sections introduce common txtai use cases. A comprehensive set of over 70 [example notebooks and applications](https://neuml.github.io/txtai/examples) are also available.

### Semantic Search

Build semantic/similarity/vector/neural search applications.

![demo](https://raw.githubusercontent.com/neuml/txtai/master/demo.gif)

Traditional search systems use keywords to find data. Semantic search has an understanding of natural language and identifies results that have the same meaning, not necessarily the same keywords.

![search](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/search.png#gh-light-mode-only)
![search](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/search-dark.png#gh-dark-mode-only)

Get started with the following examples.

| Notebook  | Description  |       |
|:----------|:-------------|------:|
| [Introducing txtai](https://github.com/neuml/txtai/blob/master/examples/01_Introducing_txtai.ipynb) [▶️](https://www.youtube.com/watch?v=SIezMnVdmMs) | Overview of the functionality provided by txtai | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/01_Introducing_txtai.ipynb) |
| [Similarity search with images](https://github.com/neuml/txtai/blob/master/examples/13_Similarity_search_with_images.ipynb) | Embed images and text into the same space for search | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/13_Similarity_search_with_images.ipynb) |
| [Build a QA database](https://github.com/neuml/txtai/blob/master/examples/34_Build_a_QA_database.ipynb) | Question matching with semantic search | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/34_Build_a_QA_database.ipynb) |
| [Semantic Graphs](https://github.com/neuml/txtai/blob/master/examples/38_Introducing_the_Semantic_Graph.ipynb) | Explore topics, data connectivity and run network analysis| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtai/blob/master/examples/38_Introducing_the_Semantic_Graph.ipynb) |

### LLM Orchestration

Autonomous agents, retrieval augmented generation (RAG), chat with your data, pipelines and workflows that interface with large language models (LLMs).

![llm](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/llm.png)

See below to learn more.

| Notebook  | Description  |       |
|:----------|:-------------|------:|
| [Prompt templates and task chains]

## installation

![install](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/install.png#gh-light-mode-only)
![install](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/install-dark.png#gh-dark-mode-only)

The easiest way to install is via pip and PyPI

```
pip install txtai
```

Python 3.10+ is supported. Using a Python [virtual environment](https://docs.python.org/3/library/venv.html) is recommended.

See the detailed [install instructions](https://neuml.github.io/txtai/install) for more information covering [optional dependencies](https://neuml.github.io/txtai/install/#optional-dependencies), [environment specific prerequisites](https://neuml.github.io/txtai/install/#environment-specific-prerequisites), [installing from source](https://neuml.github.io/txtai/install/#install-from-source), [conda support](https://neuml.github.io/txtai/install/#conda), [lightweight minimal installation](https://neuml.github.io/txtai/install/#minimal-install) and how to [run with containers](https://neuml.github.io/txtai/cloud).

## Model guide

![models](https://raw.githubusercontent.com/neuml/txtai/master/docs/images/models.png)

See the table below for the current recommended models. These models all allow commercial use and offer a blend of speed and performance.

| Component                                                                     | Model(s)                                                                 |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [Embeddings](https://neuml.github.io/txtai/embeddings)                        | [all-MiniLM-L6-v2](https://hf.co/sentence-transformers/all-MiniLM-L6-v2) | 
| [Image Captions](https://neuml.github.io/txtai/pipeline/image/caption)        | [BLIP](https://hf.co/Salesforce/blip-image-captioning-base)              |
| [Labels - Zero Shot](https://neuml.github.io/txtai/pipeline/text/labels)      | [DeBERTa v3 Zeroshot](https://hf.co/MoritzLaurer/deberta-v3-base-zeroshot-v2.0-c) |
| [Labels - Fixed](https://neuml.github.io/txtai/pipeline/text/labels)          | Fine-tune with [training pipeline](https://neuml.github.io/txtai/pipeline/train/trainer)          |
| [Large Language Model (LLM)](https://neuml.github.io/txtai/pipeline/text/llm) | [Gemma 4 31B](https://hf.co/google/gemma-4-31B) |
| [Summarization](https://neuml.github.io/txtai/pipeline/text/summary)          | [DistilBART](https://hf.co/sshleifer/distilbart-cnn-12-6)                |
| [Text-to-Speech](https://neuml.github.io/txtai/pipeline/audio/texttospeech)   | [ESPnet JETS](https://hf.co/NeuML/ljspeech-jets-onnx)                    |
| [Transcription](https://neuml.github.io/txtai/pipeline/audio/transcription)   | [Whisper](https://hf.co/openai/whisper-base)                             | 
| [Translation](https://neuml.github.io/txtai/pipeline/text/translation)        | [OPUS Model Series](https://hf.co/Helsinki-NLP)                          |

Models can be loaded as either a path from the Hugging Face Hub or a local directory. Model paths are optional, defaults are loaded when not specified. For tasks with no recommended model, txtai uses the default models as shown in the Hugging Face Tasks guide.

See the following links to learn more.

- [Hugging Face Tasks](https://hf.co/tasks)
- [Hugging Face Model Hub](https://hf.co/models)
- [Embeddings Leaderboard](https://hf.co/spaces/mteb/leaderboard)
- [LLM Leaderboard](https://hf.co/spaces/lmarena-ai/arena-leaderboard)

## Powered by txtai

The following applications are powered by txtai.

![apps](https://raw.githubusercontent.com/neuml/txtai/master/apps.jpg)

| Application  | Description  |
|:------------ |:-------------|
| [rag](https://github.com/neuml/rag) | Retrieval Augmented Generation (RAG) application |
| [ncoder](https://github.com/neuml/ncoder) | Open-Source AI coding agent |
| [paperai](https://github.com/neuml/paperai) | AI for medical and s
