# casdoor/casdoor

An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI supporting OpenClaw, MCP, OAuth, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, 

## features

Casdoor is a **complete identity provider**, not an authentication proxy and not a library you embed. It stores your users, issues the tokens, and gives you an admin console to manage all of it — so your applications can delegate login entirely and never handle a password themselves.

- **One server, many protocols.** The same user directory is reachable over OAuth 2.0, OIDC, SAML 2.0, CAS, LDAP and SCIM, so a modern SPA and a legacy CAS-only app can share one set of accounts.
- **Everything is editable in the UI.** Organizations, applications, providers, sign-in methods, email and SMS templates, and login-page branding are configured in the web console instead of in files you have to redeploy.
- **Policy-based authorization built in.** Access rules are expressed with [Casbin](https://casbin.org/) — ACL, RBAC, ABAC and custom models — rather than a fixed permission scheme.
- **Straightforward to self-host.** A single Go binary plus a database. No JVM, no operator, no cluster required.

If all you need is a login screen in front of an existing reverse proxy, a smaller tool may suit you better. Casdoor is for when you want to own the user directory itself.

## installation

Four supported paths, fastest first. All of them end up at <http://localhost:8000>.
