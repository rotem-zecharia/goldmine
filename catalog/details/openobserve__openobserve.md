# openobserve/openobserve

Open source observability platform for logs, metrics, traces, frontend monitoring, pipelines and LLM observability. A sophisticated, simple and highly performant alternative to Datadog, Splunk, and El

## features

A single platform for all of your observability signals. Here's why teams choose OpenObserve:

| Benefit | Description |
| --- | --- |
| **140x lower storage cost** | Parquet columnar storage + S3-native architecture dramatically reduce costs vs Elasticsearch |
| **Single binary deployment** | Up and running in under 2 minutes — no complex cluster setup required |
| **OpenTelemetry native** | Built on the OpenTelemetry standard — no vendor lock-in |
| **Unified platform** | Logs, metrics, traces, RUM, dashboards, alerts, and incidents in one tool |
| **High performance** | Better query performance than Elasticsearch on a quarter of the hardware |
| **SQL + PromQL** | Query logs and traces with SQL, metrics with SQL or PromQL — no proprietary query language |
| **Built in Rust** | Memory-safe, high-performance, single binary |

**Cost comparison: OpenObserve vs Elasticsearch**

![OpenObserve vs Elasticsearch storage cost comparison](./screenshots/zo_vs_es.png)

## installation

### OpenObserve Cloud (fastest way)

Get started in minutes without managing infrastructure. The free tier includes up to 50 GB/day of ingestion.

**[Get Started Free →](https://cloud.openobserve.ai/)**

### 🐳 Docker

```bash
docker run -d \
      --name openobserve \
      -v $PWD/data:/data \
      -p 5080:5080 \
      -e ZO_ROOT_USER_EMAIL="root@example.com" \
      -e ZO_ROOT_USER_PASSWORD="Complexpass#123" \
      public.ecr.aws/zinclabs/openobserve:latest
```

Then open [http://localhost:5080](http://localhost:5080) and log in with the credentials above.

For other installation methods, see the [quickstart documentation](https://openobserve.ai/docs/quickstart). For clustered deployments, see the [High Availability deployment guide](https://openobserve.ai/docs/ha_deployment/).

## Product Tour

OpenObserve ships with a powerful, unified web UI for every signal — logs, traces, metrics, dashboards, RUM, alerts, incidents, pipelines, and AI observability.

[![Watch the OpenObserve introduction video](./screenshots/o2_intro.webp)](https://www.youtube.com/watch?v=4VwuC1tpRP4)

## limitations

All data in OpenObserve is **immutable** — once ingested, it cannot be modified or deleted (only entire retention periods can be dropped). This is by design and is a feature for logs and compliance use cases, ensuring data integrity and audit trails.

### Is this production-ready?

Yes. OpenObserve runs in production across thousands of deployments worldwide, including environments processing in excess of 2 PB/day. See our [customer stories](https://openobserve.ai/customer-stories/) for real-world examples.

### How does query performance compare to Elasticsearch?

OpenObserve delivers better performance than Elasticsearch for most workloads, with faster search and significantly faster analytics — while using about a quarter of the hardware. The columnar Parquet format is particularly effective for complex aggregations and analytics.

### Is there a steep learning curve?

No. OpenObserve is designed to be intuitive from day one:

- **Familiar query languages** — SQL for logs and traces, PromQL for metrics; no proprietary query language to learn
- **Easy-to-use GUI** — an intuitive interface with a drag-and-drop dashboard builder
- **No complex tuning** — unlike Elasticsearch, there are no shards, replicas, or heap sizes to manage. Just install and go.

Most users are productive within hours, not weeks.

## License

**Open Source Edition** — licensed under [AGPL-3.0](https://github.com/openobserve/openobserve/blob/main/LICENSE). We chose AGPL to ensure that improvements to OpenObserve remain open source and benefit the entire community, while still allowing free commercial use. [Why AGPL, and why it's good for the community →](https://openobserve.ai/blog/what-are-apache-gpl-and-agpl-licenses-and-why-openobserve-moved-from-apache-to-agpl/)

**Enterprise Edition** — licensed under a commercial Enterprise License Agreement (not AGPL), which provides additional flexibility for enterprise deployments.

## SBOM

Software Bill of Materials for OpenObserve. You can analyze either SBOM with [Dependency-Track](https://dependencytrack.org/).

### Rust

The SBOM is available [here](./openobserve.cdx.xml). To regenerate it:

```bash
cargo install cargo-cyclonedx
cargo-cyclonedx cyclonedx
```

### JavaScript

The SBOM is available [here](./web/sbom.json). To regenerate it:

```bash
npm install --global @cyclonedx/cyclonedx-npm
cd web
cyclonedx-npm > sbom.json
```
