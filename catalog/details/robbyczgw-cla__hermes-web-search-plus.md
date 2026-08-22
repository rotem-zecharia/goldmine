# robbyczgw-cla/hermes-web-search-plus

Give your Hermes agent the web as real sources, never a made-up answer — multi-provider search and extraction with an optional local, key-free DonSeTch option.

## features

- **One setup, many search services.** Pick one provider to start and add more only when you need them.
- **Real sources.** Results point back to the pages they came from instead of hiding the web behind a generated answer.
- **Fewer dead ends.** If one service is unavailable or returns nothing, Web Search Plus can try another.
- **Search and page reading together.** Find useful pages, then turn them into clean text for your agent.
- **Optional details when you need them.** Quality reports show which service worked and what happened along the way.
- **Local options are available.** SearXNG, Keenable and the optional DonSeTch provider can reduce your dependence on paid APIs.

Everything new since 3.0 is additive or opt-in, except the v4.0 provider migration described above. Full details: [4.0 Release Notes](docs/RELEASE_NOTES_V400.md) · [3.4 Release Notes](docs/RELEASE_NOTES_V34.md) · [3.3 Release Notes](docs/RELEASE_NOTES_V33.md) · [3.2 Release Notes](docs/RELEASE_NOTES_V32.md) · [3.1 Release Notes](docs/RELEASE_NOTES_V31.md) · [3.0 Release Notes](docs/RELEASE_NOTES_V3.md).

---

## installation

```bash
# 1) Install and enable the plugin
hermes plugins install robbyczgw-cla/hermes-web-search-plus --enable

## configuration

python3 ~/.hermes/plugins/web-search-plus/setup.py status
python3 ~/.hermes/plugins/web-search-plus/setup.py setup --preset starter

## tools

# CLI: exit and start `hermes` again, or use /reset in-session
# Gateway: /restart, then /reset

# 4) Optional shell smoke test
cd ~/.hermes/plugins/web-search-plus
python3 search.py --query "Hermes Agent latest release" --provider auto --quality-report
```

Web Search Plus supports 15 search and 9 extraction providers — you do **not** need them all. One search-capable key or configured local endpoint enables `web_search_plus`; one extraction-capable key or endpoint enables `web_extract_plus`; more providers just make controlled routing more flexible. The setup helper stores keys in the active Hermes environment file — never commit them to the repository.

Provider privacy is not uniform. Before sending sensitive queries or URLs, review the maintained [Provider Privacy & Terms guide](https://websearchplus.xyz/providers.html#privacy-terms), which distinguishes standard self-serve terms from enterprise-only ZDR or no-training options.

### Upgrading to 4.0.0

The core tools and existing keyed providers remain available, but the optional Hound integration was removed. If you used Hound, follow the [DonSeTch migration guide](docs/DONSETCH.md#migration-from-hound): install DonSeTch 2.3.1 separately, set `DONSETCH_BIN`, and change explicit `provider="hound"` calls to `provider="donsetch"`.

### Self-hosted / no-paid-key profile

For a privacy- and budget-oriented setup with no commercial API key, use the self-hosted wizard preset:

```bash
python3 ~/.hermes/plugins/web-search-plus/setup.py setup --preset self-hosted
python3 ~/.hermes/plugins/web-search-plus/setup.py status
```

It selects the derived `self_hosted` profile: automatic search uses only your SearXNG instance and keyless Keenable, while automatic extraction runs through Keenable's public fetch tier (SearXNG does not extract; the public tier is rate-limited and has no SLA). Configure SearXNG with `searxng.base_url` (the older `instance_url` still works); the preset enables Keenable's existing public tier without writing a key. See the [Self-hosted profile guide](docs/USER_GUIDE.md#self-hosted-profile) for prerequisites and explicit-provider behavior.

### Optional Octen source search via Monid

Set `MONID_API_KEY` from [Monid](https://app.monid.ai/access/api-keys) to use [Octen](https://octen.ai) as an explicit source-search provider:

```python
web_search_plus(query="recent vector database research", provider="octen", freshness="month")
```

The adapter executes Octen's `/search` endpoint through Monid's documented HTTP API for ranked links and highlights. It supports freshness and domain filters, explicitly disables full-content retrieval, and does not call Octen's answer or Broad Search APIs. Access and billing use Monid's prepaid wallet; see Monid for current pricing and terms. Octen stays outside automatic routing and fallback unless you deliberately enable `auto_allow`.

### Optional TinyFish source search

Set `TINYFISH_API_KEY` from your own [TinyFish account](https://agent.tinyfish.ai/api-keys) to use its direct Search API explicitly. Web Search Plus does not provide, pool, proxy, or share TinyFish credentials.

```python
web_search_plus(query="recent agent framework releases", provider="tinyfish", freshness="week")
```

The adapter calls only TinyFish's fixed source-search endpoint and returns ranked links and snippets. It never sends the optional `purpose` or `fetch` parameters and does not call TinyFish Agent or Browser APIs. Domain filters and result hosts are accepted only as ASCII/Punycode hostnames; raw Unicode hostnames are rejected fail-closed. TinyFish remains outside automatic routing and fallback: its [standard Terms](https://www.tinyfish.ai/terms) permit Customer Data to be used for model training and fine-tuning, and its [Privacy Policy](https://www.tinyfish.ai/privacy-policy) does not provide a fixed deletion period. Treat the integration as high risk unless your contract supplies stronger terms; see the [provider/privacy matrix](https://websearchp
