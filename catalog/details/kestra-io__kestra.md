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
docker run --pull=always -it -p 8080:8080 --user=root \
  --name kestra --restart=always \
  -v kestra_data:/app/storage \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp \
  kestra/kestra:latest server local
```

If you're on Windows and use PowerShell:
```powershell
docker run --pull=always -it -p 8080:8080 --user=root `
  --name kestra --restart=always `
  -v "kestra_data:/app/storage" `
  -v "/var/run/docker.sock:/var/run/docker.sock" `
  -v "C:/Temp:/tmp" `
  kestra/kestra:latest server local
```

If you're on Windows and use Command Prompt (CMD):
```cmd
docker run --pull=always -it -p 8080:8080 --user=root ^
  --name kestra --restart=always ^
  -v "kestra_data:/app/storage" ^
  -v "/var/run/docker.sock:/var/run/docker.sock" ^
  -v "C:/Temp:/tmp" ^
  kestra/kestra:latest server local
```

If you're on Windows and use WSL (Linux-based environment in Windows):
```bash
docker run --pull=always -it -p 8080:8080 --user=root \
  --name kestra --restart=always \
  -v kestra_data:/app/storage \
  -v "/var/run/docker.sock:/var/run/docker.sock" \
  -v "/mnt/c/Temp:/tmp" \
  kestra/kestra:latest server local
```

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
  - **Local or Remote Execution:** Execute tasks on your local machine, remote servers via SSH, or scale out to serverless containers using [Task Runners](https://kestra.io/docs/task-runners).
  - **Docker and Kubernetes Support:** Seamlessly run Docker containers within your workflows or launch Kubernetes jobs to handle compute-intensive workloads.

- **Code in Any Language:**
  - **Scripting Support:** Write scripts in your preferred programming language. Kestra supports Python, Node.js, R, Go, Shell, and others, allowing you to integrate existing codebases and deployment patterns.
  - **Flexible Automation:** Execute shell commands, run SQL queries against various databases, and make HTTP requests to interact with APIs.

- **Event-Driven and Real-Time Processing:**
  - **Real-Time Triggers:** React to events from external systems in real-time, such as file arrivals, new messages in message buses (Kafka, Redis, Pulsar, AMQP, MQTT, NATS, AWS SQS, Google Pub/Sub, Azure Event Hubs), and more.
  - **Custom Events:** Define custom events to trigger flows based on specific conditions or external signals, enabling highly responsive workflows.

- **Cloud Integrations:**

