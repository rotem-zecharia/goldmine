# Shopify/toxiproxy

:alarm_clock: :fire: A TCP proxy to simulate network and system conditions for chaos and resiliency testing

## features

The existing ones we found didn't provide the kind of dynamic API we needed for
integration and unit testing. Linux tools like `nc` and so on are not
cross-platform and require root, which makes them problematic in test,
development and CI environments.

## tools

Configuring a project to use Toxiproxy consists of three steps:

1. Installing Toxiproxy
2. Populating Toxiproxy
3. Using Toxiproxy

## installation

**Linux**

See [`Releases`](https://github.com/Shopify/toxiproxy/releases) for the latest
binaries and system packages for your architecture.

**Ubuntu**

```bash
$ wget -O toxiproxy-2.1.4.deb https://github.com/Shopify/toxiproxy/releases/download/v2.1.4/toxiproxy_2.1.4_amd64.deb
$ sudo dpkg -i toxiproxy-2.1.4.deb
$ sudo service toxiproxy start
```

**OS X**

With [Homebrew](https://brew.sh/):

```bash
$ brew tap shopify/shopify
$ brew install toxiproxy
```

Or with [MacPorts](https://www.macports.org/):

```bash
$ port install toxiproxy
```

**Windows**

Toxiproxy for Windows is available for download at https://github.com/Shopify/toxiproxy/releases/download/v2.1.4/toxiproxy-server-windows-amd64.exe

**Docker**

Toxiproxy is available on [Github container registry](https://github.com/Shopify/toxiproxy/pkgs/container/toxiproxy).
Old versions `<= 2.1.4` are available on on [Docker Hub](https://hub.docker.com/r/shopify/toxiproxy/).

```bash
$ docker pull ghcr.io/shopify/toxiproxy
$ docker run --rm -it ghcr.io/shopify/toxiproxy
```

If using Toxiproxy from the host rather than other containers, enable host networking with `--net=host`.

```shell
$ docker run --rm --entrypoint="/toxiproxy-cli" -it ghcr.io/shopify/toxiproxy list
```

**Source**

If you have Go installed, you can build Toxiproxy from source using the make file:
```bash
$ make build
$ ./toxiproxy-server
```

#### Upgrading from Toxiproxy 1.x

In Toxiproxy 2.0 several changes were made to the API that make it incompatible with version 1.x.
In order to use version 2.x of the Toxiproxy server, you will need to make sure your client
library supports the same version. You can check which version of Toxiproxy you are running by
looking at the `/version` endpoint.

See the documentation for your client library for specific library changes. Detailed changes
for the Toxiproxy server can been found in [CHANGELOG.md](./CHANGELOG.md).
