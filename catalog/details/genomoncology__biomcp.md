# genomoncology/biomcp

BioMCP: Biomedical Model Context Protocol

## features

- **Search the literature:** `search article` fans out across PubTator3 and
  Europe PMC, deduplicates PMID/PMCID/DOI identifiers, and can add a Semantic
  Scholar leg when your filters support it.
- **Pivot without rework:** move from a gene, variant, drug, disease, pathway,
  protein, or article straight into the next built-in view instead of
  rebuilding filters by hand.
- **Choose a playbook:** `biomcp skill list` shows shipped worked examples
  so you can open the matching `biomcp skill <slug>` workflow.
- **Analyze studies locally:** `study` commands cover local query, cohort, survival,
  compare, and co-occurrence workflows with native terminal, SVG, and PNG
  charts for downloaded cBioPortal-style datasets.
- **Follow the paper trail:** `article citations`, `article references`,
  `article recommendations`, and `article entities` turn one known paper into a
  broader evidence map.
- **Enrich and batch:** use `biomcp enrich` for top-level g:Profiler
  enrichment and `biomcp batch` for up to 10 focused `get` calls in one
  command.

## installation

First useful query in under 30 seconds:

```bash
uv tool install biomcp-cli
biomcp health --apis-only
biomcp skill list
biomcp list gene
biomcp search all --gene BRAF --disease melanoma  # unified cross-entity discovery
biomcp get gene BRAF pathways hpa
```

## tools

Most commands work without credentials. Optional keys improve rate limits or
unlock optional enrichments:

```bash
export NCBI_API_KEY="..."        # PubTator, PubMed/efetch, PMC OA, NCBI ID converter
export S2_API_KEY="..."          # Optional Semantic Scholar auth; dedicated quota at 1 req/sec
export OPENFDA_API_KEY="..."     # OpenFDA rate limits
export NCI_API_KEY="..."         # NCI CTS trial search (--source nci)
export ONCOKB_TOKEN="..."        # OncoKB variant helper
export ALPHAGENOME_API_KEY="..." # AlphaGenome variant effect prediction
```

`search article`, `get article`, `article batch`, `get article ... tldr`, and
the explicit Semantic Scholar helpers all work without `S2_API_KEY`. With the
key, BioMCP sends authenticated requests and uses a dedicated rate limit at
1 req/sec. Without it, BioMCP uses the shared unauthenticated pool at 1 req/2sec.
`search article --source` supports `all`, `pubtator`, `europepmc`, `pubmed`,
`semanticscholar`, and `litsense2`. The default compatible article federation
uses PubTator3, Europe PMC, PubMed, and automatic Semantic Scholar; use
`--source semanticscholar` or `--source litsense2` explicitly when you want one
of those sources alone. Explicit source selection also disables cross-provider
row enrichment. References
and recommendations can be empty for paywalled papers because of publisher
elision in Semantic Scholar upstream coverage.
