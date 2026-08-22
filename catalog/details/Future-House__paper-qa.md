# Future-House/paper-qa

High accuracy RAG for answering questions from scientific documents with citations

## installation

In this example we take a folder of research paper PDFs,
magically get their metadata - including citation counts with a retraction check,
then parse and cache PDFs into a full-text search index,
and finally answer the user question with an LLM agent.

```bash
pip install paper-qa
mkdir my_papers
curl -o my_papers/PaperQA2.pdf https://arxiv.org/pdf/2409.13740
cd my_papers
pqa ask 'What is PaperQA2?'
```

### Example Output

Question: Has anyone designed neural networks that compute with proteins or DNA?

> The claim that neural networks have been designed to compute with DNA is supported by multiple sources.
> The work by Qian, Winfree, and Bruck demonstrates the use of DNA strand displacement cascades
> to construct neural network components, such as artificial neurons and associative memories,
> using a DNA-based system (Qian2011Neural pages 1-2, Qian2011Neural pages 15-16, Qian2011Neural pages 54-56).
> This research includes the implementation of a 3-bit XOR gate and a four-neuron Hopfield associative memory,
> showcasing the potential of DNA for neural network computation.
> Additionally, the application of deep learning techniques to genomics,
> which involves computing with DNA sequences, is well-documented.
> Studies have applied convolutional neural networks (CNNs) to predict genomic features such as
> transcription factor binding and DNA accessibility (Eraslan2019Deep pages 4-5, Eraslan2019Deep pages 5-6).
> These models leverage DNA sequences as input data,
> effectively using neural networks to compute with DNA.
> While the provided excerpts do not explicitly mention protein-based neural network computation,
> they do highlight the use of neural networks in tasks related to protein sequences,
> such as predicting DNA-protein binding (Zeng2016Convolutional pages 1-2).
> However, the primary focus remains on DNA-based computation.

## What is PaperQA2

PaperQA2 is engineered to be the best agentic RAG model for working with scientific papers.
Here are some features:

- A simple interface to get good answers with grounded responses containing in-text citations.
- State-of-the-art implementation including document metadata-awareness
  in embeddings and LLM-based re-ranking and contextual summarization (RCS).
- Support for agentic RAG, where a language agent can iteratively refine queries and answers.
- Automatic redundant fetching of paper metadata,
  including citation and journal quality data from multiple providers.
- A usable full-text search engine for a local repository of PDF/text files.
- A robust interface for customization, with default support for all [LiteLLM][LiteLLM providers] models.

[LiteLLM providers]: https://docs.litellm.ai/docs/providers
[LiteLLM general docs]: https://docs.litellm.ai/docs/

By default, it uses [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings)
and [models](https://platform.openai.com/docs/models) with a Numpy vector DB to embed and search documents.
However, you can easily use other closed-source, open-source models or embeddings (see details below).

PaperQA2 depends on some awesome libraries/APIs that make our repo possible.
Here are some in no particular order:

1. [Semantic Scholar](https://www.semanticscholar.org/)
2. [Crossref](https://www.crossref.org/)
3. [Unpaywall](https://unpaywall.org/)
4. [Pydantic](https://docs.pydantic.dev/latest/)
5. [tantivy](https://github.com/quickwit-oss/tantivy)
6. [LiteLLM][LiteLLM general docs]
7. [pybtex](https://pybtex.org/)

### PaperQA2 vs PaperQA

We've been working hard on fundamental upgrades for a while
and mostly followed [SemVer](https://semver.org/), until [December 2025](#paperqa2-goes-calver-in-december-2025).
Meaning we've incremented the major version number on each breaking change.
This brings us to the current major version number v5.
So why call is the repo now called PaperQA2?
We wanted to remark on the fact though that we've
exceeded human performance on [many important metrics](https://paper.wikicrow

## tools

The fastest way to test PaperQA2 is via the CLI. First navigate to a directory with some papers and use the `pqa` cli:

```bash
pqa ask 'What is PaperQA2?'
```

You will see PaperQA2 index your local PDF files,
gathering the necessary metadata for each of them
(using [Crossref](https://www.crossref.org/) and [Semantic Scholar](https://www.semanticscholar.org/)),
search over that index, then break the files into chunked evidence contexts,
rank them, and ultimately generate an answer.
The next time this directory is queried,
your index will already be built (save for any differences detected, like new added papers),
so it will skip the indexing and chunking steps.

All prior answers will be indexed and stored,
you can view them by querying via the `search` subcommand,
or access them yourself in your `PQA_HOME` directory,
which defaults to `~/.pqa/`.

```bash
pqa -i 'answers' search 'ranking and contextual summarization'
```

PaperQA2 is highly configurable, when running from the command line,
`pqa --help` shows all options and short descriptions.
For example to run with a higher temperature:

```bash
pqa --temperature 0.5 ask 'What is PaperQA2?'
```

You can view all settings with `pqa view`.
Another useful thing is to change to other templated settings - for example
`fast` is a setting that answers more quickly
and you can see it with `pqa -s fast view`

Maybe you have some new settings you want to save? You can do that with

```bash
pqa -s my_new_settings --temperature 0.5 --llm foo-bar-5 save
```

and then you can use it with

```bash
pqa -s my_new_settings ask 'What is PaperQA2?'
```

If you run `pqa` with a command which requires a new indexing,
say if you change the default chunk_size,
a new index will automatically be created for you.

```bash
pqa --parsing.chunk_size 5000 ask 'What is PaperQA2?'
```

You can also use `pqa` to do full-text search with use of LLMs view the search command.
For example, let's save the index from a directory and give it a name:

```bash
pqa -i nanomaterials index
```

Now I can search for papers about thermoelectrics:

```bash
pqa -i nanomaterials search thermoelectrics
```

or I can use the normal ask

```bash
pqa -i nanomaterials ask 'Are there nm scale features in thermoelectric materials?'
```

Both the CLI and module have pre-configured settings based on prior performance and our publications,
they can be invoked as follows:

```bash
pqa --settings <setting name> \
    ask 'Are there nm scale features in thermoelectric materials?'
```

### Bundled Settings

Inside [`src/paperqa/configs`](src/paperqa/configs) we bundle known useful settings:

| Setting Name | Description                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| high_quality | Highly performant, relatively expensive (due to having `evidence_k` = 15) query using a `ToolSelector` agent.                |
| fast         | Setting to get answers cheaply and quickly.                                                                                  |
| wikicrow     | Setting to emulate the Wikipedia article writing used in our WikiCrow publication.                                           |
| contracrow   | Setting to find contradictions in papers, your query should be a claim that needs to be flagged as a contradiction (or not). |
| debug        | Setting useful solely for debugging, but not in any actual application beyond debugging.                                     |
| tier1_limits | Settings that match OpenAI rate limits for each tier, you can use `tier<1-5>_limits` to specify the tier.                    |

### Rate Limits

If you are hitting rate limits, say with the OpenAI Tier 1 plan, you can add them into PaperQA2.
For each OpenAI tier, a pre-built setting exists to limit usage.

```bash
pqa --settings 'tier1_limits' a
