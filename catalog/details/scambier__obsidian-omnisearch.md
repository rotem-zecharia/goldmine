# scambier/obsidian-omnisearch

A search engine that "just works" for Obsidian. Supports OCR and PDF indexing.

## installation

- Omnisearch is available on [the official Community Plugins repository](https://obsidian.md/plugins?search=Omnisearch).
- Beta releases can be installed through [BRAT](https://github.com/TfTHacker/obsidian42-brat). **Be advised that those
  versions can be buggy and break things.**

You can check the [CHANGELOG](./CHANGELOG.md) for more information on the different versions.

## features

> Omnisearch's first goal is to _locate_ files instantly. You can see it as a _Quick Switcher_ on steroids.

- Find your **📝notes, 📄Office documents, 📄PDFs, and 🖼images** faster than ever
  - Images, documents, and PDF indexing is available
    through [Text Extractor](https://github.com/scambier/obsidian-text-extractor)
- Automatic document scoring using
  the [BM25 algorithm](https://github.com/lucaong/minisearch/issues/129#issuecomment-1046257399)
  - The relevance of a document against a query depends on the number of times the query terms appear in the document,
    its filename, and its headings
- Keyboard first: you never have to use your mouse
- Workflow similar to the "Quick Switcher" core plugin
- Opt-in local HTTP server to query Omnisearch from outside of Obsidian
- Resistance to typos
- Switch between Vault and In-file search to quickly skim multiple results in a single note
- Supports `"expressions in quotes"` and `-exclusions`
- Filters file types with `.jpg` or `.md`
- Directly Insert a `[[link]]` from the search results
- Supports Vim navigation keys

**Note:** support of Chinese depends
on [this additional plugin](https://github.com/aidenlx/cm-chs-patch) (also you may need to clear search cache data to apply new Chinese index). Please read its documentation for more
information.
