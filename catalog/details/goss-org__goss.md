# goss-org/goss

Quick and Easy server testing/validation

## features

* Goss is EASY! - [Goss in 45 seconds](#goss-in-45-seconds)
* Goss is FAST! - small-medium test suites are near instantaneous, see [benchmarks](https://github.com/goss-org/goss/wiki/Benchmarks)
* Goss is SMALL! - <10MB single self-contained binary

## installation

**Note:** For macOS and Windows, see: [platform-feature-parity].

This will install goss and [dgoss](https://github.com/goss-org/goss/tree/master/extras/dgoss).

**Note:** Using `curl | sh` is not recommended for production systems, use manual installation below.

```bash
# Install latest version to /usr/local/bin
curl -fsSL https://goss.rocks/install | sh

# Install v0.4.10 version to ~/bin
curl -fsSL https://goss.rocks/install | GOSS_VER=v0.4.10 GOSS_DST=~/bin sh
```

<!-- --8<-- [end:intro] -->
<!-- --8<-- [start:install] -->

### Manual installation

!!! warning

    If you're using goss in a CI pipeline, it's recommended that you don't
    download the `latest` and instead use a specific release tag. Using the
    latest release may lead to unexpected behaviour.

#### Specific Version

```bash
# See https://github.com/goss-org/goss/releases for release versions
VERSION=v0.4.10
curl -L "https://github.com/goss-org/goss/releases/download/${VERSION}/goss_${VERSION#v}_linux_x86_64.tar.gz" | tar xz -C /usr/local/bin goss
chmod +rx /usr/local/bin/goss

# (optional) dgoss docker wrapper (use 'master' for latest version)
VERSION=v0.4.10
curl -L "https://github.com/goss-org/goss/releases/download/${VERSION}/dgoss" -o /usr/local/bin/dgoss
chmod +rx /usr/local/bin/dgoss
```

### Build it yourself

```bash
make build
```

Alternatively, you can build it with [goreleaser](https://goreleaser.com/). To
build a binary, use `gorelease build`, and to only build for the same OS and
architecture as the machine you're building on, include the `--single-target`
flag. The `--clean` flag will clean up any existing builds, and `--snapshot`
will allow you to build against something other than a tag.

Here's an example:

```console
$ goreleaser build --clean --single-target --snapshot
  • skipping validate...
  • cleaning distribution directory
  • loading environment variables
  • getting and validating git state
    • ignoring errors because this is a snapshot     error=git doesn't contain any tags - either add a tag or use --snapshot
    • using tags                                     previous=<unknown> current=v0.0.0
    • pipe skipped or partially skipped              reason=disabled during snapshot mode
  • parsing tag
  • setting defaults
  • partial
  • snapshotting
    • building snapshot...                           version=0.0.1-next
  • running before hooks
    • running                                        hook=go mod tidy
  • ensuring distribution directory
  • setting up metadata
  • writing release metadata
  • loading go mod information
  • build prerequisites
  • building binaries
    • partial build                                  match=target=linux_arm64_v8.0
    • building                                       paths=cmd/goss binaries=goss target=linux_arm64_v8.0
      • took: 31s
  • writing artifacts metadata
  • build succeeded after 31s
  • thanks for using GoReleaser!
$ tree dist
dist
├── artifacts.json
├── binaries_linux_arm64_v8.0
│   └── goss                            <- your binary
├── config.yaml
└── metadata.json

2 directories, 4 files
```

<!-- --8<-- [end:install] -->

## Full Documentation

[Full Documentation](https://goss.readthedocs.io/en/stable/)

## Using the container image

[Using the Goss container image](https://goss.readthedocs.io/en/stable/container_image/)

## Quick start

<!-- --8<-- [start:quickstart] -->

### Writing a simple sshd test

An initial set of tests can be derived from the system state by using the [add](https://goss.readthedocs.io/en/stable/cli/#add)
or [autoadd](https://goss.readthedocs.io/en/stable/cli/#autoadd) commands.

Let's write a simple sshd test using autoadd.

```txt
# Running it as root will allow it to also detect ports
$ sudo goss autoadd sshd
```

Generated `goss.yaml`:

```yaml
port:
  tcp:22:
    listening: true
    ip:
    - 0.0.0.0
  tcp6:22:
    listening: true
    ip:
    - '::'
service:
  sshd:
    enabled: true
    running: true
user:
  sshd:
    exists: true


## limitations

`goss` works well on Linux, but support on Windows & macOS is alpha. See [platform-feature-parity].

The following tests have limitations.

Package:

* rpm
* deb
* Alpine apk
* pacman

Service:

* systemd
* sysV init
* OpenRC init
* Upstart

[kubernetes-simplified-health-checks]: https://medium.com/@aelsabbahy/docker-1-12-kubernetes-simplified-health-checks-and-container-ordering-with-goss-fa8debbe676c
[platform-feature-parity]: https://goss.readthedocs.io/en/stable/platforms/

<!-- --8<-- [end:about] -->
