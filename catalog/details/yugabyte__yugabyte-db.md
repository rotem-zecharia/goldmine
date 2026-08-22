# yugabyte/yugabyte-db

YugabyteDB - the cloud native distributed SQL database for mission-critical applications.

## features

* **[Powerful RDBMS capabilities](https://docs.yugabyte.com/stable/explore/ysql-language-features/)** Yugabyte SQL (*YSQL* for short) reuses the PostgreSQL query layer (similar to Amazon Aurora PostgreSQL), thereby supporting most of its features (datatypes, queries, expressions, operators and functions, stored procedures, triggers, extensions, and so on).

* **[Distributed transactions](https://docs.yugabyte.com/stable/architecture/transactions/)** The transaction design is based on the Google Spanner architecture. Strong consistency of writes is achieved by using Raft consensus for replication and cluster-wide distributed ACID transactions using *hybrid logical clocks*. *Snapshot*, *serializable* and *read committed* isolation levels are supported. Reads (queries) have strong consistency by default, but can be tuned dynamically to read from followers and read replicas.

* **[Continuous availability](https://docs.yugabyte.com/stable/explore/fault-tolerance/)** YugabyteDB is extremely resilient to common outages with native failover and repair. YugabyteDB can be configured to tolerate disk, rack, node, zone, region, and cloud failures automatically. For a typical deployment where a YugabyteDB cluster is deployed in one region across multiple zones on a public cloud, the RPO is 0 (meaning no data is lost on failure) and the RTO is 3 seconds (meaning the data being served by the failed node is available in 3 seconds).

* **[Horizontal scalability](https://docs.yugabyte.com/stable/explore/linear-scalability/)** Scaling a YugabyteDB cluster to achieve more IOPS or data storage is as simple as adding nodes to the cluster.

* **[Geo-distributed, multi-cloud](https://docs.yugabyte.com/stable/develop/multi-cloud/)** YugabyteDB can be deployed in public clouds and natively inside Kubernetes. It supports deployments that span three or more fault domains, such as multi-zone, multi-rack, multi-region, and multi-cloud deployments. It also supports xCluster asynchronous replication with unidirectional master-slave and bidirectional multi-master configurations in two-region deployments. Read replicas are also a supported to serve (stale) data with low latencies.

* **[Multi API design](https://docs.yugabyte.com/stable/api)** The YugabyteDB query layer is built to be extensible. Currently, YugabyteDB supports two distributed SQL APIs: [Yugabyte SQL (YSQL)](https://docs.yugabyte.com/stable/api/ysql/), a fully relational API that re-uses the PostgreSQL query layer, and [Yugabyte Cloud QL (YCQL)](https://docs.yugabyte.com/stable/api/ycql/), a semi-relational SQL-like API with documents/indexing support with Apache Cassandra QL roots.

* **[100% open source](https://github.com/yugabyte/yugabyte-db)** YugabyteDB is fully open-source under the [Apache 2.0 license](https://github.com/yugabyte/yugabyte-db/blob/master/LICENSE.md). The open-source version has powerful enterprise features such as distributed backups, encryption of data at rest, in-flight TLS encryption, change data capture, read replicas, and more.

YugabyteDB was created with several key design goals in mind, aiming to address the challenges faced by modern, cloud-native applications while maintaining the familiarity and power of traditional relational databases. Read more about these in our [Design goals](https://docs.yugabyte.com/stable/architecture/design-goals/).

## limitations

The following is a list of some of the key features being worked on for upcoming releases.

|                                                  Feature                                                   |                                                           Details                                                           |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [PostgreSQL 15 Compatibility](https://github.com/yugabyte/yugabyte-db/issues/9797)                         | For latest features, new PostgreSQL extensions, performance, and community fixes.                                            |
| [PostgreSQL Publication/Replication slot API in CDC](https://github.com/yugabyte/yugabyte-db/issues/18724) | PostgreSQL has a huge community that needs a PG-compatible API to set up and consume database changes.                      |
| [Bitmap scan](https://github.com/yugabyte/yugabyte-db/issues/22653)                                        | Bitmap Scan support for using Index Scans, remote filter and enhanced Cost Model.                                            |
| [Cost based optimizer(CBO)](https://github.com/yugabyte/yugabyte-db/issues/10177)                          | Efficient query plans based on statistics (such as table size, number of rows) and data distribution.                       |
| [Parallel query execution](https://github.com/yugabyte/yugabyte-db/issues/17984)                           | Higher query performance by splitting a single query for execution across different CPU cores.          |
| [pgvector extension](https://github.com/yugabyte/yugabyte-db/issues/16166)                                 | Support for vector data types, enabling efficient storage and querying of high-dimensional vectors.                         |
| [Connection Management](https://github.com/yugabyte/yugabyte-db/issues/17599)                              | Server side connection management enabling upto 30K connections per node                                                    |

Refer to [roadmap tracker](https://github.com/yugabyte/yugabyte-db/issues?q=is:issue+is:open+label:current-roadmap) for the list of all items in the current roadmap.

## configuration

Time synchronization across nodes has been enhanced through the use of the [ClockBound](https://github.com/aws/clock-bound) library, which is an open source daemon that allows you to compare timestamps to determine order for events and transactions, independent of an instance's geographic location; it improves clock accuracy by several orders of magnitude.

## installation

YugabyteDB now supports seamless replication of YSQL DDL changes across xCluster setups, eliminating the need to manually apply DDLs on both source and target clusters.
