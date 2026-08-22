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

## features

APISIX is built on top of NGINX and etcd. Compared with traditional API gateways, APISIX has dynamic routing and hot-loading of plugins, which is especially suitable for API management under a microservice architecture.

The technical architecture of Apache APISIX:

![Technical architecture of Apache APISIX](docs/assets/images/apisix.png)
