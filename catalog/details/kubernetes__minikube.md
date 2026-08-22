# kubernetes/minikube

Run Kubernetes locally

## features

minikube runs the latest stable release of Kubernetes, with support for standard Kubernetes features like:

* [LoadBalancer](https://minikube.sigs.k8s.io/docs/handbook/accessing/#loadbalancer-access) - using `minikube tunnel`
* Multi-cluster - using `minikube start -p <name>`
* [NodePorts](https://minikube.sigs.k8s.io/docs/handbook/accessing/#nodeport-access) - using `minikube service`
* [Persistent Volumes](https://minikube.sigs.k8s.io/docs/handbook/persistent_volumes/)
* [Dashboard](https://minikube.sigs.k8s.io/docs/handbook/dashboard/) - `minikube dashboard`
* [Container runtimes](https://minikube.sigs.k8s.io/docs/handbook/config/#runtime-configuration) - `minikube start --container-runtime`
* [Configure apiserver and kubelet options](https://minikube.sigs.k8s.io/docs/handbook/config/#modifying-kubernetes-defaults) via command-line flags
* Supports common [CI environments](https://github.com/minikube-ci/examples)

As well as developer-friendly features:

* [Addons](https://minikube.sigs.k8s.io/docs/handbook/deploying/#addons) - a marketplace for developers to share configurations for running services on minikube
* [NVIDIA GPU support](https://minikube.sigs.k8s.io/docs/tutorials/nvidia/) - for machine learning
* [AMD GPU support](https://minikube.sigs.k8s.io/docs/tutorials/amd/) - for machine learning
* [Filesystem mounts](https://minikube.sigs.k8s.io/docs/handbook/mount/)

**For more information, see the official [minikube website](https://minikube.sigs.k8s.io)**

## installation

See the [Getting Started Guide](https://minikube.sigs.k8s.io/docs/start/)

:mega: **Please fill out our [fast 5-question survey](https://forms.gle/Gg3hG5ZySw8c1C24A)** so that we can learn how & why you use minikube, and what improvements we should make. Thank you! :dancers:

## tools

See minikube in action in the [controls handbook](https://minikube.sigs.k8s.io/docs/handbook/controls/)
