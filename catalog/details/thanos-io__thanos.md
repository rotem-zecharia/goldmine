# thanos-io/thanos

Highly available Prometheus setup with long term storage capabilities. A CNCF Incubating project.

## features

Thanos is a set of components that can be composed into a highly available metric system with unlimited storage capacity, which can be added seamlessly on top of existing Prometheus deployments.

Thanos is a [CNCF](https://www.cncf.io/) Incubating project.

Thanos leverages the Prometheus 2.0 storage format to cost-efficiently store historical metric data in any object storage while retaining fast query latencies. Additionally, it provides a global query view across all Prometheus installations and can merge data from Prometheus HA pairs on the fly.

Concretely the aims of the project are:

1. Global query view of metrics.
2. Unlimited retention of metrics.
3. High availability of components, including Prometheus.

## installation

* **[Getting Started](https://thanos.io/tip/thanos/getting-started.md/)**
* [Design](https://thanos.io/tip/thanos/design.md/)
* [Blog posts](docs/getting-started.md#blog-posts)
* [Talks](docs/getting-started.md#talks)
* [Proposals](docs/proposals-done)
* [Integrations](docs/integrations.md)
