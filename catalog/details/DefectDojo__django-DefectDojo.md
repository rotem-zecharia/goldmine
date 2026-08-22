# DefectDojo/django-DefectDojo

Open-Source Unified Vulnerability Management, DevSecOps & ASPM

## installation

```sh
git clone https://github.com/DefectDojo/django-DefectDojo && cd django-DefectDojo && docker compose up
```

This quick start guide will do the following

- Clone the repository and change directories
- Start the application
- Obtain admin credentials in the initializer logs. The first initialization can take up to 3 minutes to run.


if running DefectDojo in detached mode via `docker compose up -d`, obtain admin credentials from the initializer logs with the command below. Please note, the initializer can take up to 3 minutes to run.

`docker compose logs initializer | grep "Admin password:"`

## Documentation

* [Official Docs](https://docs.defectdojo.com/)
* [REST APIs](https://docs.defectdojo.com/en/open_source/api-v2-docs/)
* [Client APIs and Wrappers](https://docs.defectdojo.com/en/open_source/api-v2-docs/#clients--api-wrappers)
* Authentication options:
    * [OAuth2/SAML2](https://docs.defectdojo.com/en/open_source/archived_docs/integrations/social-authentication/)
    * [LDAP](https://docs.defectdojo.com/en/open_source/ldap-authentication/)
* [Supported tools](https://docs.defectdojo.com/en/connecting_your_tools/parsers/)
* [How to Write Documentation Locally](/docs/README.md)
* [Development](readme-docs/DOCKER.md#run-with-docker-compose-in-development-mode-with-hot-reloading)

## Supported Installation Options

* Pro - SaaS or self-hosted (via K8s or docker compose). [Speak to our team](https://defectdojo.com/contact) or [sign-up for SaaS directly](https://cloud.defectdojo.com/accounts/onboarding/plg_step_1)
* OS - [docker compose](readme-docs/DOCKER.md)


## Community, Getting Involved, and Updates

[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/updated-dojo-chop.png" alt="Dojo" height="50"/>](https://community-defectdojo.tightknit.community/)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/slack-logo-icon.png" alt="Slack" height="50"/>](https://join.slack.com/t/defectdojocommunity/shared_invite/zt-3l9028wlf-ezDB29D_MIh9ShXdesCHZA)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/Linkedin-logo-icon-png.png" alt="LinkedIn" height="50"/>](https://www.linkedin.com/company/defectdojo)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/x_logo.jpg" alt="Twitter" height="50"/>](https://x.com/defectdojo)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/YouTube-Emblem.png" alt="Youtube" height="50"/>](https://www.youtube.com/channel/UCWw9qzqptiIvTqSqhOFuCuQ)

Checkout our new [Community Portal](https://community-defectdojo.tightknit.community/) and join the DefectDojo community on [Slack](https://join.slack.com/t/defectdojocommunity/shared_invite/zt-3l9028wlf-ezDB29D_MIh9ShXdesCHZA)! 

Follow DefectDojo on [LinkedIn](https://www.linkedin.com/company/defectdojo), [YouTube](https://www.youtube.com/channel/UCWw9qzqptiIvTqSqhOFuCuQ), and [X](https://twitter.com/defectdojo) for platform updates!

## Contributing

Please see our [contributing guidelines](readme-docs/CONTRIBUTING.md) for details and standards on contributing __before__ considering or submitting a pull request.

## Pro Edition

[Upgrade to DefectDojo Pro!](https://defectdojo.com/pricing) Pro transcends the do-it-yourself approach of open-source: A new UI, risk-based vulnerability management, incredibile scalability, API connectors, ServiceNow, GitHub, GitLab, Azure DevOps, automatic data enrichment, prioritization, and more! See all the differentiators at the bottom of our pricing page: [defectdojo.com/pricing](https://defectdojo.com/pricing).

Alternatively, for information please email hello@defectdojo.com

## About Us

DefectDojo is maintained by:
* Greg Anderson ([@devGregA](https://github.com/devgrega) | [LinkedIn](https://www.linkedin.com/in/g-anderson/))
* Matt Tesauro ([@mtesauro](https://github.com/mtesauro) | [Link
