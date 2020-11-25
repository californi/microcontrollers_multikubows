
## Before of all, create a virtual network "Primary Virtual Switch" in hyperv
## Creating a cluster in Windows 10 with hyperv. Note that is necessary to do this when using features docker in dev machine
minikube start --cpus=3 --vm-driver hyperv --hyperv-virtual-switch "Primary Virtual Switch" --kubernetes-version=v1.16.10

## Enabling the ingress to use DNS - Minikube
minikube addons enable ingress
