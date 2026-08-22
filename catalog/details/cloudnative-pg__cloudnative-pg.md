# cloudnative-pg/cloudnative-pg

The most popular Kubernetes Operator for PostgreSQL.

## installation

The best way to get started is the [Quickstart Guide](https://cloudnative-pg.io/docs/devel/quickstart/).

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
