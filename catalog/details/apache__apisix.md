# apache/apisix

The Cloud-Native API Gateway and AI Gateway

## limitations

#
-->

## tools

<img src="./logos/apisix-white-bg.jpg" alt="APISIX logo" height="150px" align="right" />

[![Build Status](https://github.com/apache/apisix/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/apache/apisix/actions/workflows/build.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/apache/apisix/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/apache/apisix?color=blue)](https://github.com/apache/apisix/releases)
[![GitHub stars](https://img.shields.io/github/stars/apache/apisix?style=flat&color=blue)](https://github.com/apache/apisix/stargazers)
[![Docker Pulls](https://img.shields.io/docker/pulls/apache/apisix?color=blue)](https://hub.docker.com/r/apache/apisix)
[![Commit activity](https://img.shields.io/github/commit-activity/m/apache/apisix)](https://github.com/apache/apisix/graphs/commit-activity)
[![GitHub issues](https://img.shields.io/github/issues/apache/apisix)](https://github.com/apache/apisix/issues)
[![Slack](https://badgen.net/badge/Slack/Join%20Apache%20APISIX?icon=slack)](https://apisix.apache.org/slack)

**Apache APISIX** is a dynamic, real-time, high-performance API Gateway.

APISIX API Gateway provides rich traffic management features such as load balancing, dynamic upstream, canary release, circuit breaking, authentication, observability, and more. You can use it to handle traditional north-south traffic, as well as east-west traffic between services. It can also be used as a [Kubernetes ingress controller](https://github.com/apache/apisix-ingress-controller).

## Table of Contents

- [Why APISIX](#why-apisix)
- [AI Gateway](#ai-gateway)
- [Get Started](#get-started)
- [Features](#features)
- [Benchmark](#benchmark)
- [Community](#community)
- [User Stories](#user-stories)
- [Who Uses APISIX API Gateway?](#who-uses-apisix-api-gateway)
- [Logos](#logos)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## features

APISIX is built on top of NGINX and etcd. Compared with traditional API gateways, APISIX has dynamic routing and hot-loading of plugins, which is especially suitable for API management under a microservice architecture.

The technical architecture of Apache APISIX:

![Technical architecture of Apache APISIX](docs/assets/images/apisix.png)

## AI Gateway

APISIX can serve as an **[AI Gateway](https://apisix.apache.org/ai-gateway/)** through its flexible plugin system, providing:

- **AI proxying** to route traffic to different LLM providers through a unified interface.
- **Load balancing, retries, and fallbacks** across multiple LLMs to ensure the efficiency and reliability of AI agents.
- **Token-based rate limiting** to control cost and protect upstream models.
- **Robust security** for authentication, authorization, and traffic control on AI workloads.

APISIX also provides the [`mcp-bridge`](https://apisix.apache.org/blog/2025/04/21/host-mcp-server-with-api-gateway/) plugin to seamlessly convert stdio-based MCP servers to scalable HTTP SSE services.

## Get Started

Install and run APISIX with a single command using the quickstart script (requires [Docker](https://docs.docker.com/get-docker/)):

```shell
curl -sL https://run.api7.ai/apisix/quickstart | sh
```

This starts APISIX (listening on port `9080`) together with its etcd configuration store. Verify it is running:

```shell
curl "http://127.0.0.1:9080" --head | grep Server
```

Create your first route via the Admin API (port `9180`) to proxy requests to an upstream service:

```shell
curl -i "http://127.0.0.1:9180/apisix/admin/routes/1" -X PUT -d '
{
  "uri": "/get",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

Send a request through APISIX to confirm the route works:

```shell
curl "http://127.0.0.1:9080/get"
```

To learn more, follow the [Getting Started](https://apisix.apache.org/docs/apisix/getting-started/) guide and the [installation documentation](https://apisix.apache.org/docs/apisix/installation-guide/) for other deployment methods. To extend APISIX, see the [plugin development guide](docs/en/latest/plugin-develop.md), the [plugin concept](docs/en/latest/terminology/plugin.md), and the [REST Admin API](docs/en/latest/admin-api.md) reference.

For more documents, please refer to the [Apache APISIX Documentation site](https://apisix.apache.org/docs/apisix/getting-started/).

## Features

You can use APISIX API Gateway as a traffic entrance to process all business data, including dynamic routing, dynamic upstream, dynamic certificates,
A/B testing, canary release, blue-green deployment, limit rate, defense against malicious attacks, metrics, monitoring alarms, service observability, service governance, etc.

- **All platforms**

  - Cloud-Native: Platform agnostic, No vendor lock-in, APISIX API Gateway can run from bare-metal to Kubernetes.
  - Supports ARM64: Don't worry about the lock-in of the infra technology.

- **Multi protocols**

  - [TCP/UDP Proxy](docs/en/latest/stream-proxy.md): Dynamic TCP/UDP proxy.
  - [Dubbo Proxy](docs/en/latest/plugins/dubbo-proxy.md): Dynamic HTTP to Dubbo proxy.
  - [Dynamic MQTT Proxy](docs/en/latest/plugins/mqtt-proxy.md): Supports to load balance MQTT by `client_id`, both support MQTT [3.1.\*](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html), [5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html).
  - [gRPC proxy](docs/en/latest/grpc-proxy.md): Proxying gRPC traffic.
  - [gRPC Web Proxy](docs/en/latest/plugins/grpc-web.md): Proxying gRPC Web traffic to gRPC Service.
  - [gRPC transcoding](docs/en/latest/plugins/grpc-transcode.md): Supports protocol transcoding so that clients can access your gRPC API by using HTTP/JSON.
  - Proxy Websocket
  - Proxy Protocol
  - HTTP(S) Forward Proxy
  - [SSL](docs/en/latest/certificate.md): Dynamically load an SSL certificate
  - [HTTP/3 with QUIC](docs/en/latest/http3.md)

- **Full Dynamic**

  - [Hot Up
