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

## features

PGO, the Postgres Operator from Crunchy Data, is tested on the following platforms:

- Kubernetes
- OpenShift
- Rancher
- Google Kubernetes Engine (GKE), including Anthos
- Amazon EKS
- Microsoft AKS
- VMware Tanzu
