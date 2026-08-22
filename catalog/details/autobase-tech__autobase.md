# autobase-tech/autobase

Automated database platform for PostgreSQL® - Your own DBaaS.

## installation

You can deploy PostgreSQL clusters using the Console (UI), command line (Ansible), or GitOps.

### Console (UI)

- [Community Edition](./console/README.md) - Free license for individual developers and hobby projects; includes lightweight cluster deployment.
- [Enterprise Edition](https://autobase.tech/docs#getting-started) - Commercial license for production environments; includes extended cluster management features and support.

### Ansible Collection

- [Ansible Collection](./automation/README.md) - The automation layer for those who prefer Ansible playbooks instead of the database platform.

### GitOps

- [GitOps (CI/CD)](https://autobase.tech/docs/management/gitops) - Manage cluster configuration in Git and apply changes through CI/CD pipelines.

> [!TIP]
> 📩 Contact us at info@autobase.tech, and our team will help you implement Autobase into your infrastructure.

## Compatibility

Red Hat and Debian-based distributions.

###### Supported Linux Distributions:

- **Debian**: 11, 12, 13
- **Ubuntu**: 22.04, 24.04, 26.04
- **CentOS Stream**: 9, 10
- **Oracle Linux**: 8, 9, 10
- **Rocky Linux**: 8, 9, 10
- **AlmaLinux**: 8, 9, 10

Architecture: x86_64 (amd64), aarch64 (arm64).

###### PostgreSQL versions:

All supported PostgreSQL versions.

:white_check_mark: tested, works fine: PostgreSQL 10, 11, 12, 13, 14, 15, 16, 17, 18

_Table of results of daily automated testing of cluster deployment:_
| Distribution | Test result |
|--------------|:----------:|
| Debian 12 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_debian12.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_debian12.yml) |
| Debian 13 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_debian13.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_debian13.yml) |
| Ubuntu 24.04 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_ubuntu2404.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_ubuntu2404.yml) |
| Ubuntu 26.04 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_ubuntu2604.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_ubuntu2604.yml) |
| CentOS Stream 9 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_centosstream9.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_centosstream9.yml) |
| CentOS Stream 10 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_centosstream10.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_centosstream10.yml) |
| Oracle Linux 9 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_oracle_linux9.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_oracle_linux9.yml) |
| Oracle Linux 10 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_oracle_linux10.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_oracle_linux10.yml) |
| Rocky Linux 9 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_rockylinux9.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflows/schedule_pg_rockylinux9.yml) |
| Rocky Linux 10 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/autobase-tech/autobase/schedule_pg_rockylinux10.yml?branch=main)](https://github.com/autobase-tech/autobase/actions/workflow
