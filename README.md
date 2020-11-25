## This project uses the Kubow platform and tools provided By Carlos Mendes (i.e. https://github.com/ppgia-unifor/kubow)

## Cluster configurations

minikube start --cpus=5 --vm-driver hyperv --hyperv-virtual-switch "Primary Virtual Switch" --kubernetes-version=v1.16.10
minikube addons enable ingress

# microcontrollers_multikubows

## monitoring: 
kubectl apply -k .\tools\monitoring\

## target system - kube-znn
kubectl apply -k .\TargetSystem\kube-znn\overlay\default\

## nginxc-ingress
kubectl apply -f .\tools\nginxc-ingress\

## Microcontrollers based on kubow
kubectl apply -k .\Microcontrollers\kubow_based\fidelity_microcontroller\kubow\overlay\kube-znn\
kubectl apply -k .\Microcontrollers\kubow_based\scalability_microcontroller\kubow\overlay\kube-znn\

## MetaController - kubow - TODO:  defining the components with respect to Deployments and services
kubectl apply -k .\MetaController\kubow\overlay\kube-znn\


## customised Microcontrollers
kubectl apply -f .\Microcontrollers\customised\k8s\kube-znn-microcontrollers.yaml


## Performing testing
kubectl apply -k .\Testing\k6\

## Generating logs

kubectl logs pod/metacontroller-kubow-84c9b6ff8d-4nhnb >> arquivo23112020.log

## Updating PowerShell terminal

while (1) {clear; kubectl get all; sleep 5}
while (1) {clear; kubectl describe deployment kube-znn; sleep 5}


# To analyse event failures for a specific pod
kubectl describe pod kube-znn-644ff8f5d6-59r9n

