# cloudnative-pg/cloudnative-pg

The most popular Kubernetes Operator for PostgreSQL.

## installation

The best way to get started is the [Quickstart Guide](https://cloudnative-pg.io/docs/devel/quickstart/).

## Scope

### Mission

CloudNativePG aims to increase PostgreSQL adoption within Kubernetes by making
it an integral part of the development process and GitOps-driven CI/CD
automation.

## features

Designed by PostgreSQL experts for Kubernetes administrators, CloudNativePG
follows a Kubernetes-native approach to PostgreSQL primary/standby cluster
management. Instead of relying on external high-availability tools (like
Patroni, repmgr, or Stolon), it integrates directly with the Kubernetes API to
automate database operations that a skilled DBA would perform manually.

Key design decisions include:

- Direct integration with Kubernetes API: The PostgreSQL cluster’s status is
  available directly in the `Cluster` resource, allowing users to inspect it
  via the Kubernetes API.
- Operator pattern: The operator ensures that the desired PostgreSQL state is
  reconciled automatically, following Kubernetes best practices.
- Immutable application containers: Updates follow an immutable infrastructure
  model, as explained in
  ["Why EDB Chose Immutable Application Containers"](https://www.enterprisedb.com/blog/why-edb-chose-immutable-application-containers).

### How CloudNativePG Works

The operator continuously monitors and updates the PostgreSQL cluster state.
Examples of automated actions include:

- Failover management: If the primary instance fails, the operator elects a new
  primary, updates the cluster status, and orchestrates the transition.
- Scaling read replicas: When the number of desired replicas changes, the
  operator provisions or removes resources such as persistent volumes, secrets,
  and config maps while managing streaming replication.
- Service updates: Kubernetes remains the single source of truth, ensuring
  that PostgreSQL service endpoints are always up to date.
- Rolling updates: When an image is updated, the operator follows a rolling
  strategy—first updating replica pods before performing a controlled
  switchover for the primary.

CloudNativePG manages additional Kubernetes resources to enhance PostgreSQL
management, including: `Backup`, `ClusterImageCatalog`, `Database`,
`ImageCatalog`, `Pooler`, `Publication`, `ScheduledBackup`, and `Subscription`.

## Out of Scope

- **Kubernetes only:** CloudNativePG is dedicated to vanilla Kubernetes
  maintained by the [Cloud Native Computing Foundation
  (CNCF)](https://kubernetes.io/).
- **PostgreSQL only:** CloudNativePG is dedicated to vanilla PostgreSQL
  maintained by the [PostgreSQL Global Development Group
  (PGDG)](https://www.postgresql.org/about/).
- **No support for forks:** Features from PostgreSQL forks will only be
  considered if they can be integrated as extensions or pluggable frameworks.
- **Not a general-purpose database operator:** CloudNativePG does not support
  other databases (e.g., MariaDB).

CloudNativePG can be extended via the [CNPG-I plugin interface](https://github.com/cloudnative-pg/cnpg-i).

## Communications

Please refer to the [Getting in touch](https://github.com/cloudnative-pg#getting-in-touch)
section on the GitHub organization page.

## Community Meetings

Everyone is welcome, no invitation needed. For details, see the
[Community Meetings](https://github.com/cloudnative-pg#cloudnativepg-community-meetings)
section on the GitHub organization page.

## Resources

- [Roadmap](ROADMAP.md)
- [Website](https://cloudnative-pg.io)
- [FAQ](docs/src/faq.md)
- [Blog](https://cloudnative-pg.io/blog/)
- [CloudNativePG plugin Interface (CNPG-I)](https://github.com/cloudnative-pg/cnpg-i).

## Adopters

A list of publicly known users of the CloudNativePG operator is in [ADOPTERS.md](ADOPTERS.md).
Help us grow our community and CloudNativePG by adding yourself and your
organization to this list!

### CloudNativePG at KubeCon

- March 25, 2026, KubeCon Europe 2026 in Amsterdam: ["Cloud Native Theater / Data on Kubernetes Day: From VMs to Kubernetes in a Large Global Bank: A DBA's Journey"](https://kccnceu2026.sched.com/event/2EG01/cloud-native-theater-data-on-kubernetes-day-from-vms-to-kubernetes-in-a-large-global-bank-a-dbas-journey-gabriele-bartolini-edb-laurent-parodi-hsbc) - Gabriele Bartolini, EDB & Laurent Parodi, HSBC
- March 23, 
