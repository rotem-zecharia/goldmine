# authelia/authelia

The Single Sign-On Multi-Factor portal for web apps, now OpenID Certified™

## features

This is a list of the key features of Authelia:

* [OpenID Connect 1.0 / OAuth 2.0](#openid-connect-10--oauth-20)
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

## installation

See the [Get Started Guide](https://www.authelia.com/integration/prologue/get-started/) or one of the curated examples
below.

## configuration

Several contact options exist for our community, the primary one being [Matrix](#matrix). These are in addition to
[GitHub issues](https://github.com/authelia/authelia/issues) for creating a
[new issue](https://github.com/authelia/authelia/issues/new/choose).
