# containerd/containerd

An open and reliable container runtime

## installation

See our documentation on [containerd.io](https://containerd.io):
* [for ops and admins](docs/ops.md)
* [namespaces](docs/namespaces.md)
* [client options](docs/client-opts.md)

To get started contributing to containerd, see [CONTRIBUTING](CONTRIBUTING.md).

If you are interested in trying out containerd see our example at [Getting Started](docs/getting-started.md).

## requirements

Runtime requirements for containerd are very minimal. Most interactions with
the Linux and Windows container feature sets are handled via [runc](https://github.com/opencontainers/runc) and/or
OS-specific libraries (e.g. [hcsshim](https://github.com/Microsoft/hcsshim) for Microsoft).
The current required version of `runc` is described in [RUNC.md](docs/RUNC.md).

There are specific features
used by containerd core code and snapshotters that will require a minimum kernel
version on Linux. With the understood caveat of distro kernel versioning, a
reasonable starting point for Linux is a minimum 4.x kernel version.

The overlay filesystem snapshotter, used by default, uses features that were
finalized in the 4.x kernel series. If you choose to use btrfs, there may
be more flexibility in kernel version (minimum recommended is 3.18), but will
require the btrfs kernel module and btrfs tools to be installed on your Linux
distribution.

To use Linux checkpoint and restore features, you will need `criu` installed on
your system. See more details in [Checkpoint and Restore](#checkpoint-and-restore).

Build requirements for developers are listed in [BUILDING](BUILDING.md).

## features

For a detailed overview of containerd's core concepts and the features it supports,
please refer to the [FEATURES.MD](./docs/features.md) document.

## tools

Please see [RELEASES.md](RELEASES.md) for details on versioning and stability
of containerd components.

Downloadable 64-bit Intel/AMD binaries of all official releases are available on
our [releases page](https://github.com/containerd/containerd/releases). Binaries
are published for additional platforms as well; see
[Platform Support](RELEASES.md#platform-support) for the full list of platforms
and the level of support for each.

For other architectures and distribution support, you will find that many
Linux distributions package their own containerd and provide it across several
architectures, such as [Canonical's Ubuntu packaging](https://launchpad.net/ubuntu/bionic/+package/containerd).

#### Enabling command auto-completion

Starting with containerd 1.4, the urfave client feature for auto-creation of bash and zsh
autocompletion data is enabled. To use the autocomplete feature in a bash shell for example, source
the autocomplete/ctr file in your `.bashrc`, or manually like:

```
$ source ./contrib/autocomplete/ctr
```

#### Distribution of `ctr` autocomplete for bash and zsh

For bash, copy the `contrib/autocomplete/ctr` script into
`/etc/bash_completion.d/` and rename it to `ctr`. The `zsh_autocomplete`
file is also available and can be used similarly for zsh users.

Provide documentation to users to `source` this file into their shell if
you don't place the autocomplete file in a location where it is automatically
loaded for the user's shell environment.
