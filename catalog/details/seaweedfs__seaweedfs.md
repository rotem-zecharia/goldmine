# seaweedfs/seaweedfs

SeaweedFS is a distributed storage system for object storage (S3), file systems, and Iceberg tables, designed to handle billions of files with O(1) disk access and effortless horizontal scaling.

## installation

## Quick Start with weed mini ##

Download the latest binary from https://github.com/seaweedfs/seaweedfs/releases and unzip the single `weed` (or `weed.exe`) file, or run `go install github.com/seaweedfs/seaweedfs/weed@latest`. Then start a ready-to-use S3 object store with credentials and a pre-created bucket in one command:

```bash
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
S3_BUCKET=my-bucket \
./weed mini -dir=/data
```

That's it — the S3 endpoint is at http://localhost:8333, `my-bucket` already exists, and `admin`/`secret` are valid credentials. `S3_BUCKET` accepts a comma-separated list (e.g. `raw,processed`); use `S3_TABLE_BUCKET` for S3 Tables buckets, each `name` or `name:FORMAT` where the format is `ICEBERG` (the default) or `LANCE`. Drop any of the env vars to skip that piece (no AWS keys → S3 runs in unauthenticated "Allow All" mode for development).

The same command starts everything else too:
- **S3 Endpoint**: http://localhost:8333
- **Master UI**: http://localhost:9333
- **Volume Server**: http://localhost:9340
- **Filer UI**: http://localhost:8888
- **WebDAV**: http://localhost:7333
- **Admin UI**: http://localhost:23646

> macOS: if the binary is quarantined, run `xattr -d com.apple.quarantine ./weed` first.

Perfect for development, testing, learning SeaweedFS, and single-node deployments. To scale out, add more volume servers by running `weed volume -dir="/some/data/dir2" -master="<master_host>:9333" -port=8081` locally, on another machine, or on thousands of machines.

## Quick Start for S3 API on Docker ##

```bash
docker run -p 8333:8333 \
  -e AWS_ACCESS_KEY_ID=admin \
  -e AWS_SECRET_ACCESS_KEY=secret \
  -e S3_BUCKET=my-bucket \
  chrislusf/seaweedfs
```

Same behavior as the `weed mini` command above — the S3 endpoint is at http://localhost:8333 with `my-bucket` pre-created. Drop the env vars to run anonymously for development.

# Introduction #

SeaweedFS is a simple and highly scalable distributed file system. There are two objectives:

1. to store billions of files!
2. to serve the files fast!

SeaweedFS started as a blob store to handle small files efficiently. 
Instead of managing all file metadata in a central master, 
the central master only manages volumes on volume servers, 
and these volume servers manage files and their metadata. 
This relieves concurrency pressure from the central master and spreads file metadata into volume servers, 
allowing faster file access (O(1), usually just one disk read operation).

There is only 40 bytes of disk storage overhead for each file's metadata. 
It is so simple with O(1) disk reads that you are welcome to challenge the performance with your actual use cases.

SeaweedFS started by implementing [Facebook's Haystack design paper](http://www.usenix.org/event/osdi10/tech/full_papers/Beaver.pdf). 
Also, SeaweedFS implements erasure coding with ideas from 
[f4: Facebook’s Warm BLOB Storage System](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-muralidhar.pdf), and has a lot of similarities with [Facebook’s Tectonic Filesystem](https://www.usenix.org/system/files/fast21-pan.pdf) and [Google's Colossus File System](https://cloud.google.com/blog/products/storage-data-transfer/a-peek-behind-colossus-googles-file-system)

On top of the blob store, optional [Filer] can support directories and POSIX attributes. 
Filer is a separate linearly-scalable stateless server with customizable metadata stores, 
e.g., MySql, Postgres, Redis, Cassandra, HBase, Mongodb, Elastic Search, LevelDB, RocksDB, Sqlite, MemSql, TiDB, Etcd, CockroachDB, YDB, etc.

SeaweedFS can transparently integrate with the cloud. 
With hot data on local cluster, and warm data on the cloud with O(1) access time, 
SeaweedFS can achieve both fast local access time and elastic cloud storage capacity.
What's more, the cloud storage access API cost is minimized. 
Faster and cheaper than direct cloud storage!

SeaweedFS also ships a built-in **Iceberg REST Catalog**, turn

## features

## Additional Blob Store Features ##
* Support different replication levels, with rack and data center aware.
* Automatic master servers failover - no single point of failure (SPOF).
* Automatic compression depending on file MIME type.
* Automatic compaction to reclaim disk space after deletion or update.
* [Automatic entry TTL expiration][VolumeServerTTL].
* Flexible Capacity Expansion: Any server with some disk space can add to the total storage space.
* Adding/Removing servers does **not** cause any data re-balancing unless triggered by admin commands.
* Optional picture resizing.
* Support ETag, Accept-Range, Last-Modified, etc.
* Support in-memory/leveldb/readonly mode tuning for memory/performance balance.
* Support rebalancing the writable and readonly volumes.
* [Customizable Multiple Storage Tiers][TieredStorage]: Customizable storage disk types to balance performance and cost.
* [Transparent cloud integration][CloudTier]: unlimited capacity via tiered cloud storage for warm data.
* [Erasure Coding for warm storage][ErasureCoding]  Rack-Aware 10.4 erasure coding reduces storage cost and increases availability. Enterprise version can customize EC ratio.

[Back to TOC](#table-of-contents)

## Filer Features ##
* [Filer server][Filer] provides "normal" directories and files via HTTP.
* [File TTL][FilerTTL] automatically expires file metadata and actual file data.
* [Mount filer][Mount] reads and writes files directly as a local directory via FUSE.
* [Filer Store Replication][FilerStoreReplication] enables HA for filer meta data stores.
* [Active-Active Replication][ActiveActiveAsyncReplication] enables asynchronous one-way or two-way cross cluster continuous replication.
* [Amazon S3 compatible API][AmazonS3API] accesses files with S3 tooling.
* [Hadoop Compatible File System][Hadoop] accesses files from Hadoop/Spark/Flink/etc or even runs HBase.
* [Async Replication To Cloud][BackupToCloud] has extremely fast local access and backups to Amazon S3, Google Cloud Storage, Azure, BackBlaze.
* [WebDAV] accesses as a mapped drive on Mac and Windows, or from mobile devices.
* [AES256-GCM Encrypted Storage][FilerDataEncryption] safely stores the encrypted data.
* [Super Large Files][SuperLargeFiles] stores large or super large files in tens of TB.
* [Cloud Drive][CloudDrive] mounts cloud storage to local cluster, cached for fast read and write with asynchronous write back.
* [Gateway to Remote Object Store][GatewayToRemoteObjectStore] mirrors bucket operations to remote object storage, in addition to [Cloud Drive][CloudDrive]

## Data Lakehouse Features ##
* [S3 Table Buckets][S3TableBucket] expose a dedicated namespace for Iceberg tables with strict layout validation.
* Built-in [Iceberg REST Catalog][IcebergCatalog] runs alongside the S3 endpoint — no external metastore needed.
* Native integrations with [Apache Spark][SparkIceberg], [Trino][TrinoIceberg], [Dremio][DremioIceberg], [DuckDB][DuckDBIceberg], and [RisingWave][RisingWaveIceberg].
* [Automated table maintenance][IcebergMaintenance]: compaction, snapshot expiration, orphan removal, manifest rewriting.
* Granular IAM at the bucket, namespace, and table level via standard S3 bucket policies.

## Kubernetes ##
* [Kubernetes CSI Driver][SeaweedFsCsiDriver] A Container Storage Interface (CSI) Driver. [![Docker Pulls](https://img.shields.io/docker/pulls/chrislusf/seaweedfs-csi-driver.svg?maxAge=4800)](https://hub.docker.com/r/chrislusf/seaweedfs-csi-driver/)
* [SeaweedFS Operator](https://github.com/seaweedfs/seaweedfs-operator)

[Filer]: https://github.com/seaweedfs/seaweedfs/wiki/Directories-and-Files
[SuperLargeFiles]: https://github.com/seaweedfs/seaweedfs/wiki/Data-Structure-for-Large-Files
[Mount]: https://github.com/seaweedfs/seaweedfs/wiki/FUSE-Mount
[AmazonS3API]: https://github.com/seaweedfs/seaweedfs/wiki/Amazon-S3-API
[BackupToCloud]: https://github.com/seaweedfs/seaweedfs/wiki/Async-Replication-to-Cloud
[Hadoop]: https://github.com/seaweedfs/seaweedfs/wiki/Ha
