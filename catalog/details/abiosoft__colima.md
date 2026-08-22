# abiosoft/colima

Container runtimes on macOS (and Linux) with minimal setup

## installation

[![Go](https://github.com/abiosoft/colima/actions/workflows/go.yml/badge.svg)](https://github.com/abiosoft/colima/actions/workflows/go.yml)
[![Integration](https://github.com/abiosoft/colima/actions/workflows/linux-integration.yml/badge.svg)](https://github.com/abiosoft/colima/actions/workflows/linux-integration.yml)
[![Integration](https://github.com/abiosoft/colima/actions/workflows/macos-integration.yml/badge.svg)](https://github.com/abiosoft/colima/actions/workflows/macos-integration.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/abiosoft/colima)](https://goreportcard.com/report/github.com/abiosoft/colima)

![Demonstration](colima.gif)

**Website & Documentation:** [colima.run](https://colima.run) | [colima.run/docs](https://colima.run/docs/)

## features

Support for Intel and Apple Silicon macOS, and Linux

- Simple CLI interface with sensible defaults
- Automatic Port Forwarding
- Volume mounts
- Multiple instances
- Support for multiple container runtimes
  - [Docker](https://docker.com) (with optional Kubernetes)
  - [Containerd](https://containerd.io) (with optional Kubernetes)
  - [Incus](https://linuxcontainers.org/incus) (containers and virtual machines)
- GPU accelerated containers for AI workloads

## tools

Start Colima with defaults

```
colima start
```

For more usage options

```
colima --help
colima start --help
```

Or use a config file

```
colima start --edit
```
