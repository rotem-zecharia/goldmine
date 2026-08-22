# k8sgpt-ai/k8sgpt

Giving Kubernetes Superpowers to everyone

## installation

### Linux/Mac via brew

```sh
brew install k8sgpt
```

or

```sh
brew tap k8sgpt-ai/k8sgpt
brew install k8sgpt
```

<details>
  <summary>RPM-based installation (RedHat/CentOS/Fedora)</summary>

**32 bit:**

  <!---x-release-please-start-version-->

  ```
  sudo rpm -ivh https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.4.36/k8sgpt_386.rpm
  ```
  <!---x-release-please-end-->

**64 bit:**

  <!---x-release-please-start-version-->
  ```
  sudo rpm -ivh https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.4.36/k8sgpt_amd64.rpm
  ```
  <!---x-release-please-end-->
</details>

<details>
  <summary>DEB-based installation (Ubuntu/Debian)</summary>

**32 bit:**

  <!---x-release-please-start-version-->

```
curl -LO https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.4.36/k8sgpt_386.deb
sudo dpkg -i k8sgpt_386.deb
```

  <!---x-release-please-end-->

**64 bit:**

  <!---x-release-please-start-version-->

```
curl -LO https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.4.36/k8sgpt_amd64.deb
sudo dpkg -i k8sgpt_amd64.deb
```

  <!---x-release-please-end-->
</details>

<details>

  <summary>APK-based installation (Alpine)</summary>

**32 bit:**

  <!---x-release-please-start-version-->
  ```
  wget https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.4.36/k8sgpt_386.apk
  apk add --allow-untrusted k8sgpt_386.apk
  ```
  <!---x-release-please-end-->

**64 bit:**

  <!---x-release-please-start-version-->
  ```
  wget https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.4.36/k8sgpt_amd64.apk
  apk add --allow-untrusted k8sgpt_amd64.apk
  ```
  <!---x-release-please-end-->
</details>

<details>
  <summary>Failing Installation on WSL or Linux (missing gcc)</summary>
  When installing Homebrew on WSL or Linux, you may encounter the following error:

```
==> Installing k8sgpt from k8sgpt-ai/k8sgpt Error: The following formula cannot be installed from a bottle and must be
built from the source. k8sgpt Install Clang or run brew install gcc.
```

If you install gcc as suggested, the problem will persist. Therefore, you need to install the build-essential package.

```
   sudo apt-get update
   sudo apt-get install build-essential
```

</details>

### Windows

- Download the latest Windows binaries of **k8sgpt** from the [Release](https://github.com/k8sgpt-ai/k8sgpt/releases)
  tab based on your system architecture.
- Extract the downloaded package to your desired location. Configure the system _PATH_ environment variable with the binary location

## Operator Installation

To install within a Kubernetes cluster please use our `k8sgpt-operator` with installation instructions available [here](https://github.com/k8sgpt-ai/k8sgpt-operator)

_This mode of operation is ideal for continuous monitoring of your cluster and can integrate with your existing monitoring such as Prometheus and Alertmanager._

## Quick Start

- Currently, the default AI provider is OpenAI, you will need to generate an API key from [OpenAI](https://openai.com)
  - You can do this by running `k8sgpt generate` to open a browser link to generate it
- Run `k8sgpt auth add` to set it in k8sgpt.
  - You can provide the password directly using the `--password` flag.
- Run `k8sgpt filters` to manage the active filters used by the analyzer. By default, all filters are executed during analysis.
- Run `k8sgpt analyze` to run a scan.
- And use `k8sgpt analyze --explain` to get a more detailed explanation of the issues.
- You also run `k8sgpt analyze --with-doc` (with or without the explain flag) to get the official documentation from Kubernetes.

# Using with Claude Desktop

K8sGPT can be integrated with Claude Desktop to provide AI-powered Kubernetes cluster analysis. This integration requires K8sGPT v0.4.14 or later.

## requirements

1. Install K8sGPT v0.4.14 or later:
   ```sh
   brew install k8sgpt
   ```

2. Install Claude Desktop from the official website

3. Configure K8sGPT with your preferred AI backend:
   ```sh
   k8sgpt auth
   ```

## tools

Once connected, you can use Claude Desktop to:
- Analyze your Kubernetes cluster
- Get detailed insights about cluster health
- Receive recommendations for fixing issues
- Query cluster information

Example commands in Claude Desktop:
- "Analyze my Kubernetes cluster"
- "What's the health status of my cluster?"
- "Show me any issues in the default namespace"

## Troubleshooting

If you encounter connection issues:
1. Ensure K8sGPT is running with the MCP server enabled
2. Verify your Kubernetes cluster is accessible
3. Check that your AI backend is properly configured
4. Restart both K8sGPT and Claude Desktop

For more information, visit our [documentation](https://docs.k8sgpt.ai).

## Analyzers

K8sGPT uses analyzers to triage and diagnose issues in your cluster. It has a set of analyzers that are built in, but
you will be able to write your own analyzers.

### Built in analyzers

#### Enabled by default

- [x] podAnalyzer
- [x] pvcAnalyzer
- [x] rsAnalyzer
- [x] serviceAnalyzer
- [x] eventAnalyzer
- [x] ingressAnalyzer
- [x] statefulSetAnalyzer
- [x] deploymentAnalyzer
- [x] jobAnalyzer
- [x] cronJobAnalyzer
- [x] nodeAnalyzer
- [x] mutatingWebhookAnalyzer
- [x] validatingWebhookAnalyzer
- [x] configMapAnalyzer

#### Optional

- [x] hpaAnalyzer
- [x] pdbAnalyzer
- [x] networkPolicyAnalyzer
- [x] gatewayClass
- [x] gateway
- [x] httproute
- [x] logAnalyzer
- [x] storageAnalyzer
- [x] securityAnalyzer
- [x] CatalogSource
- [x] ClusterCatalog
- [x] ClusterExtension
- [x] ClusterService
- [x] ClusterServiceVersion
- [x] OperatorGroup
- [x] InstallPlan
- [x] Subscription

## Examples

_Run a scan with the default analyzers_

```
k8sgpt generate
k8sgpt auth add
k8sgpt analyze --explain
k8sgpt analyze --explain --with-doc
```

_Filter on resource_

```
k8sgpt analyze --explain --filter=Service
```

_Filter by namespace_

```
k8sgpt analyze --explain --filter=Pod --namespace=default
```

_Output to JSON_

```
k8sgpt analyze --explain --filter=Service --output=json
```

_Anonymize during explain_

```
k8sgpt analyze --explain --filter=Service --output=json --anonymize
```

<details>
<summary> Using filters </summary>

_List filters_

```
k8sgpt filters list
```

_Add default filters_

```
k8sgpt filters add [filter(s)]
```

### Examples :

- Simple filter : `k8sgpt filters add Service`
- Multiple filters : `k8sgpt filters add Ingress,Pod`

_Remove default filters_

```
k8sgpt filters remove [filter(s)]
```

### Examples :

- Simple filter : `k8sgpt filters remove Service`
- Multiple filters : `k8sgpt filters remove Ingress,Pod`

</details>

<details>

<summary> Additional commands </summary>

_List configured backends_

```
k8sgpt auth list
```

_Update configured backends_

```
k8sgpt auth update $MY_BACKEND1,$MY_BACKEND2..
```

_Remove configured backends_

```
k8sgpt auth remove -b $MY_BACKEND1,$MY_BACKEND2..
```

_List integrations_

```
k8sgpt integrations list
```

_Activate integrations_

```
k8sgpt integrations activate [integration(s)]
```

_Use integration_

```
k8sgpt analyze --filter=[integration(s)]
```

_Deactivate integrations_

```
k8sgpt integrations deactivate [integration(s)]
```

_Serve mode_

```
k8sgpt serve
```

_Serve mode with MCP (Model Context Protocol)_

```
# Enable MCP server on default port 8089
k8sgpt serve --mcp --mcp-http

# Enable MCP server on custom port
k8sgpt serve --mcp --mcp-http --mcp-port 8089

# Full serve mode with MCP
k8sgpt serve --mcp --mcp-http --port 8080 --metrics-port 8081 --mcp-port 8089
```

The MCP server enables integration with tools like Claude Desktop and other MCP-compatible clients. It runs on port 8089 by default and provides:
- Kubernetes cluster analysis via MCP protocol
- Resource information and health status
- AI-powered issue explanations and recommendations

For Helm chart deployment with MCP support, see the `charts/k8sgpt/values-mcp-example.yaml` file.

_Analysis with serve mode_

```
grpcurl -plaintext -d '{"namespace": "k8sgpt", "explain" : "true"}' localhost:80

## features

<details>

With this option, the data is anonymized before being sent to the AI Backend. During the analysis execution, `k8sgpt` retrieves sensitive data (Kubernetes object names, labels, etc.). This data is masked when sent to the AI backend and replaced by a key that can be used to de-anonymize the data when the solution is returned to the user.

<summary> Anonymization </summary>

1. Error reported during analysis:

```bash
Error: HorizontalPodAutoscaler uses StatefulSet/fake-deployment as ScaleTargetRef which does not exist.
```

2. Payload sent to the AI backend:

```bash
Error: HorizontalPodAutoscaler uses StatefulSet/tGLcCRcHa1Ce5Rs as ScaleTargetRef which does not exist.
```

3. Payload returned by the AI:

```bash
The Kubernetes system is trying to scale a StatefulSet named tGLcCRcHa1Ce5Rs using the HorizontalPodAutoscaler, but it cannot find the StatefulSet. The solution is to verify that the StatefulSet name is spelled correctly and exists in the same namespace as the HorizontalPodAutoscaler.
```

4. Payload returned to the user:

```bash
The Kubernetes system is trying to scale a StatefulSet named fake-deployment using the HorizontalPodAutoscaler, but it cannot find the StatefulSet. The solution is to verify that the StatefulSet name is spelled correctly and exists in the same namespace as the HorizontalPodAutoscaler.
```

### Further Details

Note: **Anonymization does not currently apply to events.**

_In a few analysers like Pod, we feed to the AI backend the event messages which are not known beforehand thus we are not masking them for the **time being**._

- The following is the list of analysers in which data is **being masked**:-

  - Statefulset
  - Service
  - PodDisruptionBudget
  - Node
  - NetworkPolicy
  - Ingress
  - HPA
  - Deployment
  - Cronjob

- The following is the list of analysers in which data is **not being masked**:-

  - ReplicaSet
  - PersistentVolumeClaim
  - Pod
  - Log
  - **_\*Events_**

**\*Note**:

- k8gpt will not mask the above analysers because they do not send any identifying information except **Events** analyser.
- Masking for **Events** analyzer is scheduled in the near future as seen in this [issue](https://github.com/k8sgpt-ai/k8sgpt/issues/560). _Further research has to be made to understand the patterns and be able to mask the sensitive parts of an event like pod name, namespace etc._

- The following is the list of fields which are not **being masked**:-

  - Describe
  - ObjectStatus
  - Replicas
  - ContainerStatus
  - **_\*Event Message_**
  - ReplicaStatus
  - Count (Pod)

**\*Note**:

- It is quite possible the payload of the event message might have something like "super-secret-project-pod-X crashed" which we don't currently redact _(scheduled in the near future as seen in this [issue](https://github.com/k8sgpt-ai/k8sgpt/issues/560))_.

### Proceed with care

- The K8gpt team recommends using an entirely different backend **(a local model) in critical production environments**. By using a local model, you can rest assured that everything stays within your DMZ, and nothing is leaked.
- If there is any uncertainty about the possibility of sending data to a public LLM (open AI, Azure AI) and it poses a risk to business-critical operations, then, in such cases, the use of public LLM should be avoided based on personal assessment and the jurisdiction of risks involved.

</details>

<details>
<summary> Configuration management</summary>

`k8sgpt` stores config data in the `$XDG_CONFIG_HOME/k8sgpt/k8sgpt.yaml` file. The data is stored in plain text, including your OpenAI key.

Config file locations:
| OS | Path |
| ------- | ------------------------------------------------ |
| MacOS | ~/Library/Application Support/k8sgpt/k8sgpt.yaml |
| Linux | ~/.config/k8sgpt/k8sgpt.yaml |
| Windows | %LOCALAPPDATA%/k8sgpt/k8sgpt.yaml |

</details>

<details>
There may be scenarios where caching remotely is preferred.
In these scenarios K8sGPT supports AWS S3 or Azure Blob storage Integ
