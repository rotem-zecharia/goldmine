# grafana/pyroscope

Continuous Profiling Platform. Debug performance issues down to a single line of code

## installation

### Docker
```sh
docker run -it -p 4040:4040 grafana/pyroscope
```

### Homebrew (macOS / Linux)
```sh
brew install pyroscope-io/brew/pyroscope
brew services start pyroscope
```

### Binary
Download the archive for your operating system and architecture from the [latest release](https://github.com/grafana/pyroscope/releases/latest), unpack it, and run the binary:
```sh
tar xvf pyroscope_*.tar.gz
./pyroscope
```

Pyroscope listens on port `4040`. For Kubernetes/Helm, Linux packages, building from source, and full configuration options, see the [Get started guide](https://grafana.com/docs/pyroscope/latest/get-started/) and the [server documentation](https://grafana.com/docs/pyroscope/latest/configure-server/).

## **Quick Start: Visualize profiles with Grafana Profiles Drilldown**

<img width="1728" alt="image" src="https://github.com/user-attachments/assets/67691443-6450-45b9-8064-f41056c88ade">

[Grafana Profiles Drilldown](https://grafana.com/docs/grafana/latest/visualizations/simplified-exploration/profiles/) (formerly Explore Profiles) is the primary, queryless way to visualize and analyze your profiling data.

### Grafana Cloud / OSS
Profiles Drilldown is pre-installed and is the default way to explore your profiles – all you need to do is start sending data.

## Documentation

For more information on how to use Pyroscope with other programming languages, install it on Linux, or use it in a production environment, check out our documentation:

* [Getting Started](https://grafana.com/docs/pyroscope/latest/get-started/)
* [Deployment Guide](https://grafana.com/docs/pyroscope/latest/deploy-kubernetes/)
* [Pyroscope v2 Architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/)

## Send data to the server

You can send profiles to Pyroscope with the language SDKs, with [Grafana Alloy](https://grafana.com/docs/pyroscope/latest/configure-client/grafana-alloy/), or over OTLP from OpenTelemetry-compatible sources such as the [OpenTelemetry eBPF profiler](https://grafana.com/docs/pyroscope/latest/configure-client/opentelemetry/ebpf-profiler/).

For more documentation on how to add the Pyroscope SDK to your code, see the [client documentation](https://grafana.com/docs/pyroscope/latest/configure-client/) on our website or find language-specific examples and documentation below:
<table>
   <tr>
      <td align="center"><a href="https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/go_push/"><img src="https://user-images.githubusercontent.com/23323466/178160549-2d69a325-56ec-4e19-bca7-d460d400b163.png" width="100px;" alt=""/><br />
        <b>Golang</b></a><br />
          <a href="https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/go_push/" title="Documentation">Documentation</a><br />
          <a href="https://github.com/grafana/pyroscope/tree/main/examples/language-sdk-instrumentation/golang-push" title="golang-examples">Examples</a>
      </td>
      <td align="center"><a href="https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/java/"><img src="https://user-images.githubusercontent.com/23323466/178160550-2b5a623a-0f4c-4911-923f-2c825784d45d.png" width="100px;" alt=""/><br />
        <b>Java</b></a><br />
          <a href="https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/java/" title="Documentation">Documentation</a><br />
          <a href="https://github.com/grafana/pyroscope/tree/main/examples/language-sdk-instrumentation/java/rideshare" title="java-examples">Examples</a>
      </td>
      <td align="center"><a href="https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/python/"><img src="https://user-images.githubusercontent.com/23323466/178160553-c78b8c15-99b4-43f3-a2a0-252b6c4862b1.png" width="100px;" alt=""/><br />
        <b>Python</b></a><br />
          <a href="https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/python/" title="Documentation">Documentation</a><b
