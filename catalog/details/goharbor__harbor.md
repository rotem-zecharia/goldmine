# goharbor/harbor

An open source trusted cloud native registry project that stores, signs, and scans content.

## features

* **Cloud native registry**: With support for both container images and [Helm](https://helm.sh) charts, Harbor serves as registry for cloud native environments like container runtimes and orchestration platforms.
* **Role based access control**: Users access different repositories through 'projects' and a user can have different permission for images or Helm charts under a project.
* **Policy based replication**: Images and charts can be replicated (synchronized) between multiple registry instances based on policies with using filters (repository, tag and label). Harbor automatically retries a replication if it encounters any errors. This can be used to assist loadbalancing, achieve high availability, and facilitate multi-datacenter deployments in hybrid and multi-cloud scenarios.
* **Vulnerability Scanning**: Harbor scans images regularly for vulnerabilities and has policy checks to prevent vulnerable images from being deployed.
* **LDAP/AD support**: Harbor integrates with existing enterprise LDAP/AD for user authentication and management, and supports importing LDAP groups into Harbor that can then be given permissions to specific projects.
* **OIDC support**: Harbor leverages OpenID Connect (OIDC) to verify the identity of users authenticated by an external authorization server or identity provider. Single sign-on can be enabled to log into the Harbor portal.
* **Image deletion & garbage collection**: System administrators can run garbage collection jobs so that images (dangling manifests and unreferenced blobs) can be deleted and their space can be freed up periodically.
* **Graphical user portal**: User can easily browse, search repositories and manage projects.
* **Auditing**: All the operations to the repositories are tracked through logs.
* **RESTful API**: RESTful APIs are provided to facilitate administrative operations, and are easy to use for integration with external systems. An embedded Swagger UI is available for exploring and testing the API.
* **Easy deployment**: Harbor can be deployed via Docker compose as well Helm Chart, and a Harbor Operator was added recently as well.

## Architecture

For learning the architecture design of Harbor, check the document [Architecture Overview of Harbor](https://github.com/goharbor/harbor/wiki/Architecture-Overview-of-Harbor).

## tools

* Harbor RESTful API: The APIs for most administrative operations of Harbor and can be used to perform integrations with Harbor programmatically.
  * Part 1: [New or changed APIs](https://editor.swagger.io/?url=https://raw.githubusercontent.com/goharbor/harbor/main/api/v2.0/swagger.yaml)

## installation

**System requirements:**

**On a Linux host:** docker 20.10.10-ce+ and docker-compose 1.18.0+.

Download binaries of **[Harbor release ](https://github.com/goharbor/harbor/releases)** and follow **[Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/)** to install Harbor.

If you want to deploy Harbor on Kubernetes, please use the **[Harbor chart](https://github.com/goharbor/harbor-helm)**.

Refer to the **[documentation](https://goharbor.io/docs/)** for more details on how to use Harbor.
### Verifying Release Signatures
Starting with v2.15.0, Harbor release artifacts are cryptographically signed using Cosign to ensure authenticity and integrity.

Download the installers and signature bundles from the Harbor releases page.

#### Quick Verification
```bash
# Install Cosign (v2.0+)
brew install sigstore/tap/cosign

# Verify signature
cosign verify-blob \
  --bundle harbor-offline-installer-v2.15.0.tgz.sigstore.json \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity-regexp '^https://github.com/goharbor/harbor/.github/workflows/publish_release.yml@refs/tags/v.*$' \
  harbor-offline-installer-v2.15.0.tgz
```
- *Expected output:* Verified OK

- *Full verification guide:* [docs/signature-verification.md](docs/signature-verification.md)

## OCI Distribution Conformance Tests

Check the OCI distribution conformance tests [report](https://storage.googleapis.com/harbor-conformance-test/report.html) of Harbor.

## Compatibility

The [compatibility list](https://goharbor.io/docs/edge/install-config/harbor-compatibility-list/) document provides compatibility information for the Harbor components.

* [Replication adapters](https://goharbor.io/docs/edge/install-config/harbor-compatibility-list/#replication-adapters)
* [OIDC adapters](https://goharbor.io/docs/edge/install-config/harbor-compatibility-list/#oidc-adapters)
* [Scanner adapters](https://goharbor.io/docs/edge/install-config/harbor-compatibility-list/#scanner-adapters)

## Community

* **Twitter:** [@project_harbor](https://twitter.com/project_harbor)
* **User Group:** Join Harbor user email group: [harbor-users@lists.cncf.io](https://lists.cncf.io/g/harbor-users) to get update of Harbor's news, features, releases, or to provide suggestion and feedback.
* **Developer Group:** Join Harbor developer group: [harbor-dev@lists.cncf.io](https://lists.cncf.io/g/harbor-dev) for discussion on Harbor development and contribution.
* **Slack:** Join Harbor's community for discussion and ask questions: [Cloud Native Computing Foundation](https://slack.cncf.io/), channel: [#harbor](https://cloud-native.slack.com/messages/harbor/) and [#harbor-dev](https://cloud-native.slack.com/messages/harbor-dev/)

## Demos

* **[Live Demo](https://demo.goharbor.io)** - A demo environment with the latest Harbor stable build installed. For additional information please refer to [this page](https://goharbor.io/docs/latest/install-config/demo-server/).
* **[Video Demos](https://github.com/goharbor/harbor/wiki/Video-demos-for-Harbor)** - Demos for Harbor features and continuously updated.

## Partners and Users

For a list of users, please refer to [ADOPTERS.md](ADOPTERS.md).

## Security

### Security Audit

A third party security audit was performed by Cure53 in October 2019. You can see the full report [here](https://goharbor.io/docs/2.0.0/security/Harbor_Security_Audit_Oct2019.pdf).

### Reporting security vulnerabilities

If you've found a security related issue, a vulnerability, or a potential vulnerability in Harbor, do not file a public issue. Report it privately via [GitHub private vulnerability reporting](https://github.com/goharbor/harbor/security/advisories/new): open the
[Security tab](https://github.com/goharbor/harbor/security) and click **Report a vulnerability**. The Harbor Security Team will acknowledge your report, and will follow up in the advisory
thread once we've identified the issue positively or negatively.

For
