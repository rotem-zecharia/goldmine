# FlagOpen/FlagEmbedding

Retrieval and Retrieval-augmented LLMs

## installation

### Using pip:
If you do not want to finetune the models, you can install the package without the finetune dependency:
```
pip install -U FlagEmbedding
```
If you want to finetune the models, you can install the package with the finetune dependency:
```
pip install -U FlagEmbedding[finetune]
```
### Install from sources:

Clone the repository and install
```
git clone https://github.com/FlagOpen/FlagEmbedding.git
cd FlagEmbedding
# If you do not need to finetune the models, you can install the package without the finetune dependency:
pip install  .
# If you want to finetune the models, install the package with the finetune dependency:
# pip install  .[finetune]
```
For development in editable mode:
```
# If you do not need to finetune the models, you can install the package without the finetune dependency:
pip install -e .
# If you want to finetune the models, install the package with the finetune dependency:
# pip install -e .[finetune]
```

## Quick Start
First, load one of the BGE embedding model:
```
from FlagEmbedding import FlagAutoModel

model = FlagAutoModel.from_finetuned('BAAI/bge-base-en-v1.5',
                                      query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                                      use_fp16=True)
```
Then, feed some sentences to the model and get their embeddings:
```
sentences_1 = ["I love NLP", "I love machine learning"]
sentences_2 = ["I love BGE", "I love text retrieval"]
embeddings_1 = model.encode(sentences_1)
embeddings_2 = model.encode(sentences_2)
```
Once we get the embeddings, we can compute similarity by inner product:
```
similarity = embeddings_1 @ embeddings_2.T
print(similarity)
```

For more details, you can refer to [embedder inference](./examples/inference/embedder), [reranker inference](./examples/inference/reranker), [embedder finetune](./examples/finetune/embedder), [reranker fintune](./examples/finetune/reranker), [evaluation](./examples/evaluation).

If you're unfamiliar with any of related concepts, please check out the [tutorial](./Tutorials/). If it's not there, let us know.

For more interesting topics related to BGE, take a look at [research](./research).

## Community

We are actively maintaining the community of BGE and FlagEmbedding. Let us know if you have any suggessions or ideas!

Currently we are updating the [tutorials](./Tutorials/), we aim to create a comprehensive and detailed tutorial for beginners on text retrieval and RAG. Stay tuned!

The following contents are releasing in the upcoming weeks:

- Evaluation
- BGE-EN-ICL

<details>
  <summary>The whole tutorial roadmap</summary>
    <img src="./Tutorials/tutorial_map.png"/>
</details>

## Model List

`bge` is short for `BAAI general embedding`.

| Model                                                                     | Language |                                                             Description                                                             |                                query instruction for retrieval                                 |
|:--------------------------------------------------------------------------|:--------:|:-----------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|
| [BAAI/bge-en-icl](https://huggingface.co/BAAI/bge-en-icl) | English | A LLM-based embedding model with in-context learning capabilities, which can fully leverage the model's potential based on a few shot examples | Provide instructions and few-shot examples freely based on the given task. |
| [BAAI/bge-multilingual-gemma2](https://huggingface.co/BAAI/bge-multilingual-gemma2) |    Multilingual     | A LLM-based multilingual embedding model, trained on a diverse range of languages and tasks. |        Provide instructions based on the given task.         |
| [BAAI/bge-m3](https:
