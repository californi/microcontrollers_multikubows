## This project uses the Kubow platform and tools provided By Carlos Mendes (i.e. https://github.com/ppgia-unifor/kubow)

## Cluster configurations

minikube start --cpus=5 --vm-driver hyperv --hyperv-virtual-switch "Primary Virtual Switch" --kubernetes-version=v1.16.10
minikube addons enable ingress

# microcontrollers_multikubows

## monitoring: 
kubectl apply -k .\tools\monitoring\

## target system - kube-znn
kubectl apply -k .\TargetSystem\kube-znn\overlay\default\

# microservices for failuremanager
kubectl apply -f .\Microcontrollers\customised\k8s

## nginxc-ingress (nginx tem que ver deopis do target system e do failuremanager)
kubectl apply -f .\tools\nginxc-ingress\

## Microcontrollers based on kubow
kubectl apply -k .\Microcontrollers\kubow_based\fidelity_microcontroller\kubow\overlay\kube-znn\
kubectl apply -k .\Microcontrollers\kubow_based\scalability_microcontroller\kubow\overlay\kube-znn\

## MetaController - kubow - TODO:  defining the components with respect to Deployments and services
kubectl apply -k .\MetaController\kubow\overlay\kube-znn\


## Performing testing
kubectl apply -k .\Testing\k6\

## Generating logs

kubectl logs pod/metacontroller-kubow-bd8d4db79-zjlhg >> arquivo29112020.log

## Updating PowerShell terminal

while (1) {clear; kubectl get all; sleep 5}
while (1) {clear; kubectl describe deployment kube-znn; sleep 5}


# To analyse event failures for a specific pod
kubectl describe pod kube-znn-644ff8f5d6-59r9n

# query prometheus in K8s

kubectl port-forward pod/prometheus-d4499d495-rh2rt 9090:9090

# Grafana

 kubectl port-forward pod/grafana-b659fcdd9-8r9h5 3000:3000