# comet-ml/opik

Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards.

## installation

Install the Python SDK and configure it:

```bash
pip install opik
opik configure
```

Wrap any function with the `@track` decorator to start logging traces:

```python
from opik import track

@track
def my_function(input: str) -> str:
    return input
```

Every call to `my_function` is now logged to Opik, including nested calls, so this works for full agent and pipeline traces, not just single LLM calls. See the [Quickstart guide](https://www.comet.com/docs/opik/quickstart?from=llm&utm_source=opik&utm_medium=github&utm_content=quickstart_hero_link&utm_campaign=opik) for the TypeScript SDK and other setup options.

<br>

<a id="-how-opik-compares"></a>

## configuration

./opik.sh --help
```

Use the `--help` or `--info` options to troubleshoot issues. Dockerfiles now ensure containers run as non-root users for enhanced security. Once all is up and running, you can now visit [localhost:5173](http://localhost:5173) on your browser! For detailed instructions, see the [Local Deployment Guide](https://www.comet.com/docs/opik/self-host/local_deployment?from=llm&utm_source=opik&utm_medium=github&utm_content=self_host_link&utm_campaign=opik).

#### Self-Hosting with Kubernetes & Helm (for Scalable Deployments)

For production or larger-scale self-hosted deployments, Opik can be installed on a Kubernetes cluster using our Helm chart. Click the badge for the full [Kubernetes Installation Guide using Helm](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik).

[![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326ce5.svg?&logo=kubernetes&logoColor=white)](https://www.comet.com/docs/opik/self-host/kubernetes/#kubernetes-installation?from=llm&utm_source=opik&utm_medium=github&utm_content=kubernetes_link&utm_campaign=opik)

<a id="-opik-client-sdk"></a>
