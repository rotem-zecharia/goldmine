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

## tools

* Harbor RESTful API: The APIs for most administrative operations of Harbor and can be used to perform integrations with Harbor programmatically.
  * Part 1: [New or changed APIs](https://editor.swagger.io/?url=https://raw.githubusercontent.com/goharbor/harbor/main/api/v2.0/swagger.yaml)

## installation

**System requirements:**

**On a Linux host:** docker 20.10.10-ce+ and docker-compose 1.18.0+.

Download binaries of **[Harbor release ](https://github.com/goharbor/harbor/releases)** and follow **[Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/)** to install Harbor.

If you want to deploy Harbor on Kubernetes, please use the **[Harbor chart](https://github.com/goharbor/harbor-helm)**.

Refer to the **[documentation](https://goharbor.io/docs/)** for more details on how to use Harbor.
