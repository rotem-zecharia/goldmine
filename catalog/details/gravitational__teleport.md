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
