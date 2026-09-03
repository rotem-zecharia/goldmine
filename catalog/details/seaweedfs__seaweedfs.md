# seaweedfs/seaweedfs

SeaweedFS is a distributed storage system for object storage (S3), file systems, and Iceberg tables, designed to handle billions of files with O(1) disk access and effortless horizontal scaling.

## installation

## One command ##

Download the latest binary from the [releases](https://github.com/seaweedfs/seaweedfs/releases/latest) page and unzip the single `weed` (or `weed.exe`) file, or let the install script put it in `/usr/local/bin`:

```bash
curl -fsSL https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/install.sh | bash
```

Then start a ready-to-use S3 object store:

```bash
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
S3_BUCKET=my-bucket \
./weed mini -dir=./data
```

That's it. The S3 endpoint is at http://localhost:8333, `my-bucket` exists, and `admin`/`secret` are valid credentials:

```bash
AWS_ACCESS_KEY_ID=admin AWS_SECRET_ACCESS_KEY=secret \
  aws --endpoint-url http://localhost:8333 s3 cp README.md s3://my-bucket/
```

The same process also runs the master, a volume server, the filer, WebDAV, the Iceberg REST catalog, and the Admin UI. Add `S3_TABLE_BUCKET=warehouse` to also create an Iceberg table bucket, or `warehouse:LANCE` for a Lance one. Drop the AWS keys to run without authentication for development.

> macOS: if the binary is quarantined, run `xattr -d com.apple.quarantine ./weed` first.

`weed mini` is auto-tuned for one node and is fine for single-node production, such as an S3 gateway that issues presigned URLs. See [Quick Start with weed mini][WeedMini].

## Docker ##

```bash
docker run -p 8333:8333 -v weed-data:/data \
  -e AWS_ACCESS_KEY_ID=admin \
  -e AWS_SECRET_ACCESS_KEY=secret \
  -e S3_BUCKET=my-bucket \
  chrislusf/seaweedfs
```

Same behavior as the `weed mini` command above.

## Docker Compose ##

To run master, volume server, filer, S3, and WebDAV as separate services:

```bash
wget https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/docker/seaweedfs-compose.yml
wget -P prometheus https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/docker/prometheus/prometheus.yml
docker compose -f seaweedfs-compose.yml -p seaweedfs up
```

[Docker Compose for S3][DockerComposeS3] adds credentials, and the [docker/compose](docker/compose) folder has variants for replication, mounts, message queues, and more.

## Kubernetes with Helm ##

```bash
helm repo add seaweedfs https://seaweedfs.github.io/seaweedfs/helm
helm install seaweedfs seaweedfs/seaweedfs -n seaweedfs --create-namespace -f values.yaml
```

A production-shaped `values.yaml` for a three-node cluster: two copies of every write, three masters, and an S3 endpoint with credentials and a bucket.

```yaml
global:
  seaweedfs:
    enableReplication: true
    replicationPlacement: "001"   # one extra copy on another server; "002" for two

master:
  replicas: 3
  data:
    type: persistentVolumeClaim   # the cluster's default storage class; add storageClass to pick one
    size: 1Gi

volume:
  replicas: 3                     # at least 1 + the sum of the replication digits
  dataDirs:
    - name: data
      type: persistentVolumeClaim
      size: 500Gi
      maxVolumes: 0               # size the volume count from the disk

filer:
  replicas: 2
  data:
    type: persistentVolumeClaim
    size: 20Gi

s3:
  enabled: true
  replicas: 2
  enableAuth: true
  credentials:
    admin:
      accessKey: admin
      secretKey: change-me
  createBuckets:
    - name: app-storage
```

The S3 endpoint is the `seaweedfs-s3` service on port 8333. [Helm Chart Recipes][HelmRecipes] has values for a development cluster, a lakehouse with the Iceberg catalog exposed, filer metadata on PostgreSQL, and node-local disks. The [SeaweedFS Operator][Operator] and the [CSI driver][SeaweedFsCsiDriver] are the other Kubernetes paths.

## Build from source ##

```bash
git clone https://github.com/seaweedfs/seaweedfs.git
cd seaweedfs/weed && make install
```

`weed` lands in `$GOPATH/bin`. [Getting Started][GettingStarted] covers running master, volume, filer, and S3 as separate processes.

## Scale out ##

Capacity is a volume server. Start one on any machine with disk and point it at the master:

```bash
weed volume -dir=/data -master=<master_host>:9

## features

## Fast ##

* One disk read per blob. A small file is one blob; a large file is split into chunks of a few MB, each its own blob. A volume server keeps a 16-byte index entry per blob in memory and reads it in a single seek, also for erasure-coded data.
* The master is not in the read path. Clients cache the volume-to-server mapping and talk to volume servers directly.
* 40 bytes of metadata per file on disk. Small files are packed into append-only volume files, so there is no per-file inode, no per-file metadata file, no fragmentation, and writes are SSD friendly.
* Hot data is replicated; [erasure coding][ErasureCoding] is applied to warm data in the background, so writes never pay the encoding cost.
* The [Rust volume server][RustVolume] is a drop-in for higher throughput and lower tail latency on the same on-disk format.

On one laptop, [`weed benchmark`][Benchmarks] writes 1KB files at 15,700 per second and reads them back at 47,000 per second, and a mixed S3 [warp][S3Benchmark] run totals 3.2 GiB/s. Numbers are in the [Benchmark](#benchmark) section; throughput grows with volume servers and gateways.

## Scalable ##

* The master tracks volumes, not files. A cluster with billions of files has a few thousand volumes, so the master stays small. One master is enough for most clusters; run three for [Raft failover][FailoverMaster].
* Adding a server adds capacity with no data reshuffle. Balancing, vacuum, erasure coding, and repair run on demand from [`weed shell`][WeedShell] or the [maintenance worker][Worker].
* Filer and S3 gateways are stateless and scale linearly. Directory metadata lives in a [store you already run][FilerStores]: LevelDB, RocksDB, SQLite, MySQL, PostgreSQL, Cassandra, HBase, MongoDB, Redis, Elasticsearch, etcd, TiKV, FoundationDB, YDB, ArangoDB, Tarantool, and MySQL or PostgreSQL compatible databases such as TiDB, CockroachDB, and MemSQL.
* Rack and data center aware [replication][Replication], [tiered storage][TieredStorage] across disk types, and [transparent cloud tiering][CloudTier] for unlimited capacity.
* Files from a byte to [tens of TB][SuperLargeFiles]. Volumes up to 8TB with the large-disk build.

## tools

The S3 gateway implements the object, bucket, S3 Tables, IAM, and STS APIs on one endpoint, so the AWS SDKs and CLI, rclone, restic, Spark, and Trino work unchanged.

| API | Operations |
| --- | --- |
| S3 bucket and object | 73 |
| S3 Tables | 36 |
| IAM | 39 |
| STS | 5 |

* [Versioning][Versioning], [Object Lock][ObjectLock] with retention and legal hold, [lifecycle][Lifecycle] rules, tagging, [CORS][CORS], [conditional reads and writes][ConditionalOps], checksums, presigned URLs, browser POST uploads, multipart uploads, and an atomic [RenameObject][RenameObject].
* [Bucket policies][BucketPolicies] with [conditions][PolicyConditions] and [variables][PolicyVariables]; IAM users, groups, and policies; STS with [OIDC][OIDC], LDAP, and [Kubernetes service accounts][K8sSA].
* [SSE-S3, SSE-KMS, and SSE-C][SSE] server-side encryption, with OpenBao and Vault, AWS KMS, Azure Key Vault, and GCP KMS as key providers.
* [Audit log][AuditLog], [bucket quota][BucketQuota], and [rate limiting][RateLimiting].
* Each bucket is its own collection, so deleting a bucket is instant.

The full operation list is in [Amazon S3 API][AmazonS3API], and [Supported APIs vs MinIO][S3vsMinio] compares. The S3 compatibility suite and the SDK, IAM, SSE, policy, and Spark integration tests run in CI on every change.

## A data warehouse with S3 Tables ##

SeaweedFS is a lakehouse in one system. [S3 Table Buckets][S3TableBucket] hold Apache Iceberg tables by default, or [Lance][LanceCatalog] tables for vectors and multimodal data, and the built-in [Iceberg REST Catalog][IcebergCatalog] and Lance namespace serve them directly. There is no Hive Metastore, Glue, or separate catalog service to deploy, secure, and back up.

* Query engines operate on the same tables at the same time: [Spark][SparkIceberg], [Trino][TrinoIceberg], [Dremio][DremioIceberg], [DuckDB][DuckDBIceberg], [Apache Doris][DorisIceberg], [RisingWave][RisingWaveIceberg], ClickHouse, and [LanceDB][LanceDB]. Catalog commits are atomic compare-and-swap, so concurrent writers are safe. [Lakekeeper][Lakekeeper] can front the same storage with STS-vended credentials.
* [Automated table maintenance][IcebergMaintenance]: compaction, snapshot expiration, orphan file removal, and manifest rewriting, configured per bucket or table through the S3 Tables maintenance APIs, and the same for [Lance][LanceMaintenance].
* IAM at the bucket, namespace, and table level with standard bucket policies, see [S3 Tables Security][S3TablesSecurity].
* A [Hadoop compatible file system][Hadoop] for Spark, Flink, and HBase.

`S3_TABLE_BUCKET=warehouse ./weed mini -dir=./data` brings the whole stack up on a laptop.

## A fast cache for cloud storage ##

[Cloud Drive][CloudDrive] mounts a bucket from S3, Google Cloud Storage, Azure, Backblaze B2, Wasabi, Storj, or any S3-compatible store into SeaweedFS and serves it at local speed:

* Metadata is pulled once, so listing, stat, and directory walks cost no cloud API calls.
* File content is downloaded once, on first read or [warmed][CacheRemote] by folder, name pattern, size, or age, and cached with the capacity of the whole cluster: cache everything, no churn.
* Local writes complete at local latency and are written back to the cloud asynchronously in the cloud's native layout, so other tools keep reading the bucket directly.
* Uncache by the same rules to free local disk while keeping the metadata.

[Cloud Tier][CloudTier] goes the other direction, moving whole warm volumes to cloud storage while keeping one-read access, and the [Gateway to Remote Object Storage][GatewayToRemoteObjectStore] mirrors every bucket to a remote store. Faster and cheaper than reading the cloud directly.

## Active-active replication and more ##

* [Active-active or active-passive replication][ActiveActiveAsyncReplication] between clusters, continuous and resumable, for the whole tree or chosen folders, across data centers.
* [Filer store replication][FilerStoreReplication] for metadata HA, [async
