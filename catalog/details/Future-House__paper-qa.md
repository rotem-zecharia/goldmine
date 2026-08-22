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
