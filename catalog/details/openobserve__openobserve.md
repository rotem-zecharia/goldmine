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

## limitations

All data in OpenObserve is **immutable** — once ingested, it cannot be modified or deleted (only entire retention periods can be dropped). This is by design and is a feature for logs and compliance use cases, ensuring data integrity and audit trails.
