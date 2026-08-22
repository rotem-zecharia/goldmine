# seaweedfs/seaweedfs

SeaweedFS is a distributed storage system for object storage (S3), file systems, and Iceberg tables, designed to handle billions of files with O(1) disk access and effortless horizontal scaling.

## installation

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

## features

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
