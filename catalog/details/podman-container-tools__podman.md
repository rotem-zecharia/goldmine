# podman-container-tools/podman

Podman: A tool for managing OCI containers and pods.

## features

At a high level, the scope of Podman and libpod is the following:

* Support for multiple container image formats, including OCI and Docker images.
* Full management of those images, including pulling from various sources (including trust and verification), creating (built via Containerfile or Dockerfile or committed from a container), and pushing to registries and other storage backends.
* Full management of container lifecycle, including creation (both from an image and from an exploded root filesystem), running, checkpointing and restoring (via CRIU), and removal.
* Full management of container networking, using Netavark.
* Support for pods, groups of containers that share resources and are managed together.
* Support for running containers and pods without root or other elevated privileges.
* Resource isolation of containers and pods.
* Support for a Docker-compatible CLI interface, which can both run containers locally and on remote systems.
* No manager daemon, for improved security and lower resource utilization at idle.
* Support for a REST API providing both a Docker-compatible interface and an improved interface exposing advanced Podman functionality.
* Support for running on Windows and Mac via virtual machines run by `podman machine`.

## limitations

The future of Podman feature development can be found in its **[roadmap](ROADMAP.md)**.
