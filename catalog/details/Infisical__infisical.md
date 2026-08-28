# Infisical/infisical

Infisical is the open-source platform for secrets, certificates, and privileged access management.

## features

### Secrets Management:

Centralize your application secrets and configuration across every environment, with versioning, rotation, and leak prevention built in.

- **[Dashboard](https://infisical.com/docs/documentation/platform/project)**: Manage secrets across projects and environments (e.g. development, production, etc.) through a user-friendly interface.
- **[Secret Syncs](https://infisical.com/docs/integrations/secret-syncs/overview)**: Sync secrets to platforms like [GitHub](https://infisical.com/docs/integrations/cicd/githubactions), [Vercel](https://infisical.com/docs/integrations/cloud/vercel), [AWS](https://infisical.com/docs/integrations/cloud/aws-secret-manager), and use tools like [Terraform](https://infisical.com/docs/integrations/frameworks/terraform), [Ansible](https://infisical.com/docs/integrations/platforms/ansible), and more.
- **[Secret versioning](https://infisical.com/docs/documentation/platform/secret-versioning)** and **[Point-in-Time Recovery](https://infisical.com/docs/documentation/platform/pit-recovery)**: Keep track of every secret and project state; roll back when needed.
- **[Secret Rotation](https://infisical.com/docs/documentation/platform/secret-rotation/overview)**: Rotate secrets at regular intervals for services like [PostgreSQL](https://infisical.com/docs/documentation/platform/secret-rotation/postgres-credentials), [MySQL](https://infisical.com/docs/documentation/platform/secret-rotation/mysql), [AWS IAM](https://infisical.com/docs/documentation/platform/secret-rotation/aws-iam-user-secret), and more.
- **[Dynamic Secrets](https://infisical.com/docs/documentation/platform/dynamic-secrets/overview)**: Generate ephemeral secrets on-demand for services like [PostgreSQL](https://infisical.com/docs/documentation/platform/dynamic-secrets/postgresql), [MySQL](https://infisical.com/docs/documentation/platform/dynamic-secrets/mysql), [RabbitMQ](https://infisical.com/docs/documentation/platform/dynamic-secrets/rabbit-mq), and more.
- **[Secret Scanning and Leak Prevention](https://infisical.com/docs/cli/scanning-overview)**: Prevent secrets from leaking to git.
- **[Infisical Kubernetes Operator](https://infisical.com/docs/documentation/guides/kubernetes-operator)**: Deliver secrets to your Kubernetes workloads and automatically reload deployments.
- **[Infisical Agent](https://infisical.com/docs/integrations/platforms/infisical-agent)**: Inject secrets into applications without modifying any code logic.
- **[Honey Tokens](https://infisical.com/docs/documentation/platform/honey-tokens/overview)**: Plant decoy credentials alongside your real secrets that act as tripwires, instantly alerting your team the moment an attacker tries to use them.
- **[Agent Vault](https://github.com/Infisical/agent-vault)**: Broker AI agent access to external APIs so agents never hold real credentials. Outbound requests route through a proxy that injects secrets before forwarding, eliminating credential exfiltration risk from prompt injection.

### Certificate Management

Run a complete private PKI: issue, manage, and monitor X.509 certificates from a centralized platform.

- **[Internal CA](https://infisical.com/docs/documentation/platform/pki/ca/private-ca)**: Create and manage a private
  CA hierarchy directly within Infisical.
- **[External CA](https://infisical.com/docs/documentation/platform/pki/ca/external-ca)**: Integrate with third-party certificate authorities such as Let’s Encrypt, DigiCert, Microsoft AD CS, and more to leverage existing PKI infrastructure
  or issue publicly trusted certificates.
- **[Certificate Lifecycle Management](https://infisical.com/docs/documentation/platform/pki/applications/certificates)**: Create certificate [profiles](https://infisical.com/docs/documentation/platform/pki/settings/profiles) and [policies](https://infisical.com/docs/documentation/platform/pki/settings/policies) to control how certificates are issued, including [enrollment methods](https://infisical.com/docs/documen

## installation

Check out the [Quickstart Guides](https://infisical.com/docs/documentation/getting-started/overview)

| Use Infisical Cloud                                                                                                                                     | Deploy Infisical on premise                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| The fastest and most reliable way to <br> get started with Infisical is signing up <br> for free to [Infisical Cloud](https://app.infisical.com/login). | <br> View all [deployment options](https://infisical.com/docs/self-hosting/overview) <br><br> Already self-hosting? Plan version upgrades with the [Infisical Upgrade Tool](https://upgrade.infisical.com/). |

### Run Infisical locally

To set up and run Infisical locally, make sure you have [Git](https://git-scm.com/downloads) and [Docker](https://www.docker.com/get-started/) installed on your system.

**Linux/macOS:**

```console
git clone https://github.com/Infisical/infisical && cd "$(basename $_ .git)" && cp .env.example .env && docker compose -f docker-compose.prod.yml up
```

**Windows (Command Prompt):**

```console
git clone https://github.com/Infisical/infisical && cd infisical && copy .env.example .env && docker compose -f docker-compose.prod.yml up
```

Once running, create an account at [http://localhost:80](http://localhost:80).

> **Contributing?** Check out our guide to see how to [get started](https://infisical.com/docs/contributing/getting-started).

### Scan and prevent secret leaks

On top of managing secrets with Infisical, you can also [scan for over 140+ secret types](https://infisical.com/docs/cli/scanning-overview) in your files, directories and git repositories.

To scan your full git history, run:

```
infisical scan --verbose
```

Install pre commit hook to scan each commit before you push to your repository

```
infisical scan install --pre-commit-hook
```

Learn about Infisical's code scanning feature [here](https://infisical.com/docs/cli/scanning-overview)

## Open-source vs. paid

This repo available under the [MIT expat license](https://github.com/Infisical/infisical/blob/main/LICENSE), with the exception of the `ee` directory which will contain premium enterprise features requiring a Infisical license.

If you are interested in managed Infisical Cloud of self-hosted Enterprise Offering, take a look at [our website](https://infisical.com/) or [book a meeting with us](https://infisical.cal.com/vlad/infisical-demo).

## Security

Please do not file GitHub issues or post on our public forum for security vulnerabilities, as they are public!

Infisical takes security issues very seriously. If you have any concerns about Infisical or believe you have uncovered a vulnerability, please report it privately through our vulnerability disclosure policy at <https://infisical.com/vulnerability-disclosure>. Scope, safe harbour and disclosure terms are all set out there. See also [SECURITY.md](./SECURITY.md).

Please report any security problems to us before disclosing them publicly. For compliance documentation and security questionnaires, use security@infisical.com instead.

## Contributing

Whether it's big or small, we love contributions. Check out our guide to see how to [get started](https://infisical.com/docs/contributing/getting-started).

Not sure where to get started? You can:

- Join our <a href="https://infisical.com/slack">Slack</a>, and ask us any questions there.

## We are hiring!

If you're reading this, there is a strong chance you like the products we created.

You might also make a great addition to our team. We're growing fast and would love for you to [join us](https://infisical.com/careers).
