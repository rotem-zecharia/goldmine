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
