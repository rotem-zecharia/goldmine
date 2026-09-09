# kestra-io/kestra

Event Driven Orchestration & Scheduling Platform for Mission Critical Applications

## installation

### Launch on AWS (CloudFormation)

Deploy Kestra on AWS using our CloudFormation template:

[![Launch Stack](https://cdn.jsdelivr.net/gh/buildkite/cloudformation-launch-stack-button-svg@master/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://kestra-deployment-templates.s3.eu-west-3.amazonaws.com/aws/cloudformation/ec2-rds-s3/kestra-oss.yaml&stackName=kestra-oss)

### Launch on Google Cloud (Terraform deployment)

Deploy Kestra on Google Cloud Infrastructure Manager using [our Terraform module](https://github.com/kestra-io/deployment-templates/tree/main/gcp/terraform/infrastructure-manager/vm-sql-gcs).

### Get Started Locally in 5 Minutes

#### Launch Kestra in Docker

Make sure that Docker is running. Then, start Kestra in a single command:

```bash
docker run --pull=always --rm -it -p 8080:8080 --user=root \
  --name kestra \
  -v kestra_data:/app/storage \
  -v kestra_db:/app/data \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp \
  -e KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true \
  kestra/kestra:latest-slim server local
```

If you're on Windows and use PowerShell:
```powershell
docker run --pull=always --rm -it -p 8080:8080 --user=root `
  --name kestra `
  -v "kestra_data:/app/storage" `
  -v "kestra_db:/app/data" `
  -v "/var/run/docker.sock:/var/run/docker.sock" `
  -v "C:/Temp:/tmp" `
  -e KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true `
  kestra/kestra:latest-slim server local
```

If you're on Windows and use Command Prompt (CMD):
```cmd
docker run --pull=always --rm -it -p 8080:8080 --user=root ^
  --name kestra ^
  -v "kestra_data:/app/storage" ^
  -v "kestra_db:/app/data" ^
  -v "/var/run/docker.sock:/var/run/docker.sock" ^
  -v "C:/Temp:/tmp" ^
  -e KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true ^
  kestra/kestra:latest-slim server local
```

If you're on Windows and use WSL (Linux-based environment in Windows):
```bash
docker run --pull=always --rm -it -p 8080:8080 --user=root \
  --name kestra \
  -v kestra_data:/app/storage \
  -v kestra_db:/app/data \
  -v "/var/run/docker.sock:/var/run/docker.sock" \
  -v "/mnt/c/Temp:/tmp" \
  -e KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true \
  kestra/kestra:latest-slim server local
```

The `-slim` image ships without bundled plugins to keep the download small; `KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true` makes Kestra fetch each plugin from Maven Central the first time a flow needs it. Prefer everything bundled up front? Use `kestra/kestra:latest` instead and drop the environment variable.

Check our [Installation Guide](https://kestra.io/docs/installation) for other deployment options (Docker Compose, Podman, Kubernetes, AWS, GCP, Azure, and more).

Access the Kestra UI at [http://localhost:8080](http://localhost:8080) and start building your first flow!

#### Your First Hello World Flow

Create a new flow with the following content:

```yaml
id: hello_world
namespace: dev

tasks:
  - id: say_hello
    type: io.kestra.plugin.core.log.Log
    message: "Hello, World!"
```


Run the flow and see the output in the UI!

---

## 🧩 Plugin Ecosystem

Kestra's functionality is extended through a rich [ecosystem of plugins](https://kestra.io/plugins) that empower you to run tasks anywhere and code in any language, including Python, Node.js, R, Go, Shell, and more. Here's how Kestra plugins enhance your workflows:

- **Run Anywhere:**
  - **Local or Remote Execution:** Execute tasks on your local machine, remote servers via SSH, or scale out to serverless containers and cloud VMs using [Task Runners](https://kestra.io/docs/task-runners), including the AWS EC2, Azure Virtual Machine, and Google Compute Engine runners added in 2.0.
  - **Docker and Kubernetes Support:** Seamlessly run Docker containers within your workflows or launch Kubernetes jobs to handle compute-intensive workloads.

- **Code in Any Language:**
  - **Scripting Support:** Write scripts in your preferred programming language. Kestra supports Python, Node.
