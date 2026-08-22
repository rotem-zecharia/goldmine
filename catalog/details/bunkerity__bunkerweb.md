# bunkerity/bunkerweb

🛡️ Open-source and cloud-native Web Application Firewall (WAF)

## features

https://github.com/user-attachments/assets/c3fed740-28d8-4335-ab05-113a9e815b4f

- **Easy integration into existing environments**: Seamlessly integrate BunkerWeb into various environments such as Linux, Docker, Swarm, Kubernetes, and more. Enjoy a smooth transition and hassle-free implementation.
- **Highly customizable**: Tailor BunkerWeb to your specific requirements with ease. Enable, disable, and configure features effortlessly, allowing you to customize the security settings according to your unique use case.
- **Secure by default**: BunkerWeb provides out-of-the-box, hassle-free minimal security for your web services. Experience peace of mind and enhanced protection right from the start.
- **Awesome web UI**: Take control of BunkerWeb more efficiently with the exceptional web user interface (UI). Navigate settings and configurations effortlessly through a user-friendly graphical interface, eliminating the need for the command-line interface (CLI).
- **Plugin system**: Extend the capabilities of BunkerWeb to meet your own use cases. Seamlessly integrate additional security measures and customize the functionality of BunkerWeb according to your specific requirements.
- **Free as in "freedom"**: BunkerWeb is licensed under the free [AGPLv3 license](https://www.gnu.org/licenses/agpl-3.0.en.html), embracing the principles of freedom and openness. Enjoy the freedom to use, modify, and distribute the software, backed by a supportive community.
- **Professional services**: Get technical support, tailored consulting, and custom development directly from the maintainers of BunkerWeb. Visit the [Bunker Panel](https://panel.bunkerweb.io/?utm_campaign=self&utm_source=github) for more information.

## Security features

A non-exhaustive list of security features:

- **HTTPS** support with transparent **Let's Encrypt** automation
- **State-of-the-art web security**: HTTP security headers, prevent leaks, TLS hardening, ...
- Integrated **ModSecurity WAF** with the **OWASP Core Rule Set**
- **Automatic ban** of strange behaviors based on HTTP status codes
- Apply **connection and request limits** for clients
- **Block bots** by asking them to solve a **challenge** (e.g., cookie, JavaScript, captcha, hCaptcha, or reCAPTCHA)
- **Block known bad IPs** with external blacklists and DNSBL
- And much more...

Learn more about the core security features in the [security tuning](https://docs.bunkerweb.io/1.6.14/advanced/?utm_campaign=self&utm_source=github#security-tuning) section of the documentation.

## Demo

https://github.com/user-attachments/assets/6fc0e3c1-d353-4a84-bad0-15bf9b6623a5

A demo website protected with BunkerWeb is available at [demo.bunkerweb.io](https://demo.bunkerweb.io/?utm_campaign=self&utm_source=github). Feel free to visit it and perform some security tests.

## Web UI

https://github.com/user-attachments/assets/a3ed56f8-c124-4ca9-b8b3-4be0913b3078

BunkerWeb offers an optional [user interface](web-ui.md) to manage your instances and their configurations. An online read-only demo is available at [demo-ui.bunkerweb.io](https://demo-ui.bunkerweb.io/?utm_campaign=self&utm_source=doc), feel free to test it yourself.

## BunkerWeb Cloud

Don't want to self-host and manage your own BunkerWeb instance(s)? You might be interested in BunkerWeb Cloud, our fully managed SaaS offering for BunkerWeb.

Order your [BunkerWeb Cloud instance](https://panel.bunkerweb.io/store/bunkerweb-cloud?utm_campaign=self&utm_source=doc) and get access to:

- A fully managed BunkerWeb instance hosted in our cloud
- All BunkerWeb features, including PRO ones
- A monitoring platform with dashboards and alerts
- Technical support to assist you with configuration

If you are interested in the BunkerWeb Cloud offering, don't hesitate to [contact us](https://panel.bunkerweb.io/contact.php?utm_campaign=self&utm_source=doc) so we can discuss your needs.

## PRO version

Want to quickly test BunkerWeb PRO for one month? Use the code `freetrial` when placing y

## configuration

Because meeting all the use cases only using the settings is not an option (even with [external plugins](https://docs.bunkerweb.io/1.6.14/plugins/?utm_campaign=self&utm_source=github)), you can use custom configurations to solve your specific challenges.

Under the hood, BunkerWeb uses the notorious NGINX web server, that's why you can leverage its configuration system for your specific needs. Custom NGINX configurations can be included in different [contexts](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/#contexts) like HTTP or server (all servers and/or specific server block).

Another core component of BunkerWeb is the ModSecurity Web Application Firewall: you can also use custom configurations to fix some false positives or add custom rules, for example.

## Database

<p align="center">
	<img alt="Database model" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/bunkerweb_db.svg" />
</p>

The state of the current configuration of BunkerWeb is stored in a backend database which contains the following data:

- Settings defined for all the services
- Custom configurations
- BunkerWeb instances
- Metadata about job execution
- Cached files

The following backend databases are supported: SQLite, MariaDB, MySQL, and PostgreSQL.

## Scheduler

To make things automagically work together, a dedicated service called the scheduler is in charge of:

- Storing the settings and custom configurations inside the database
- Executing various tasks (called jobs)
- Generating a configuration which is understood by BunkerWeb
- Being the intermediary for other services (like web UI or autoconf)

In other words, the scheduler is the brain of BunkerWeb.

## installation

<!--## BunkerWeb Cloud

<p align="center">
	<img alt="Docker banner" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/bunkerweb-cloud.webp" />
</p>

BunkerWeb Cloud is the easiest way to get started with BunkerWeb. It offers you a fully managed BunkerWeb service with no hassle. Think of it like a BunkerWeb-as-a-Service!

You will find more information about BunkerWeb Cloud beta [here](https://www.bunkerweb.io/cloud?utm_campaign=self&utm_source=docs) and you can apply for free [in the BunkerWeb panel](https://panel.bunkerweb.io/store/bunkerweb-cloud?utm_campaign=self&utm_source=docs).
-->
## Linux

<p align="center">
	<img alt="Linux banner" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/integration-linux.svg" />
</p>

List of supported Linux distros:

- Debian 12 "Bookworm"
- Debian 13 "Trixie"
- Ubuntu 22.04 "Jammy"
- Ubuntu 24.04 "Noble"
- Ubuntu 26.04 "Resolute Raccoon"
- Fedora 43
- Fedora 44
- RHEL, CentOS, Rocky Linux and AlmaLinux 8, 9 and 10

You will find more information in the [Linux section](https://docs.bunkerweb.io/1.5.10/integrations/?utm_campaign=self&utm_source=github#linux) of the documentation.

## Docker

<p align="center">
	<img alt="Docker banner" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/integration-docker.svg" />
</p>

We provide ready-to-use prebuilt images for x64, x86, armv7, and arm64 platforms on [Docker Hub](https://hub.docker.com/u/bunkerity).

Docker integration key concepts are:

- **Environment variables** to configure BunkerWeb
- **Scheduler** container to store configuration and execute jobs
- **Networks** to expose ports for clients and connect to upstream web services

You will find more information in the [Docker integration section](https://docs.bunkerweb.io/1.6.14/integrations/?utm_campaign=self&utm_source=github#docker) of the documentation.

## Docker autoconf

<p align="center">
	<img alt="Docker autoconf banner" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/integration-autoconf.svg" />
</p>

The downside of using environment variables is that the container needs to be recreated each time there is an update, which is not very convenient. To counter that issue, you can use another image called **autoconf** which will listen for Docker events and automatically reconfigure BunkerWeb in real-time without recreating the container.

Instead of defining environment variables for the BunkerWeb container, you simply add **labels** to your web applications containers and the **autoconf** will "automagically" take care of the rest.

You will find more information in the [Docker autoconf section](https://docs.bunkerweb.io/1.6.14/integrations/?utm_campaign=self&utm_source=github#docker-autoconf) of the documentation.

## Kubernetes

<p align="center">
	<img alt="Kubernetes banner" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/integration-kubernetes.svg" />
</p>

The autoconf acts as an [Ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) and will configure the BunkerWeb instances according to the [Ingress resources](https://kubernetes.io/docs/concepts/services-networking/ingress/). It also monitors other Kubernetes objects like [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) for custom configurations.

The official [Helm chart](https://helm.sh/) for BunkerWeb is available in the [bunkerity/bunkerweb-helm repository](https://github.com/bunkerity/bunkerweb-helm).

You will find more information in the [Kubernetes section](https://docs.bunkerweb.io/1.6.14/integrations/?utm_campaign=self&utm_source=github#kubernetes) of the documentation.

## Microsoft Azure

<p align="center">
	<img alt="Azure banner" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/integration-azure.webp" />
</p>

BunkerWeb is referenced in the [Azure Marketplace](https://azuremarketplace.microsoft.com/fr-fr/ma
