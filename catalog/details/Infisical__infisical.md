# Infisical/infisical

Infisical is the open-source platform for securing secrets, certificates, access, and AI Agents.

## features

### Secrets Management

Centralize your application secrets and configuration across every environment, with versioning, rotation, and leak prevention built in.

- **[Dashboard](https://infisical.com/docs/documentation/platform/project)**: Manage secrets across projects and environments (e.g. development, production, etc.) through a user-friendly interface.
- **[Secret Syncs](https://infisical.com/docs/integrations/secret-syncs/overview)**: Sync secrets to platforms like [GitHub](https://infisical.com/docs/integrations/secret-syncs/github), [Vercel](https://infisical.com/docs/integrations/secret-syncs/vercel), [AWS](https://infisical.com/docs/integrations/secret-syncs/aws-secrets-manager), and use tools like [Terraform](https://infisical.com/docs/integrations/frameworks/terraform), [Ansible](https://infisical.com/docs/integrations/platforms/ansible), and more.
- **[Secret versioning](https://infisical.com/docs/documentation/platform/secret-versioning)** and **[Point-in-Time Recovery](https://infisical.com/docs/documentation/platform/pit-recovery)**: Keep track of every secret and project state; roll back when needed.
- **[Secret Rotation](https://infisical.com/docs/documentation/platform/secret-rotation/overview)**: Rotate secrets at regular intervals for services like [PostgreSQL](https://infisical.com/docs/documentation/platform/secret-rotation/postgres-credentials), [MySQL](https://infisical.com/docs/documentation/platform/secret-rotation/mysql-credentials), [AWS IAM](https://infisical.com/docs/documentation/platform/secret-rotation/aws-iam-user-secret), and more.
- **[Dynamic Secrets](https://infisical.com/docs/documentation/platform/dynamic-secrets/overview)**: Generate ephemeral secrets on-demand for services like [PostgreSQL](https://infisical.com/docs/documentation/platform/dynamic-secrets/postgresql), [MySQL](https://infisical.com/docs/documentation/platform/dynamic-secrets/mysql), [RabbitMQ](https://infisical.com/docs/documentation/platform/dynamic-secrets/rabbit-mq), and more.
- **[Secret Sharing](https://infisical.com/docs/documentation/platform/secret-sharing)**: Share a secret with anyone through a link that expires after a set time or number of views.
- **[Infisical Kubernetes Operator](https://infisical.com/docs/documentation/guides/kubernetes-operator)**: Deliver secrets to your Kubernetes workloads and automatically reload deployments.
- **[Infisical Agent](https://infisical.com/docs/integrations/platforms/infisical-agent)**: Inject secrets into applications without modifying any code logic.
- **[Honey Tokens](https://infisical.com/docs/documentation/platform/honey-tokens/overview)**: Plant decoy credentials alongside your real secrets, and get an alert as soon as someone tries to use them.

### Secret Scanning

Find secrets that were committed to your code, and block commits that add new ones.

- **[Repository Scanning](https://infisical.com/docs/documentation/platform/secret-scanning/scan-repositories)**: Scan the full history of your [GitHub](https://infisical.com/docs/documentation/platform/secret-scanning/github), [GitLab](https://infisical.com/docs/documentation/platform/secret-scanning/gitlab), and [Bitbucket](https://infisical.com/docs/documentation/platform/secret-scanning/bitbucket) repositories and each new push, then review the [findings](https://infisical.com/docs/documentation/platform/secret-scanning/findings) in Infisical.
- **[Local Scanning](https://infisical.com/docs/documentation/platform/secret-scanning/scan-locally)**: Scan files, directories, and git history from the CLI, and install a [pre-commit hook](https://infisical.com/docs/documentation/platform/secret-scanning/pre-commit-hook) that blocks any commit containing a secret.

### Certificate Management

Issue, track, and renew X.509 certificates from internal or external CAs, and sign software artifacts.

- **[Internal CA](https://infisical.com/docs/documentation/platform/pki/ca/private-ca)**: Create and manage a private CA hierarchy

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

> **Contributing?** Check out our guide to see how to [get started](https://infisical.com/docs/contributing/getting-started/overview).

### Scan and prevent secret leaks

With the [Infisical CLI](https://infisical.com/docs/cli/overview), you can [scan for 140+ secret types](https://infisical.com/docs/documentation/platform/secret-scanning/scan-locally) in your files, directories, and git repositories.

To scan your full git history, run:

```console
infisical scan --verbose
```

To block any commit that contains a secret, install a pre-commit hook:

```console
infisical scan install --pre-commit-hook
```

To scan every push to your GitHub, GitLab, and Bitbucket repositories, see [Secret Scanning](https://infisical.com/docs/documentation/platform/secret-scanning/overview).

## Open-source vs. paid

This repo is available under the [MIT expat license](https://github.com/Infisical/infisical/blob/main/LICENSE), with the exception of the `ee` directories, which contain premium enterprise features requiring an Infisical license.

If you are interested in managed Infisical Cloud or self-hosted Enterprise Offering, take a look at [our website](https://infisical.com/) or [book a meeting with us](https://infisical.cal.com/vlad/infisical-demo).

## Security

Please do not file GitHub issues or post on our public forum for security vulnerabilities, as they are public!

Infisical takes security issues very seriously. If you have any concerns about Infisical or believe you have uncovered a vulnerability, please report it privately through our vulnerability disclosure policy at <https://infisical.com/vulnerability-disclosure>. Scope, safe harbour and disclosure terms are all set out there. See also [SECURITY.md](./SECURITY.md).

Please report any security problems to us before disclosing them publicly. For compliance documentation and security questionnaires, use security@infisical.com instead.

## Contributing

Whether it's big or small, we love contributions. Check out our guide to see how to [get started](https://infisical.com/docs/contributing/getting-started/overview).

Not sure where to get started? You can:

- Join our <a href="https://community.infisical.com/">community</a>, and ask us any questions there.

## We are hiring!

If you're reading this, there is a strong chance you like the products we created.

You might also make a great addition to our team. We're gro
