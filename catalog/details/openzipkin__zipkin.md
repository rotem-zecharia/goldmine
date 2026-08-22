# openzipkin/zipkin

Zipkin is a distributed tracing system

## requirements

$ ./mvnw -q --batch-mode -DskipTests --also-make -pl zipkin-server clean install
# Run the server
$ java -jar ./zipkin-server/target/zipkin-server-*exec.jar
```

## Artifacts
Server artifacts are under the maven group id `io.zipkin`
Library artifacts are under the maven group id `io.zipkin.zipkin2`

### Library Releases
Releases are at [Maven Central](https://central.sonatype.com/search?q=zipkin&namespace=io.zipkin)

### Library Snapshots
Snapshots are uploaded to [Sonatype](https://central.sonatype.com/repository/maven-snapshots/) after
commits to master.

### Docker Images
Released versions of zipkin-server are published to Docker Hub as `openzipkin/zipkin` and GitHub
Container Registry as `ghcr.io/openzipkin/zipkin`. See [docker](docker) for details.

### Helm Charts
Helm charts are available via `helm repo add zipkin https://zipkin.io/zipkin-helm`.
See [zipkin-helm](https://github.com/openzipkin/zipkin-helm) for details.

### Javadocs
https://zipkin.io/zipkin contains versioned folders with JavaDocs published on each (non-PR) build, as well
as releases.
