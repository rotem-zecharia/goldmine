# zalando/postgres-operator

Postgres operator creates and manages PostgreSQL clusters running in Kubernetes

## features

* Rolling updates on Postgres cluster changes, incl. quick minor version updates
* Live volume resize without pod restarts (AWS EBS, PVC)
* Database connection pooling with PGBouncer
* Support fast in place major version upgrade. Supports global upgrade of all clusters.
* Pod protection during bootstrap phase and configurable maintenance windows
* Restore and cloning Postgres clusters on AWS, GCS and Azure
* Additionally logical backups to S3 or GCS bucket can be configured
* Standby cluster from S3 or GCS WAL archive or remote host
* Configurable for non-cloud environments
* Basic credential and user management on K8s, eases application deployments
* Support for custom TLS certificates
* UI to create and edit Postgres cluster manifests
* Compatible with OpenShift
* Multi-arch support

## installation

For a quick first impression follow the instructions of this
[tutorial](docs/quickstart.md).
