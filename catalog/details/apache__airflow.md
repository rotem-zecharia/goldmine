# apache/airflow

Apache Airflow - A platform to programmatically author, schedule, and monitor workflows

## requirements

Apache Airflow is tested with:

|            | Main version (dev)                 | Stable version (3.3.0)              | Deprecate version (2.11.2)   |
|------------|------------------------------------|-------------------------------------|------------------------------|
| Python     | 3.10, 3.11, 3.12, 3.13, 3.14       | 3.10, 3.11, 3.12, 3.13, 3.14        | 3.10, 3.11, 3.12             |
| Platform   | AMD64/ARM64                        | AMD64/ARM64                         | AMD64/ARM64(\*)              |
| Kubernetes | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35 | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35  | 1.26, 1.27, 1.28, 1.29, 1.30 |
| PostgreSQL | 14, 15, 16, 17, 18                 | 14, 15, 16, 17, 18                  | 12, 13, 14, 15, 16           |
| MySQL      | 8.0, 8.4, Innovation               | 8.0, 8.4, Innovation                | 8.0, Innovation              |
| SQLite     | 3.15.0+                            | 3.15.0+                             | 3.15.0+                      |

\* Experimental

**Note**: MariaDB is not tested/recommended.

**Note**: SQLite is used in Airflow tests. Do not use it in production. We recommend
using the latest stable version of SQLite for local development.

**Note**: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly
tested on fairly modern Linux Distros and recent versions of macOS.
On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers.
The work to add Windows support is tracked via [#10388](https://github.com/apache/airflow/issues/10388), but
it is not a high priority. You should only use Linux-based distros as "Production" execution environment
as this is the only environment that is supported. The only distro that is used in our CI tests and that
is used in the [Community managed DockerHub image](https://hub.docker.com/p/apache/airflow) is
`Debian Bookworm`.

<!-- END Requirements, please keep comment here to allow auto update of PyPI readme.md -->
<!-- START Getting started, please keep comment here to allow auto update of PyPI readme.md -->

## installation

Visit the official Airflow website documentation (latest **stable** release) for help with
[installing Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/),
[getting started](https://airflow.apache.org/docs/apache-airflow/stable/start.html), or walking
through a more complete [tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/).

> Note: If you're looking for documentation for the main branch (latest development branch): you can find it on [s.apache.org/airflow-docs](https://s.apache.org/airflow-docs/).

For more information on Airflow Improvement Proposals (AIPs), visit
the [Airflow Wiki](https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Improvement+Proposals).

Documentation for dependent projects like provider distributions, Docker image, Helm Chart, you'll find it in [the documentation index](https://airflow.apache.org/docs/).

<!-- END Getting started, please keep comment here to allow auto update of PyPI readme.md -->
<!-- START Installing from PyPI, please keep comment here to allow auto update of PyPI readme.md -->
