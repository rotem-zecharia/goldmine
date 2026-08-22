# xerj-org/xerj

XERJ is the new way for AI to search data. Its autoindex capability activates agents to know your data without the token waste of grep and sed. One command indexes code, docs, logs and PDFs for search

## installation

```sh
curl -fsSL https://xerj.org/get | sh
```

Windows PowerShell:

```powershell
irm https://xerj.org/get.ps1 | iex
```

One static binary, no JVM, no dependencies. Prebuilt for Linux, macOS and Windows on x86-64
and arm64. You can also [build from source](#build-from-source). It speaks the Elasticsearch
API, so existing clients, dashboards and tooling work against it unchanged.

First commands after install (the installer prints where `xerj` landed; add it to your PATH
if needed): `xerj --insecure --data-dir ./data &`, wait until `http://localhost:9200`
responds, then `xerj autoindex ~/my-project`. See [Index a folder](#index-a-folder).

For a host with no runtime internet access, follow the
[air-gapped deployment recipe](./docs/recipes/air-gapped-deployment.md). The default lexical
embedder is offline; neural mode needs the three model files staged locally before the first
semantic operation.

## features

Agents burn their context window reading files. The PHP in WordPress core is about 5.2
million tokens, or 26 full context windows, so an agent cannot simply read it. Grep does not
solve this either, because a grep hit is a line, and judging that line means opening the
whole file.

Querying an index costs kilobytes per question instead. In
[an AI security audit of WordPress core](https://xerj.org/use-cases/code-security-audit.html),
an agent worked across 1,492 PHP files on roughly 26,000 tokens, which is what it takes to
load about half a percent of the tree.
