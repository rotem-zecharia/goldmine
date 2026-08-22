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

## installation

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
