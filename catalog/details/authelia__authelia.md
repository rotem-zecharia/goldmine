# authelia/authelia

The Single Sign-On Multi-Factor portal for web apps. OpenID Certified™ and Post-Quantum Cryptography Ready.

## features

This is a list of the key features of Authelia:

* [OpenID Connect 1.0 / OAuth 2.0](#openid-connect-10--oauth-20)
* Post-Quantum Cryptography
* Several second factor methods:
  * **[Security Keys](https://www.authelia.com/overview/authentication/security-key/)** that support
    [FIDO2]&nbsp;[WebAuthn] with devices like a [YubiKey].
  * **[Time-based One-Time password](https://www.authelia.com/overview/authentication/one-time-password/)**
    with compatible authenticator applications.
  * **[Mobile Push Notifications](https://www.authelia.com/overview/authentication/push-notification/)**
    with [Duo](https://duo.com/).
* Passwordless Authentication via WebAuthn (Passkeys)
* Password reset with identity verification using email confirmation.
* Access restriction after too many invalid authentication attempts.
* Fine-grained access control using rules which match criteria like subdomain, user, user group membership, request uri,
 request method, and network.
* Choice between one-factor and two-factor policies per-rule.
* Support of basic authentication for endpoints protected by the one-factor policy.
* Highly available using a remote database and Redis as a highly available KV store.
* Compatible with [Traefik](https://doc.traefik.io/traefik) out of the box using the
  [ForwardAuth](https://doc.traefik.io/traefik/middlewares/http/forwardauth/) middleware.
* Curated configuration from [LinuxServer](https://www.linuxserver.io/) via their
  [SWAG](https://docs.linuxserver.io/general/swag) container as well as a
  [guide](https://blog.linuxserver.io/2020/08/26/setting-up-authelia/).
* Compatible with [Caddy] using the [forward_auth](https://caddyserver.com/docs/caddyfile/directives/forward_auth)
  directive.
* Kubernetes Support:
  * Compatible with several Kubernetes Ingress Controllers and Gateways:
    * [ingress-nginx](https://www.authelia.com/integration/kubernetes/nginx-ingress/)
    * [Traefik Kubernetes CRD](https://www.authelia.com/integration/kubernetes/traefik-ingress/#ingressroute)
    * [Traefik Kubernetes Ingress](https://www.authelia.com/integration/kubernetes/traefik-ingress/#ingress)
    * [Istio](https://www.authelia.com/integration/kubernetes/envoy/introduction/)
    * [Envoy Gateway](https://www.authelia.com/integration/kubernetes/envoy/gateway/)
  * Beta support for installing via Helm using our [Charts](https://charts.authelia.com).

For more details take a look at the [Overview](https://www.authelia.com/overview/prologue/introduction/).

If you want to know more about the roadmap, follow [Roadmap](https://www.authelia.com/roadmap).

### OpenID Connect 1.0 / OAuth 2.0

Authelia is [OpenID Certified™] to the Basic OP / Implicit OP / Hybrid OP / Form Post OP / Config OP profiles of the
[OpenID Connect™ protocol]. While this offering is still effectively
[on the roadmap as a beta](https://www.authelia.com/roadmap/active/openid-connect/) it's very comprehensive and well
implemented already, also allowing us comprehensive certification. Read more about the
[OpenID Certified™] status of Authelia in the
[OpenID Connect 1.0 Integration Guide](https://www.authelia.com/integration/openid-connect/introduction/#openid-certified).

<p align="center">
	<a href="https://www.authelia.com/integration/openid-connect/introduction/#openid-certified" target="_blank">
		<picture>
			<img src="https://www.authelia.com/images/oid-certification.jpg" width="400" title="OpenID Certified™ by Authelia to the Basic OP / Implicit OP / Hybrid OP / Form Post OP / Config OP of the OpenID Connect™ protocol">
		</picture>
	</a>
</p>

## Proxy support

Authelia works in combination with [nginx], [Traefik], [Caddy], [Skipper], [Envoy], or [HAProxy].

<p align="center">
  <img src="https://www.authelia.com/images/logos/nginx.png" height="50"/>
  <img src="https://www.authelia.com/images/logos/traefik.png" height="50"/>
  <img src="https://www.authelia.com/images/logos/caddy.png" height="50"/>
  <img src="https://www.authelia.com/images/logos/env

## installation

See the [Get Started Guide](https://www.authelia.com/integration/prologue/get-started/) or one of the curated examples
below.

### docker compose

The `docker compose` bundles act as a starting point for anyone wanting to see Authelia in action. You will have to
customize them to your needs as they come with self-signed certificates.

#### [Local](https://www.authelia.com/integration/deployment/docker/#local)
The Local compose bundle is intended to test Authelia without worrying about configuration.
It's meant to be used for scenarios where the server is not be exposed to the internet.
Domains will be defined in the local hosts file and self-signed certificates will be utilized.

#### [Lite](https://www.authelia.com/integration/deployment/docker/#lite)
The Lite compose bundle is intended for scenarios where the server will be exposed to the internet, domains and DNS will
need to be setup accordingly and certificates will be generated through LetsEncrypt. The Lite element refers to minimal
external dependencies; File based user storage, SQLite based configuration storage. In this configuration, the service
will not scale well.

## Deployment

Now that you have tested **Authelia** and you want to try it out in your own infrastructure,
you can learn how to deploy and use it with [Deployment](https://www.authelia.com/integration/deployment/introduction/).
This guide will show you how to deploy it on bare metal as well as on
[Kubernetes](https://kubernetes.io/).

## Security

Authelia takes security very seriously. If you discover a vulnerability in Authelia, please see our
[Security Policy](https://github.com/authelia/authelia/security/policy).

For more information about [security](https://www.authelia.com/policies/security/) related matters, please read
[the documentation](https://www.authelia.com/policies/security/).

## configuration

Several contact options exist for our community, the primary one being [Matrix](#matrix). These are in addition to
[GitHub issues](https://github.com/authelia/authelia/issues) for creating a
[new issue](https://github.com/authelia/authelia/issues/new/choose).

### Matrix

Community members are invited to join the [Matrix Space](https://matrix.to/#/#community:authelia.com) which includes
both the [Support Room](https://matrix.to/#/#support:authelia.com) and the
[Contributing Room](https://matrix.to/#/#contributing:authelia.com).

- The core team members are identified as administrators in the Space and individual Rooms.
- All channels are linked to [Discord](#discord).

### Discord

Community members are invited to join the [Discord Server](https://discord.authelia.com).

- The core team members are identified by the <span style="color:#BA55D3;">**CORE TEAM**</span> role in Discord.
- The [#support] and [#contributing] channels are linked to [Matrix](#matrix).

### Email

You can contact the core team by email via [team@authelia.com](mailto:team@authelia.com). Please note the
[security@authelia.com](mailto:security@authelia.com) is also available but is strictly reserved for [security] related
matters.

## Breaking changes

Since Authelia is still under active development, it is subject to breaking changes. It's recommended to pin a version
tag instead of using the `latest` tag and reading the [release notes](https://github.com/authelia/authelia/releases)
before upgrading. This is where you will find information about breaking changes and what you should do to overcome
said changes.
