# paradedb/paradedb

One Postgres for your application data, full-text search, vector retrieval, and aggregations. Home of the pg_search extension.

## installation

To install ParadeDB locally in a fresh Docker container and drop straight into a `psql` session:

```bash
curl -fsSL https://paradedb.com/install.sh | sh
```

When you're ready to deploy, check out our [hosting options](https://docs.paradedb.com/deploy/overview).

## What is ParadeDB?

[ParadeDB](https://paradedb.com) adds Elastic-quality full-text search, vector retrieval, and aggregations to Postgres with the `pg_search` extension. Your application data and your search engine live in one database, with no second system to deploy and nothing to sync.

Vectors are currently indexed using the [pgvector](https://github.com/pgvector/pgvector) extension, but native vector support is coming to our search index soon.

- [x] [Full-Text Search](https://docs.paradedb.com/documentation/full-text/overview)
  - [x] [BM25 Scoring](https://docs.paradedb.com/documentation/sorting/score)
  - [x] [Top K](https://docs.paradedb.com/documentation/sorting/topk)
  - [x] [Highlighting](https://docs.paradedb.com/documentation/full-text/highlight)
  - [x] [Tokenizers & Token Filters](https://docs.paradedb.com/documentation/tokenizers/overview)
- [x] [Filtering](https://docs.paradedb.com/documentation/filtering)
- [x] [Aggregates](https://docs.paradedb.com/documentation/aggregates/overview)
  - [x] [Columnar Storage](https://docs.paradedb.com/documentation/indexing/columnar)
  - [x] [Bucket & Metrics](https://docs.paradedb.com/documentation/aggregates/overview)
  - [x] [Facets](https://docs.paradedb.com/documentation/aggregates/facets)
- [x] [JOINs](https://docs.paradedb.com/documentation/joins/overview)
- [ ] Native Vector Search (coming soon)
- [ ] Native Hybrid Search (coming soon)

Star and watch this repository to follow along. See our [current projects](https://github.com/paradedb/paradedb/projects?query=is%3Aopen) and [long-term roadmap](https://docs.paradedb.com/welcome/roadmap).

## How It Works

ParadeDB integrates battle-tested Rust libraries for search and analytics inside Postgres, contributing upstream whenever possible. Our primary dependencies are:

- [pgrx](https://github.com/pgcentralfoundation/pgrx) — bridges Postgres and Rust
- [Tantivy](https://github.com/quickwit-oss/tantivy) — powers full-text search
- [Apache DataFusion](https://github.com/apache/datafusion) — handles OLAP processing

For a deeper dive, see our [architecture docs](https://docs.paradedb.com/welcome/architecture) or [CMU Database Group talk](https://db.cs.cmu.edu/events/building-blocks-paradedb-philippe-noel/).

## Integrations

ParadeDB integrates with the tools you already use, with more on the way.

### ORMs & Frameworks

- [Drizzle](https://github.com/paradedb/drizzle-paradedb)
- [Django](https://github.com/paradedb/django-paradedb)
- [SQLAlchemy](https://github.com/paradedb/sqlalchemy-paradedb)
- [Rails](https://github.com/paradedb/rails-paradedb)
- [EF Core](https://github.com/paradedb/efcore-paradedb)
- More coming (Prisma, and others)

### AI Agents

- [Agent Skills](https://github.com/paradedb/agent-skills)
- [MCP Integration](https://docs.paradedb.com/documentation/getting-started/ai-agents)
- [Cursor Plugin](https://cursor.com/marketplace/parade-db)

### PaaS & Cloud Platforms

- [Railway](https://docs.paradedb.com/deploy/cloud-platforms/railway)
- [Render](https://docs.paradedb.com/deploy/cloud-platforms/render)
- [DigitalOcean](https://docs.paradedb.com/deploy/cloud-platforms/digitalocean)
- [Fly.io](https://docs.paradedb.com/deploy/cloud-platforms/fly)
- [Dokku](https://docs.paradedb.com/deploy/cloud-platforms/dokku)
- More coming (Heroku, and others)

## Community & Support

- [Slack](https://paradedb.com/slack) — ask questions, share what you're building
- [GitHub Discussions](https://github.com/paradedb/paradedb/discussions) — longer-form Q&A
- [GitHub Issues](https://github.com/paradedb/paradedb/issues/new/choose) — bug reports and feature requests
- [Email](mailto:sales@paradedb.com) — enterprise support and commercial licensing

## Contributing
