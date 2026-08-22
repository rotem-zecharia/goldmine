# gravitational/teleport

The easiest, and most secure way to access and protect all of your infrastructure.

## features

While working together at Rackspace, the creators of Teleport noticed that
most cloud users struggle with setting up and configuring infrastructure
security. Many popular tools designed for this are complex to understand and
expensive to maintain across modern, distributed computing infrastructure.

We decided to build a solution that's easy to use, understand, and scale. A
real-time representation of all your servers in the same room as you, as if
they were magically **teleported**. And thus, Teleport was born! 

Today, Teleport is trusted by everyone from hobbyists to hyperscalers to
simplify security across cloud CLIs and consoles, Kubernetes clusters, SSH
servers, databases, internal web apps, and Model Context Protocol (MCP) used
by AI agents.

[Learn more about Teleport and our history](https://goteleport.com/about/)

## Supporting and Contributing

We aim to make Teleport easy to adopt and contribute to, starting with clear and comprehensive [documentation](https://goteleport.com/docs/). 

If you have questions, are exploring ideas, or want to sanity-check something, please start with a GitHub Discussion. Discussions help us answer questions, explore use cases, and decide together whether something should become a bug report or feature request.

- Start a conversation in [Teleport Discussions](https://github.com/gravitational/teleport/discussions)  
  This is the best place to ask questions, share ideas, and get help. Our engineers actively participate there, and discussions can be promoted to issues when there is a clear, actionable next step.

- Issues are for confirmed bugs and well-defined feature requests  
  If something has already been validated as a bug or an enhancement, feel free to open an issue. When in doubt, start a discussion and we will help guide it.

- Enterprise and POC support  
  If you are evaluating Teleport Enterprise or need more responsive support during a POC, we can set up a dedicated Slack channel. You can [reach out to us through our website](https://goteleport.com/contact-sales/) to get started.

## installation

To set up a single-instance Teleport cluster, follow our [getting started
guide](https://goteleport.com/docs/admin-guides/deploy-a-cluster/linux-demo/).
You can then register your servers, Kubernetes clusters, and other
infrastructure with your Teleport cluster.

You can also get started with Teleport Enterprise Cloud, a managed Teleport
deployment that makes it easier to enable secure access to your
infrastructure.

[Sign up for a free trial](https://goteleport.com/signup/) of Teleport
Enterprise Cloud, and follow this guide to [register your first
server](https://goteleport.com/docs/get-started/).

## Docker

### Deploy Teleport

If you wish to deploy Teleport inside a Docker container see the
[installation guide](https://goteleport.com/docs/installation/docker/#running-teleport-on-docker).

### For Local Testing and Development

To run a full test suite locally, see [the test dependencies
list](BUILD_macos.md#local-tests-dependencies)

## Building Teleport

The `teleport` repository contains the Teleport daemon binary (written in Go)
and a web UI written in TypeScript.

If your intention is to build and deploy for use in a production infrastructure
a released tag should be used.  The default branch, `master`, is the current
development branch for an upcoming major version.  Get the latest release tags
listed at https://goteleport.com/download/ and then use that tag in the `git
clone`. For example `git clone
https://github.com/gravitational/teleport.git -b v18.5.0` gets release
v18.5.0.

### Dockerized Build

It is often easiest to build with Docker, which ensures that all required
tooling is available for the build. To execute a dockerized build, ensure
that docker is installed and running, and execute:

```
make -C build.assets build-binaries
```

This command will build Linux binaries matching the host architecture.
It is not possible to cross-compile to a different target architecture.

### Local Build

#### Dependencies

The following dependencies are required to build Teleport from source. For
maximum compatibility, install the versions of these dependencies using the
versions listed in [`build.assets/versions.mk`](/build.assets/versions.mk):

1. [`Go`](https://golang.org/dl/)
1. [`Rust`](https://www.rust-lang.org/tools/install)
1. [`Node.js`](https://nodejs.org/en/download/)
1. [`libfido2`](https://github.com/Yubico/libfido2)
1. [`pkg-config`](https://www.freedesktop.org/wiki/Software/pkg-config/)

For an example of dev environment setup on macOS, see [these
instructions](/BUILD_macos.md).

#### Perform a build

>**Important**
>
>* The Go compiler is somewhat sensitive to the amount of memory: you will
   need **at least** 1GB of virtual memory to compile Teleport. A 512MB
   instance without swap will **not** work.
>* This will build the latest version of Teleport. 

Get the source

```shell
git clone https://github.com/gravitational/teleport.git
cd teleport
```

To perform a build

```shell
make full
```

`tsh` dynamically links against libfido2 by default, to support development
environments, as long as the library itself can be found:

```shell
$ brew install libfido2 pkg-config  # Replace with your package manager of choice

$ make build/tsh
> libfido2 found, setting FIDO2=dynamic
> (...)
```

Release binaries are linked statically against libfido2. You may switch the
linking mode using the FIDO2 variable:

```shell
make build/tsh FIDO2=dynamic # dynamic linking
make build/tsh FIDO2=static  # static linking, for an easy setup use `make enter`
                             # or `build.assets/macos/build-fido2-macos.sh`.
make build/tsh FIDO2=off     # doesn't link libfido2 in any way
```

`tsh` builds with Touch ID support require access to an Apple Developer
account. If you are a Teleport maintainer, ask the team for access.

#### Build output and run locally

If the build succeeds, the installer will place the binaries in the `build`
directory.

Before starting, create default data directories:

```shell
sudo mkdi

## requirements

All dependencies are managed using [Go
modules](https://blog.golang.org/using-go-modules). Here are the
instructions for some common tasks:

#### Add a new dependency

Latest version:

```bash
go get github.com/new/dependency
```

and update the source to use this dependency.


To get a specific version, use `go get
github.com/new/dependency@version` instead.

#### Set dependency to a specific version

```bash
go get github.com/new/dependency@version
```

#### Update dependency to the latest version

```bash
go get -u github.com/new/dependency
```

#### Update all dependencies

```bash
go get -u all
```

#### Debugging dependencies

Why is a specific package imported?

`go mod why $pkgname`

Why is a specific module imported?

`go mod why -m $modname`

Why is a specific version of a module imported?

`go mod graph | grep $modname`

## License

Teleport is distributed in multiple forms with different licensing
implications.

The Teleport API module (all code in this repository under `/api`) is
available under the [Apache 2.0 license](./api/LICENSE).

The remainder of the source code in this repository is available under the
[GNU Affero General Public License](./LICENSE). Users compiling Teleport
from source must comply with the terms of this license.

Teleport Community Edition builds distributed on
http://goteleport.com/download are available under a [modified Apache 2.0
license](./build.assets/LICENSE-community).

## FAQ

### Is Teleport production-ready?

Yes, Teleport is production-ready and used to protect and facilitate
access to the most precious and mission-critical applications at many of
today's leading companies. You can learn more about the companies using
Teleport in production [on our website](https://goteleport.com/case-study/).

### Is Teleport secure?

Yes, Teleport has completed several security audits from nationally and
internationally recognized technology security companies. We publicize
audit results, our security philosophy, and related information on our
[trust page](https://trust.goteleport.com/).

### What resources does Teleport support?

Teleport secures access to a [broad set of infrastructure
resources](https://goteleport.com/docs/enroll-resources), including Linux
servers, Windows desktops, Kubernetes clusters, databases, internal web
applications, cloud provider APIs and consoles (such as AWS, Azure, and
GCP), and Model Context Protocol (MCP) servers used by AI agents.

### How is Teleport deployed?

Teleport can be [deployed to fit most
environments](https://goteleport.com/docs/feature-matrix/#platform-integrations-management-licensing-and-deployment),
either as a self-hosted cluster on Linux or Kubernetes or using Teleport
Enterprise Cloud. In all cases, Teleport agents run close to your
resources and connect through an Auth Service and Proxy Service that
enforces identity, access control, and audit.

### Is Teleport an identity provider (IdP)?

Teleport uses existing IdPs (Okta, Google Workspace, Microsoft Entra ID,
or GitHub) to issue short-lived certificates and apply access policies.
Teleport can also be [configured to act as a SAML
IdP](https://goteleport.com/docs/identity-governance/idps/) to authenticate
users into applications when needed.

### Does Teleport require credential handling or secrets management?

Teleport eliminates long-lived passwords, SSH keys, database credentials,
credential rotations, and vault processes by issuing [short-lived,
auto-expiring mTLS and SSH
certificates](https://goteleport.com/docs/reference/architecture/authentication/#short-lived-certificates)
bound to human or non-human identity.

### Is Teleport a Privileged Access Management (PAM) solution?

Teleport provides modern PAM software capabilities like strong
authentication, session recording, policy-based access, and JIT elevation
without secrets, credential rotation, or vault dependencies. This enables
controlled, audited access to servers, Kubernetes, databases, cloud
consoles, and other privileged e
