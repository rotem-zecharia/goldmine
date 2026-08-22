# CrunchyData/postgres-operator

Production PostgreSQL for Kubernetes, from high availability Postgres clusters to full-scale database-as-a-service.

## installation

Crunchy Data makes PGO available as the orchestration behind Crunchy Postgres for Kubernetes. Crunchy Postgres for Kubernetes is the integrated product that includes PostgreSQL, PGO and a collection of PostgreSQL tools and extensions that includes the various [open source components listed in the documentation](https://access.crunchydata.com/documentation/postgres-operator/latest/references/components).

We recommend following our [Quickstart](https://access.crunchydata.com/documentation/postgres-operator/v5/quickstart/) for how to install and get up and running. However, if you can't wait to try it out, here are some instructions to get Postgres up and running on Kubernetes:

1. [Fork the Postgres Operator examples repository](https://github.com/CrunchyData/postgres-operator-examples/fork) and clone it to your host machine. For example:

```sh
YOUR_GITHUB_UN="<your GitHub username>"
git clone --depth 1 "git@github.com:${YOUR_GITHUB_UN}/postgres-operator-examples.git"
cd postgres-operator-examples
```

2. Run the following commands

```sh
kubectl apply -k kustomize/install/namespace
kubectl apply --server-side -k kustomize/install/default
```

For more information please read the [Quickstart](https://access.crunchydata.com/documentation/postgres-operator/v5/quickstart/) and [Tutorial](https://access.crunchydata.com/documentation/postgres-operator/v5/tutorials/).

These installation instructions provide the steps necessary to install PGO along with Crunchy Data's Postgres distribution, Crunchy Postgres, as Crunchy Postgres for Kubernetes. In doing so the installation downloads a series of container images from Crunchy Data's Developer Portal. For more information on the use of container images downloaded from the Crunchy Data Developer Portal or other third party sources, please see 'License and Terms' below. The installation and use of PGO outside of the use of Crunchy Postgres for Kubernetes will require modifications of these installation instructions and creation of the necessary PostgreSQL and related containers.  

# Cloud Native Postgres for Kubernetes

PGO, the Postgres Operator from Crunchy Data, comes with all of the features you need for a complete cloud native Postgres experience on Kubernetes!

#### PostgreSQL Cluster [Provisioning][provisioning]

[Create, Scale, & Delete PostgreSQL clusters with ease][provisioning], while fully customizing your
Pods and PostgreSQL configuration!

#### [High Availability][high-availability]

Safe, automated failover backed by a [distributed consensus high availability solution][high-availability].
Uses [Pod Anti-Affinity][k8s-anti-affinity] to help resiliency; you can configure how aggressive this can be!
Failed primaries automatically heal, allowing for faster recovery time.

Support for [standby PostgreSQL clusters][multiple-cluster] that work both within and across [multiple Kubernetes clusters][multiple-cluster].

#### [Disaster Recovery][disaster-recovery]

[Backups][backups] and [restores][disaster-recovery] leverage the open source [pgBackRest][] utility and
[includes support for full, incremental, and differential backups as well as efficient delta restores][backups].
Set how long you to retain your backups. Works great with very large databases!

#### Security and [TLS][tls]

PGO enforces that all connections are over [TLS][tls]. You can also [bring your own TLS infrastructure][tls] if you do not want to use the defaults provided by PGO.

PGO runs containers with locked-down settings and provides Postgres credentials in a secure, convenient way for connecting your applications to your data.

#### [Monitoring][monitoring]

[Track the health of your PostgreSQL clusters][monitoring] using the open source [pgMonitor][] library.

#### [Upgrade Management][update-postgres]

Safely [apply PostgreSQL updates][update-postgres] with minimal impact to the availability of your PostgreSQL clusters.

#### Advanced Replication Support

Choose between [asynchronous][high-availability] and

## features

PGO, the Postgres Operator from Crunchy Data, is tested on the following platforms:

- Kubernetes
- OpenShift
- Rancher
- Google Kubernetes Engine (GKE), including Anthos
- Amazon EKS
- Microsoft AKS
- VMware Tanzu

# Contributing to the Project

Want to contribute to the PostgreSQL Operator project? Great! We've put together
a set of contributing guidelines that you can review here:

- [Contributing Guidelines](CONTRIBUTING.md)

Once you are ready to submit a Pull Request, please ensure you do the following:

1. Reviewing the [contributing guidelines](CONTRIBUTING.md) and ensure
   that you have followed the commit message format, added testing where
   appropriate, documented your changes, etc.
1. Open up a pull request based upon the guidelines. If you are adding a new
   feature, please open up the pull request on the `main` branch.
1. Please be as descriptive in your pull request as possible. If you are
   referencing an issue, please be sure to include the issue in your pull request

## Support

If you believe you have found a bug or have a detailed feature request, please open a GitHub issue and follow the guidelines for submitting a bug.

For general questions or community support, we welcome you to join our [community Discord](https://discord.gg/a7vWKG8Ec9) and ask your questions there.

For other information, please visit the [Support](https://access.crunchydata.com/documentation/postgres-operator/latest/support/) section of the documentation.

# Documentation

For additional information regarding the design, configuration, and operation of the
PostgreSQL Operator, pleases see the [Official Project Documentation][documentation].

[documentation]: https://access.crunchydata.com/documentation/postgres-operator/latest/

## Past Versions

Documentation for previous releases can be found at the [Crunchy Data Access Portal](https://access.crunchydata.com/documentation/).

# Releases

When a PostgreSQL Operator general availability (GA) release occurs, the container images are distributed on the following platforms in order:

- [Crunchy Data Customer Portal](https://access.crunchydata.com/)
- [Crunchy Data Developer Portal](https://www.crunchydata.com/developers)

The image rollout can occur over the course of several days.

To stay up-to-date on when releases are made available in the [Crunchy Data Developer Portal](https://www.crunchydata.com/developers), please sign up for the [Crunchy Data Developer Program Newsletter](https://www.crunchydata.com/developers#email). You can also [join the PGO project community discord](https://discord.gg/a7vWKG8Ec9)

# FAQs, License and Terms

For more information regarding PGO, the Postgres Operator project from Crunchy Data, and Crunchy Postgres for Kubernetes, please see the [frequently asked questions](https://access.crunchydata.com/documentation/postgres-operator/latest/faq). 

The installation instructions provided in this repo are designed for the use of PGO along with Crunchy Data's Postgres distribution, Crunchy Postgres, as Crunchy Postgres for Kubernetes. The unmodified use of these installation instructions will result in downloading container images from Crunchy Data repositories - specifically the Crunchy Data Developer Portal. The use of container images downloaded from the Crunchy Data Developer Portal are subject to the [Crunchy Data Developer Program terms](https://www.crunchydata.com/developers/terms-of-use).  

The PGO Postgres Operator project source code is available subject to the [Apache 2.0 license](LICENSE.md) with the PGO logo and branding assets covered by [our trademark guidelines](docs/static/logos/TRADEMARKS.md).
