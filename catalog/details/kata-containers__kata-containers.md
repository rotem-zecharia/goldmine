# kata-containers/kata-containers

Kata Containers is an open source project and community working to build a standard implementation of lightweight Virtual Machines (VMs) that feel and perform like containers, but provide the workload

## requirements

The [Kata Containers runtime](src/runtime) provides a command to
determine if your host system is capable of running and creating a
Kata Container:

```bash
$ kata-runtime check
```

> **Notes:**
>
> - This command runs a number of checks including connecting to the
>   network to determine if a newer release of Kata Containers is
>   available on GitHub. If you do not wish this to check to run, add
>   the `--no-network-checks` option.
>
> - By default, only a brief success / failure message is printed.
>   If more details are needed, the `--verbose` flag can be used to display the
>   list of all the checks performed.
>
> - If the command is run as the `root` user additional checks are
>   run (including checking if another incompatible hypervisor is running).
>   When running as `root`, network checks are automatically disabled.

## installation

New to Kata Containers? Start with the
[Quick Start Guide](docs/quick-start-guide.md) to learn the basics and run your
first workload, then see the [installation guide](docs/installation.md).

## configuration

Kata Containers uses a single
[configuration file](src/runtime/README.md#configuration)
which contains a number of sections for various parts of the Kata
Containers system including the [runtime](src/runtime), the
[agent](src/agent) and the [hypervisor](#hypervisors).
