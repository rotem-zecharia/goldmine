# goss-org/goss

Quick and Easy server testing/validation

## features

* Goss is EASY! - [Goss in 45 seconds](#goss-in-45-seconds)
* Goss is FAST! - small-medium test suites are near instantaneous, see [benchmarks](https://github.com/goss-org/goss/wiki/Benchmarks)
* Goss is SMALL! - <10MB single self-contained binary

## installation

**Note:** For macOS and Windows, see: [platform-feature-parity].

This will install goss and [dgoss](https://github.com/goss-org/goss/tree/master/extras/dgoss).

**Note:** Using `curl | sh` is not recommended for production systems, use manual installation below.

```bash

## limitations

`goss` works well on Linux, but support on Windows & macOS is alpha. See [platform-feature-parity].

The following tests have limitations.

Package:

* rpm
* deb
* Alpine apk
* pacman

Service:

* systemd
* sysV init
* OpenRC init
* Upstart

[kubernetes-simplified-health-checks]: https://medium.com/@aelsabbahy/docker-1-12-kubernetes-simplified-health-checks-and-container-ordering-with-goss-fa8debbe676c
[platform-feature-parity]: https://goss.readthedocs.io/en/stable/platforms/

<!-- --8<-- [end:about] -->
