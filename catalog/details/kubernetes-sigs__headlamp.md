# kubernetes-sigs/headlamp

A Kubernetes web UI that is fully-featured, user-friendly and extensible

## features

- Vendor-independent / generic Kubernetes UI
- Works in-cluster, or locally as a desktop app
- Multi-cluster
- Extensible through [plugins](https://github.com/headlamp-k8s/plugins)
- UI controls reflecting user roles (no deletion/update if not allowed)
- Clean & modern UI
- Cancellable creation/update/deletion operations
- Logs, exec, and resource editor with documentation
- Read-write / interactive (actions based on permissions)

## installation

If you want to deploy Headlamp in your cluster, check out the instructions on running it [in-cluster](https://headlamp.dev/docs/latest/installation/in-cluster/).

If you have a kubeconfig already, you can quickly try Headlamp locally as a
[desktop application](https://headlamp.dev/docs/latest/installation/desktop/)
for [Linux](https://headlamp.dev/docs/latest/installation/desktop/linux-installation),
[Mac](https://headlamp.dev/docs/latest/installation/desktop/mac-installation),
or [Windows](https://headlamp.dev/docs/latest/installation/desktop/win-installation).
**Make sure** you have a kubeconfig file set up with your favorite clusters and
in the default path so Headlamp can use it.

## limitations

If you are interested in the direction of the project, we maintain a
[Roadmap](https://github.com/orgs/headlamp-k8s/projects/1/views/1). It has the
biggest changes planned so far, as well as a [board](https://github.com/orgs/headlamp-k8s/projects/1/) tracking each release.
