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

## configuration

Because meeting all the use cases only using the settings is not an option (even with [external plugins](https://docs.bunkerweb.io/1.6.14/plugins/?utm_campaign=self&utm_source=github)), you can use custom configurations to solve your specific challenges.

Under the hood, BunkerWeb uses the notorious NGINX web server, that's why you can leverage its configuration system for your specific needs. Custom NGINX configurations can be included in different [contexts](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/#contexts) like HTTP or server (all servers and/or specific server block).

Another core component of BunkerWeb is the ModSecurity Web Application Firewall: you can also use custom configurations to fix some false positives or add custom rules, for example.

## installation

<!--## BunkerWeb Cloud

<p align="center">
	<img alt="Docker banner" src="https://github.com/bunkerity/bunkerweb/raw/v1.6.14/docs/assets/img/bunkerweb-cloud.webp" />
</p>

BunkerWeb Cloud is the easiest way to get started with BunkerWeb. It offers you a fully managed BunkerWeb service with no hassle. Think of it like a BunkerWeb-as-a-Service!

You will find more information about BunkerWeb Cloud beta [here](https://www.bunkerweb.io/cloud?utm_campaign=self&utm_source=docs) and you can apply for free [in the BunkerWeb panel](https://panel.bunkerweb.io/store/bunkerweb-cloud?utm_campaign=self&utm_source=docs).
-->
