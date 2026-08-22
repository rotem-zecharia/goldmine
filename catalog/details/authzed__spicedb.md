# authzed/spicedb

Open Source, Google Zanzibar-inspired database for scalably storing and querying fine-grained authorization data

## features

- [**World-class engineering**][about]: painstakingly built by experts that pioneered the cloud-native ecosystem
- [**Authentic design**][zanzibar]: mature and feature-complete implementation of Google's Zanzibar paper
- [**Proven in production**][1M]: 5ms p95 when scaled to millions of queries/s, billions of relationships
- [**Global consistency**][consistency]: consistency configured per-request unlocks correctness while maintaining performance
- [**Multi-paradigm**][caveats]: caveated relationships combine the best concepts in authorization: ABAC & ReBAC
- [**Safety in tooling**][tooling]: designs schemas with real-time validation or validate in your CI/CD workflow
- [**Reverse Indexes**][reverse-indexes]: queries for "What can `subject` do?", "Who can access `resource`?"

[about]: https://authzed.com/why-authzed
[1M]: https://authzed.com/blog/google-scale-authorization
[caveats]: https://netflixtechblog.com/abac-on-spicedb-enabling-netflixs-complex-identity-types-c118f374fa89
[tooling]: https://authzed.com/docs/spicedb/modeling/validation-testing-debugging
[reverse-indexes]: https://authzed.com/docs/spicedb/getting-started/faq#what-is-a-reverse-index
[consistency]: https://authzed.com/docs/spicedb/concepts/consistency

### Who uses SpiceDB?

SpiceDB is a powerful tool in a variety of domains and in organizations of all sizes; we've chosen to highlight a few interesting community members:

- [IBM's AI Data & Model Factory Platform](https://youtu.be/4K2a9HcRhXA)
- [Red Hat's Insights Platform](https://www.redhat.com/en/technologies/management/insights)
- [GitPod](https://github.com/gitpod-io/gitpod/issues/15632)
- [TubiTV China (中文)](https://zhuanlan.zhihu.com/p/685603356)
- [DMM Online Salon (日本語)](https://inside.dmm.com/articles/salon-datebase-migration-challenges/)

Beyond the community, you can also read [customer stories][stories] for commercial usage of SpiceDB.

[stories]: https://authzed.com/customers

## installation

### Installing the binary

Binary releases are available for Linux, macOS, and Windows on AMD64 and ARM64 architectures.

[Homebrew] users for both macOS and Linux can install the latest binary releases of SpiceDB and [zed] using the official tap:

```command
brew install authzed/tap/spicedb authzed/tap/zed
```

[Debian-based Linux] users can install SpiceDB packages by adding a new APT source:

```command
sudo apt update && sudo apt install -y curl ca-certificates gpg
curl https://pkg.authzed.com/apt/gpg.key | sudo apt-key add -
sudo echo "deb https://pkg.authzed.com/apt/ * *" > /etc/apt/sources.list.d/fury.list
sudo apt update && sudo apt install -y spicedb zed
```

[RPM-based Linux] users can install SpiceDB packages by adding a new YUM repository:

```command
sudo cat << EOF >> /etc/yum.repos.d/Authzed-Fury.repo
[authzed-fury]
name=AuthZed Fury Repository
baseurl=https://pkg.authzed.com/yum/
enabled=1
gpgcheck=0
EOF
sudo dnf install -y spicedb zed
```

[zed]: https://github.com/authzed/zed
[homebrew]: https://docs.authzed.com/spicedb/installing#brew
[Debian-based Linux]: https://en.wikipedia.org/wiki/List_of_Linux_distributions#Debian-based
[RPM-based Linux]: https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based
  
### Running a container

Container images are available for AMD64 and ARM64 architectures on the following registries:

- [authzed/spicedb](https://hub.docker.com/r/authzed/spicedb)
- [ghcr.io/authzed/spicedb](https://github.com/authzed/spicedb/pkgs/container/spicedb)
- [quay.io/authzed/spicedb](https://quay.io/authzed/spicedb)

[Docker] users can run the latest SpiceDB container with the following:

```shell

## tools

docker run --rm -p 50051:50051 -p 8443:8443 authzed/spicedb serve --http-enabled true --grpc-preshared-key "somerandomkeyhere"
```

SpiceDB containers use [Chainguard Images] to ship the bare minimum userspace which is a huge boon to security, but can complicate debugging.
If you want to execute a user session into a running SpiceDB container and install packages, you can use one of our debug images.

Appending `-debug` to any tag will provide you an image that has a userspace with debug tooling:

```command
docker run --rm -ti --entrypoint sh authzed/spicedb:latest-debug
```

Containers are also available for each git commit to the `main` branch under `${REGISTRY}/authzed/spicedb-git:${COMMIT}`.

[Docker]: https://docs.docker.com/get-docker/
[Chainguard Images]: https://github.com/chainguard-images/images

### Write your own schema and relationships

Now that you have SpiceDB running, you must define your **schema** and write **relationships** that represent the permissions in your application. There are various way to do this:

- Use the [client libraries].
- Use the [hosted Playground] or [run it yourself locally]. The playground contains a set of example schemas and test data for different scenarios.
- Use the [zed] CLI.
- Use the [gRPC](https://buf.build/authzed/api/docs/main:authzed.api.v1) or the [HTTP](https://authzed.com/docs/spicedb/api/http-api) APIs. For example:
  
```shell
    # write a schema
    curl --location 'http://localhost:8443/v1/schema/write' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer somerandomkeyhere' \
    --data '{
        "schema": "definition user {} \n definition folder { \n relation parent: folder\n relation viewer: user \n permission view = viewer + parent->view \n } \n definition document {\n relation folder: folder \n relation viewer: user \n permission view = viewer + folder->view \n }"
    }'

    # write a relationship
    curl --location 'http://localhost:8443/v1/relationships/write' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer somerandomkeyhere' \
    --data '{
        "updates": [
            {
                "operation": "OPERATION_TOUCH",
                "relationship": {
                    "resource": {
                        "objectType": "folder",
                        "objectId": "budget"
                    },
                    "relation": "viewer",
                    "subject": {
                        "object": {
                            "objectType": "user",
                            "objectId": "anne"
                        }
                    }
                }
            }
        ]
    }'
```

You can follow a [guide for developing a schema] or review the the schema language [design documentation].

Finally, you can watch the [SpiceDB primer video on schema development](https://www.youtube.com/watch?v=AoK0LrkGFDY).

[hosted Playground]: https://play.authzed.com
[run it yourself locally]: https://github.com/authzed/playground
[Playground]: https://github.com/authzed/playground
[guide for developing a schema]: https://docs.authzed.com/guides/schema
[design documentation]: https://docs.authzed.com/reference/schema-lang

### Query the SpiceDB API

You can use the [client libraries] or the [gRPC](https://buf.build/authzed/api/docs/main:authzed.api.v1) and [HTTP](https://authzed.com/docs/spicedb/api/http-api) APIs to query SpiceDB. For example,

```shell
curl --location 'http://localhost:8443/v1/permissions/check' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer somerandomkeyhere' \
--data '{
  "consistency": {
    "minimizeLatency": true
  },
  "resource": {
    "objectType": "folder",
    "objectId": "budget"
  },
  "permission": "view",
  "subject": {
    "object": {
      "objectType": "user",
      "objectId": "anne"
    }
 
