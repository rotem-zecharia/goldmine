# vectordotdev/vector

A high-performance observability data pipeline.

## features

Vector is an end-to-end, unified, open data platform.

|                     | **Vector** | Beats | Fluentbit | Fluentd | Logstash | Splunk UF | Splunk HF | Telegraf |
| ------------------- | ---------- | ----- | --------- | ------- | -------- | --------- | --------- | -------- |
| **End-to-end**      | **✓**      |       |           |         |          |           |           | ✓        |
| Agent               | **✓**      | ✓     | ✓         |         |          | ✓         |           | ✓        |
| Aggregator          | **✓**      |       |           | ✓       | ✓        |           | ✓         | ✓        |
| **Unified**         | **✓**      |       |           |         |          |           |           | ✓        |
| Logs                | **✓**      | ✓     | ✓         | ✓       | ✓        | ✓         | ✓         | ✓        |
| Metrics             | **✓**      | ⚠     | ⚠         | ⚠       | ⚠        | ⚠         | ⚠         | ✓        |
| Traces              | 🚧         |       |           |         |          |           |           |          |
| **Open**            | **✓**      |       | ✓         | ✓       |          |           |           | ✓        |
| Open-source         | **✓**      | ✓     | ✓         | ✓       | ✓        |           |           | ✓        |
| Vendor-neutral      | **✓**      |       | ✓         | ✓       |          |           |           | ✓        |
| **Reliability**     | **✓**      |       |           |         |          |           |           |          |
| Memory-safe         | **✓**      |       |           |         |          |           |           | ✓        |
| Delivery guarantees | **✓**      |       |           |         |          | ✓         | ✓         |          |
| Multi-core          | **✓**      | ✓     | ✓         | ✓       | ✓        | ✓         | ✓         | ✓        |


⚠ = Not interoperable, metrics are represented as structured logs

---

<p align="center">
  Developed with ❤️ by <strong><a href="https://datadoghq.com">Datadog</a></strong> - <a href="https://github.com/vectordotdev/vector/security/policy">Security Policy</a> - <a href="https://github.com/vectordotdev/vector/blob/master/PRIVACY.md">Privacy Policy</a>
</p>

[docs.about.concepts]: https://vector.dev/docs/introduction/concepts/
[docs.about.introduction]: https://vector.dev/docs/introduction/
[docs.administration.monitoring]: https://vector.dev/docs/administration/monitoring/
[docs.administration.management]: https://vector.dev/docs/administration/management/
[docs.administration.upgrading]: https://vector.dev/docs/administration/upgrading/
[docs.administration.validating]: https://vector.dev/docs/administration/validating/
[docs.architecture.concurrency-model]: https://vector.dev/docs/architecture/concurrency-model/
[docs.architecture.data-model]: https://vector.dev/docs/architecture/data-model/
[docs.architecture.pipeline-model]: https://vector.dev/docs/architecture/pipeline-model/
[docs.architecture.runtime-model]: https://vector.dev/docs/architecture/runtime-model/
[docs.configuration.sinks]: https://vector.dev/docs/reference/configuration/sinks/
[docs.configuration.sources]: https://vector.dev/docs/reference/configuration/sources/
[docs.configuration.tests]: https://vector.dev/docs/reference/configuration/tests/
[docs.configuration.transforms]: https://vector.dev/docs/reference/configuration/transforms/
[docs.configuration.enrichment_tables]: https://vector.dev/docs/reference/configuration/global-options/#enrichment_tables
[docs.data-model.log]: https://vector.dev/docs/architecture/data-model/log/
[docs.data-model.metric]: https://vector.dev/docs/architecture/data-model/metric/
[docs.deployment.roles]: https://vector.dev/docs/setup/deployment/roles/
[docs.deployment.topologies]: https://vector.dev/docs/setup/deployment/topologies/
[docs.deployment]: https://vector.dev/docs/setup/deployment/
[docs.installation.manual]: https://vector.dev/docs/setup/installation/manual/
[docs.installation.operating
