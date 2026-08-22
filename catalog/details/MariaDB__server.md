# MariaDB/server

MariaDB server is a community developed fork of MySQL server. Started by core members of the original MySQL team, MariaDB actively works with outside developers to deliver the most featureful, stable,

## features

* **Native vector search**. A built-in VECTOR data type with approximate
  nearest-neighbour indexing (HNSW), available since MariaDB 11.8 with
  no extension required.
* **Pluggable storage engines**. InnoDB (default for transactional workloads),
  Aria, MyRocks, ColumnStore for analytics, Spider for sharding, and S3
  for archival, among others.
* **Replication and clustering**. Asynchronous, semi-synchronous, and
  parallel replication with global transaction IDs, plus Galera synchronous
  multi-primary clustering.
* **Advanced SQL**. Common table expressions and recursive CTEs, window
  functions, system-versioned (temporal) tables, sequences, and a broad set
  of JSON functions.
* **MySQL and Oracle compatibility**. Wire-protocol and syntax compatibility
  with MySQL, plus an Oracle SQL mode supporting PL/SQL-style stored routines.
* **Spatial and full-text search**. GIS data types and functions, and built-in
  full-text indexing.
* **Security**. Role-based access control, pluggable authentication (ed25519,
  PAM, GSSAPI, and more), data-at-rest encryption, and TLS for connections.

## installation

Packages and installation instructions for all supported platforms are
available at [https://mariadb.org/download/](https://mariadb.org/download/).
