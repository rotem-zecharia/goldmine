# SigNoz/signoz

SigNoz is an open-source, OpenTelemetry-native observability platform for your team and their AI agents. Get logs, metrics, and traces in one tool with features like APM, distributed tracing, log mana

## features

1. **OpenTelemetry-native**<br>
   Instrument once with open standards and keep ownership of your telemetry.
2. **Correlated signals**<br>
   Move from service charts to traces, logs, infra metrics, and exceptions without switching tools.
3. **Single columnar database**<br>
   Built for high-cardinality, high-volume observability workloads.
4. **Predictable pricing**<br>
   No per-host pricing, no user-seat pricing, and no special pricing for custom metrics.
5. **Enterprise ready**<br>
   SOC 2 Type II and HIPAA compliance, RBAC, ingestion controls, custom retention, support, BYOC, and self-hosting.

## installation

#### Start on Cloud

Create a managed SigNoz workspace and get your first dashboard without running observability infrastructure.

[**Start free on SigNoz Cloud**](https://signoz.io/teams/)

#### Self-host SigNoz

Run SigNoz in your own infrastructure with Foundry, Docker, Kubernetes, or Linux.

[**Foundry**](https://github.com/SigNoz/foundry) · [**Docker**](https://signoz.io/docs/install/docker/) · [**Kubernetes**](https://signoz.io/docs/install/kubernetes/) · [**Linux**](https://signoz.io/docs/install/linux/)

#### Send data

Instrument applications and infrastructure with OpenTelemetry, Prometheus, language SDKs, and integrations.

[**Instrumentation**](https://signoz.io/docs/instrumentation/) · [**Integrations**](https://signoz.io/docs/integrations/integrations-list/)

## tools

SigNoz is often adopted by teams moving from a stack of single-purpose tools or commercial platforms with unpredictable pricing.

**Prometheus**<br>
Good if you just need metrics. SigNoz keeps metrics, logs, traces, dashboards, and alerts together so teams can debug with correlated context.

**Jaeger**<br>
Jaeger only does distributed tracing. SigNoz adds metrics, logs, trace analytics, dashboards, alerts, exceptions, and trace-to-log workflows.

**Elastic**<br>
SigNoz uses columnar database for efficient observability analytics and high-cardinality log workloads, with 50% lower resource requirement compared to Elastic during ingestion. Check the [detailed study](https://signoz.io/blog/logs-performance-benchmark/?utm_source=github-readme&utm_medium=logs-benchmark).

**Loki**<br>
In the linked benchmark, SigNoz indexed all keys in the test setup, while Loki hit max stream errors when more labels were added. Check the [detailed study](https://signoz.io/blog/logs-performance-benchmark/?utm_source=github-readme&utm_medium=logs-benchmark).

## Contributing

We ❤️ contributions big or small. Please read [CONTRIBUTING.md](CONTRIBUTING.md) to get started with making contributions to SigNoz.

Not sure how to get started? **Just ping us on `#contributing` in our [slack community](https://signoz.io/slack).**

As always, thanks to our amazing contributors!

<a href="https://github.com/signoz/signoz/graphs/contributors">
  <img alt="SigNoz contributors" src="https://contrib.rocks/image?repo=signoz/signoz" />
</a>
