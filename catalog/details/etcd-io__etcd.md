# etcd-io/etcd

Distributed reliable key-value store for the most critical data of a distributed system

## installation

### Getting etcd

The easiest way to get etcd is to use one of the pre-built release binaries which are available for OSX, Linux, Windows, and Docker on the [release page][github-release].

For more installation guides, please check out [play.etcd.io](http://play.etcd.io) and [operating etcd](https://etcd.io/docs/latest/op-guide).

[github-release]: https://github.com/etcd-io/etcd/releases

### Running etcd

First start a single-member cluster of etcd.

If etcd is installed using the [pre-built release binaries][github-release], run it from the installation location as below:

```bash
/tmp/etcd-download-test/etcd
```

The etcd command can be simply run as such if it is moved to the system path as below:

```bash
mv /tmp/etcd-download-test/etcd /usr/local/bin/
etcd
```

This will bring up etcd listening on port 2379 for client communication and on port 2380 for server-to-server communication.

Next, let's set a single key, and then retrieve it:

```bash
etcdctl put mykey "this is awesome"
etcdctl get mykey
```

etcd is now running and serving client requests. For more, please check out:

* [Interactive etcd playground](http://play.etcd.io)
* [Animated quick demo](https://etcd.io/docs/latest/demo)

### etcd TCP ports

The [official etcd ports][iana-ports] are 2379 for client requests, and 2380 for peer communication.

[iana-ports]: http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt

### Running a local etcd cluster

First install [goreman](https://github.com/mattn/goreman), which manages Procfile-based applications.

Our [Procfile script](./Procfile) will set up a local example cluster. Start it with:

```bash
goreman start
```

This will bring up 3 etcd members `infra1`, `infra2` and `infra3` and optionally etcd `grpc-proxy`, which runs locally and composes a cluster.

Every cluster member and proxy accepts key value reads and key value writes.

Follow the comments in [Procfile script](./Procfile) to add a learner node to the cluster.

### Install etcd client v3

```bash
go get go.etcd.io/etcd/client/v3
```

### Next steps

Now it's time to dig into the full etcd API and other guides.

* Read the full [documentation].
* Review etcd [frequently asked questions].
* Explore the full gRPC [API].
* Set up a [multi-machine cluster][clustering].
* Learn the [config format, env variables and flags][configuration].
* Find [language bindings and tools][integrations].
* Use TLS to [secure an etcd cluster][security].
* [Tune etcd][tuning].

[documentation]: https://etcd.io/docs/latest
[api]: https://etcd.io/docs/latest/learning/api
[clustering]: https://etcd.io/docs/latest/op-guide/clustering
[configuration]: https://etcd.io/docs/latest/op-guide/configuration
[integrations]: https://etcd.io/docs/latest/integrations
[security]: https://etcd.io/docs/latest/op-guide/security
[tuning]: https://etcd.io/docs/latest/tuning

## Contact

* Email: [etcd-dev](https://groups.google.com/g/etcd-dev)
* Slack: [#sig-etcd](https://kubernetes.slack.com/archives/C3HD8ARJ5) channel on Kubernetes ([get an invite](http://slack.kubernetes.io/))
* [Community meetings](#community-meetings)

### Community meetings

etcd contributors and maintainers meet every week at `11:00` AM (USA Pacific) on Thursday and meetings alternate between community meetings and issue triage meetings. Meeting agendas are recorded in a [shared Google doc][shared-meeting-notes] and everyone is welcome to suggest additional topics or other agendas.

Issue triage meetings are aimed at getting through our backlog of PRs and Issues. Triage meetings are open to any contributor; you don't have to be a reviewer or approver to help out! They can also be a good way to get started contributing.

The meeting lead role is rotated for each meeting between etcd maintainers or sig-etcd leads and is recorded in a [shared Google sheet][shared-rotation-sheet].

Meeting recordings are uploaded to the official etcd [YouTube channel].

Get calendar invitations by joining 
