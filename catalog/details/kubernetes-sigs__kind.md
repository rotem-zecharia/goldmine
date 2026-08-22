# kubernetes-sigs/kind

Kubernetes IN Docker - local clusters for testing Kubernetes

## installation

kind is a tool for running local Kubernetes clusters using Docker container "nodes".
kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

If you have [go] and [docker], [podman] or [nerdctl] installed `go install sigs.k8s.io/kind@v0.32.0 && kind create cluster` is all you need!

![](site/static/images/kind-create-cluster.png)

kind consists of:
- Go [packages][packages] implementing [cluster creation][cluster package], [image build][build package], etc.
- A command line interface ([`kind`][kind cli]) built on these packages.
- Docker [image(s)][images] written to run systemd, Kubernetes, etc.
- [`kubetest`][kubetest] integration also built on these packages (WIP)

kind bootstraps each "node" with [kubeadm][kubeadm]. For more details see [the design documentation][design doc].

**NOTE**: kind is still a work in progress, see the [1.0 roadmap].

## features

- kind supports multi-node (including HA) clusters
- kind supports building Kubernetes release builds from source
  - support for make / bash or docker, in addition to pre-published builds
- kind supports Linux, macOS and Windows
- kind is a [CNCF certified conformant Kubernetes installer](https://landscape.cncf.io/?selected=kind)
