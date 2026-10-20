# meilisearch/meilisearch

A lightning-fast search engine API bringing AI-powered hybrid search to your sites and applications.

## installation

### 1. Get a Meilisearch instance

**Option A: Meilisearch Cloud (recommended).** No install. [Start a 14-day trial](https://cloud.meilisearch.com/register?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), then create a project and pick a region. Your project URL and API keys are on the project settings page.

**Option B: Self-host.** Run the open-source engine locally with Docker:

```sh
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:latest
```

Prefer a binary? Run:
```sh
curl -L https://install.meilisearch.com | sh
./meilisearch
```

More options: [install Meilisearch locally](https://www.meilisearch.com/docs/resources/self_hosting/getting_started/install_locally?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start).

### 2. Add documents

```sh
curl -X POST "https://ms-url-example.meilisearch.io/indexes/movies/documents" \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer apiKey" \
  --data-binary '[
    { "id": 1, "title": "Carol", "genres": ["Romance", "Drama"] },
    { "id": 2, "title": "Wonder Woman", "genres": ["Action", "Adventure"] },
    { "id": 3, "title": "Life of Pi", "genres": ["Adventure", "Drama"] }
  ]'
```

### 3. Search, typo included

```sh
curl -X POST "https://ms-url-example.meilisearch.io/indexes/movies/search" \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer apiKey" \
  --data-binary '{ "q": "wondre woman" }'
```

Meilisearch returns *Wonder Woman* despite the typo. Indexing is asynchronous, so if the search comes back empty, wait a moment and retry.

Next steps: follow a 5-minute quick start for [JavaScript](https://www.meilisearch.com/docs/getting_started/sdks/javascript?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), [Python](https://www.meilisearch.com/docs/getting_started/sdks/python?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), [PHP](https://www.meilisearch.com/docs/getting_started/sdks/php?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), [Ruby](https://www.meilisearch.com/docs/getting_started/sdks/ruby?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), [Go](https://www.meilisearch.com/docs/getting_started/sdks/go?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), [Rust](https://www.meilisearch.com/docs/getting_started/sdks/rust?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), or [React](https://www.meilisearch.com/docs/getting_started/instant_meilisearch/react?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start), or follow the [Cloud getting started guide](https://www.meilisearch.com/docs/getting_started/first_project?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=quick-start).

## features

- **Hybrid search:** Combine the best of both [semantic](https://www.meilisearch.com/docs/learn/experimental/vector_search?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features) & full-text search to get the most relevant results
- **Search-as-you-type:** Find & display results in less than 50 milliseconds to provide an intuitive experience
- **[Typo tolerance](https://www.meilisearch.com/docs/learn/relevancy/typo_tolerance_settings?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** get relevant matches even when queries contain typos and misspellings
- **[Filtering](https://www.meilisearch.com/docs/learn/fine_tuning_results/filtering?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features) and [faceted search](https://www.meilisearch.com/docs/learn/fine_tuning_results/faceted_search?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** enhance your users' search experience with custom filters and build a faceted search interface in a few lines of code
- **[Sorting](https://www.meilisearch.com/docs/learn/fine_tuning_results/sorting?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** sort results based on price, date, or pretty much anything else your users need
- **[Synonym support](https://www.meilisearch.com/docs/learn/relevancy/synonyms?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** configure synonyms to include more relevant content in your search results
- **[Geosearch](https://www.meilisearch.com/docs/learn/fine_tuning_results/geosearch?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** filter and sort documents based on geographic data
- **[Extensive language support](https://www.meilisearch.com/docs/learn/what_is_meilisearch/language?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** search datasets in any language, with optimized support for Chinese, Japanese, Hebrew, and languages using the Latin alphabet
- **[Security management](https://www.meilisearch.com/docs/learn/security/master_api_keys?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** control which users can access what data with API keys that allow fine-grained permissions handling
- **[Multi-Tenancy](https://www.meilisearch.com/docs/learn/security/multitenancy_tenant_tokens?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** personalize search results for any number of application tenants
- **Highly Customizable:** customize Meilisearch to your specific needs or use our out-of-the-box and hassle-free presets
- **[RESTful API](https://www.meilisearch.com/docs/reference/api/overview?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** integrate Meilisearch in your technical stack with our plugins and SDKs
- **[Conversational search](https://www.meilisearch.com/docs/capabilities/conversational_search/overview?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** let users ask questions in natural language and get AI-generated answers grounded in your search results
- **[Personalization](https://www.meilisearch.com/docs/capabilities/personalization/overview?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** tailor search results to individual users based on their preferences and behavior
- **[Search rules](https://www.meilisearch.com/docs/capabilities/search_rules/overview?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** define custom rules to dynamically adjust search behavior based on context
- **[Document relations](https://www.meilisearch.com/docs/capabilities/indexing/how_to/document_relations?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=features):** link documents across indexes to enrich search results with r

## tools

- [**Media**](https://where2watch.meilisearch.com/?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) — Search movies and streaming platforms to watch them using [hybrid search](https://www.meilisearch.com/solutions/hybrid-search?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos).
- [**Agentic search**](https://what2watch.meilisearch.com/?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) — Chat with an AI agent to recommend movies and streaming platforms.
- [**Flickr**](https://flickr.meilisearch.com/?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) — Search and explore one hundred million Flickr images with semantic search.
- [**Ecommerce**](https://ecommerce.meilisearch.com/?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) — Ecommerce website using disjunctive [facets](https://www.meilisearch.com/docs/learn/fine_tuning_results/faceted_search?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos), range and rating filtering, and pagination.
- [**Home Booking**](https://www.meilisearch.com/docs/resources/demos/home_booking?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) - A conversational search demo for finding holiday rentals using natural language.
- [**Search Playground**](https://www.meilisearch.com/docs/resources/demos/playground?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) — An interactive playground to explore Meilisearch search features.
- [**Personalization**](https://www.meilisearch.com/docs/resources/demos/personalized_search?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) — A demo showcasing personalized search results tailored to individual users.
- [**SaaS**](https://saas.meilisearch.com/?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) — Search for contacts, deals, and companies in this [multi-tenant](https://www.meilisearch.com/docs/learn/security/multitenancy_tenant_tokens?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos) CRM application.

See the list of all our [interactive demos](https://www.meilisearch.com/docs/resources/demos/overview?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=demos).

## 🧰 SDKs & integration tools

Install one of our SDKs in your project for seamless integration between Meilisearch and your favorite language or framework!

Take a look at the complete [Meilisearch integration list](https://www.meilisearch.com/docs/learn/what_is_meilisearch/sdks?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=sdks-link).

[![Logos belonging to different languages and frameworks supported by Meilisearch, including React, Ruby on Rails, Go, Rust, and PHP](assets/integrations.png)](https://www.meilisearch.com/docs/learn/what_is_meilisearch/sdks?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=sdks-logos)

## 🤖 AI & LLM integrations

- **[MCP server](https://www.meilisearch.com/docs/getting_started/integrations/mcp?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=ai):** Meilisearch ships a native MCP server at the `/mcp` route (experimental), so AI agents and MCP clients can search your indexes directly. It works the same on Meilisearch Cloud and self-hosted instances.
- **[LangChain](https://www.meilisearch.com/docs/getting_started/integrations/langchain?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=ai):** use Meilisearch as a LangChain vector store.
- **[Conversational search](https://www.meilisearch.com/docs/capabilities/conversational_search/overview?utm_campaign=oss&utm_source=github&utm_medium=meilisearch&utm_content=ai):** answer natural-language questions with responses grounded in your indexed data.
- **[llms.txt](https://www.meilisearch.com/docs/llms.txt):** a machine-readable index of the 
