# stakater/Reloader

A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated Deployment, StatefulSet, DaemonSet and DeploymentConfig – [✩Star] if you're usin

## features

- ✅ **Zero manual restarts**: No need to manually rollout workloads after config/secret changes.
- 🔒 **Secure by design**: Ensure your apps always use the most up-to-date credentials or tokens.
- 🛠️ **Flexible**: Works with all major workload types — Deployment, StatefulSet, Daemonset, ArgoRollout, and more.
- ⚡ **Fast feedback loop**: Ideal for CI/CD pipelines where secrets/configs change frequently.
- 🔄 **Out-of-the-box integration**: Just label your workloads and let Reloader do the rest.

## installation

Follow any of this [installation options](#-installation).

## tools

Reloader supports multiple annotation-based controls to let you **customize when and how your Kubernetes workloads are reloaded** upon changes in `Secrets` or `ConfigMaps`.

Kubernetes does not trigger pod restarts when a referenced `Secret` or `ConfigMap` is updated. Reloader bridges this gap by watching for changes and automatically performing rollouts — but it gives you full control via annotations, so you can:

- Reload **all** resources by default
- Restrict reloads to only **Secrets** or only **ConfigMaps**
- Watch only **specific resources**
- Use **opt-in via tagging** (`search` + `match`)
- Exclude workloads you don’t want to reload

## configuration

These flags let you customize Reloader's behavior globally, at the Reloader controller level.

#### 1. 🔁 Reload Behavior

| Flag | Description |
|------|-------------|
| `--reload-on-create=true` | Reload workloads when a watched ConfigMap or Secret is created |
| `--reload-on-delete=true` | Reload workloads when a watched ConfigMap or Secret is deleted |
| `--auto-reload-all=true` | Automatically reload all workloads unless opted out (`auto: "false"`) |
| `--reload-strategy=env-vars` | Strategy to use for triggering reload (`env-vars` or `annotations`) |
| `--log-format=json` | Enable JSON-formatted logs for better machine readability |

##### Reload Strategies

Reloader supports multiple strategies for triggering rolling updates when a watched `ConfigMap` or `Secret` changes. You can configure the strategy using the `--reload-strategy` flag.

| Strategy     | Description |
|--------------|-------------|
| `env-vars` (default) | Adds a dummy environment variable to any container referencing the changed resource (e.g., `Deployment`, `StatefulSet`, etc.). This forces Kubernetes to perform a rolling update. |
| `annotations` | Adds a `reloader.stakater.com/last-reloaded-from` annotation to the pod template metadata. Ideal for GitOps tools like ArgoCD, as it avoids triggering unwanted sync diffs. |

- The `env-vars` strategy is the default and works in most setups.
- The `annotations` strategy is preferred in **GitOps environments** to prevent config drift in tools like ArgoCD or Flux.
- In `annotations` mode, a `ConfigMap` or `Secret` that is deleted and re-created will still trigger a reload (since previous state is not tracked).

#### 2. 🚫 Resource Filtering

| Flag | Description |
|------|-------------|
| `--resources-to-ignore=configmaps` | Ignore ConfigMaps (only one type can be ignored at a time) |
| `--resources-to-ignore=secrets` | Ignore Secrets (cannot combine with configMaps) |
| `--ignored-workload-types=jobs,cronjobs` | Ignore specific workload types from reload monitoring |
| `--resource-label-selector=key=value` | Only watch ConfigMaps/Secrets with matching labels |

> **⚠️ Note:**
>
> Only **one** resource type can be ignored at a time.
> Trying to ignore **both `configmaps` and `secrets`** will cause an error in Reloader.
> ✅ **Workaround:** Scale the Reloader deployment to `0` replicas if you want to disable it completely.

**💡 Workload Type Examples:**

```bash
