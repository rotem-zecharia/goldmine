# aquasecurity/trivy

Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more

## tools

```bash
trivy <target> [--scanners <scanner1,scanner2>] <subject>
```

Examples:

```bash
trivy image python:3.4-alpine
```

<details>
<summary>Result</summary>

https://github.com/user-attachments/assets/af1c11e7-d9c5-48af-8e05-cb34dfd6352a

</details>

```bash
trivy fs --scanners vuln,secret,misconfig myproject/
```

<details>
<summary>Result</summary>

https://github.com/user-attachments/assets/6b3894b7-77c5-4ffc-ac94-ffe6648a30dc

</details>

```bash
trivy k8s --report summary cluster
```

<details>
<summary>Result</summary>

![k8s summary](docs/imgs/trivy-k8s.png)

</details>
