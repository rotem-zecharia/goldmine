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

## Communications

If you think you've identified a security issue in the project, please *DO NOT* report the issue publicly via the GitHub issue tracker, mailing list, or IRC.
Instead, send an email with as many details as possible to `security@lists.podman.io`. This is a private mailing list for the core maintainers.

For general questions and discussion, please use Podman's
[channels](https://podman.io/community/#slack-irc-matrix-and-discord).

For discussions around issues/bugs and features, you can use the GitHub
[issues](https://github.com/containers/podman/issues)
and
[PRs](https://github.com/containers/podman/pulls)
tracking system.

There is also a [mailing list](https://lists.podman.io/archives/) at `lists.podman.io`.
You can subscribe by sending a message to `podman-join@lists.podman.io` with the subject `subscribe`.

### Community Meetings

All Podman meetings are open to everyone, free to attend, and hosted via Zoom through the CNCF/Linux Foundation.
The full calendar is available on the [Podman Container Tools LFX Meetings page](https://zoom-lfx.platform.linuxfoundation.org/meetings/podman-container-tools?view=month).
Registering for a meeting sends you an invite for that meeting and all subsequent recurring instances.

| Meeting | Schedule | Format |
|---------|----------|--------|
| [Podman Community Meeting](https://zoom-lfx.platform.linuxfoundation.org/meeting/97486138230?password=3144ae43-0fd5-457e-a495-bb4e0202e9c2) and its [agenda](https://hackmd.io/fc1zraYdS0-klJ2KJcfC7w?both) | First **Tuesday of even-numbered months** (Feb, Apr, Jun, Aug, Oct, Dec) at **11:00 a.m. Eastern** (UTC-4 summer / UTC-5 winter) | ~1 hour — demos, announcements, and community updates |
| [Podman Monday Office Hours](https://zoom-lfx.platform.linuxfoundation.org/meeting/92776077694?password=deea5903-07a5-4e4d-9ad9-a6f52319fabe) and its [agenda](https://hackmd.io/@TomSweeneyRedHat/H1qIC9nkMe) | Every **Monday at 10:00 a.m. Eastern** (UTC-4 summer / UTC-5 winter) | 30 min — technical discussions, open topics |
| [Podman Thursday Office Hours](https://zoom-lfx.platform.linuxfoundation.org/meeting/96031375483?password=97015335-907e-4f54-9eff-b3068d7052c9) and its [agenda](https://hackmd.io/@TomSweeneyRedHat/H1qIC9nkMe) | Every **Thursday at 11:00 a.m. Eastern** (UTC-4 summer / UTC-5 winter) | 30 min — technical discussions, open topics |

## Rootless
Podman can be easily run as a normal user, without requiring a setuid binary.
When run without root, Podman containers use user namespaces to set root in the container to the user running Podman.
Rootless Podman runs locked-down containers with no privileges that the user running the container does not have.
Some of these restrictions can be lifted (via `--privileged`, for example), but rootless containers will never have more privileges than the user that launched them.
If you run Podman as your user and mount in `/etc/passwd` from the host, you still won't be able to change it, since your user doesn't have permission to do so.

Almost all normal Podman functionality is available, though there are some [shortcomings](https://github.com/containers/podman/blob/main/rootless.md).
Any recent Podman release should be able to run rootless without any additional configuration, though your operating system may require some additional configuration detailed in the [install guide](https://podman.io/getting-started/installation).

A little configuration by an administrator is required before rootless Podman can be used, the necessary setup is documented [here](https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md).

## Podman Desktop

[Podman Desktop](https://podman-desktop.io/) provides a local development environment for Podman and Kubernetes on Linux, Windows, and Mac machines.
It is a full-featured desktop UI frontend for Podman which uses the `podman machine` backend on non-Li
