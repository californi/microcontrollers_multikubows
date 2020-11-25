from fastapi import FastAPI, Request, Response
import httpx
import asyncio
from kubernetes import client, config

app = FastAPI()

def update_deployment(api_instance, deployment):
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name = deployment.metadata.name,
        namespace = deployment.metadata.namespace,
        body = deployment)

    return "Deployment updated. status= " + str(api_response.status)


app = FastAPI()
config.load_incluster_config()
apps_v1 = client.AppsV1Api()

@app.post("/decreaseScalability/")
def decreaseScalability():

    # decreaseFidelity
    deployment = apps_v1.read_namespaced_deployment("kube-znn", "default")
    # scale down
    deployment.spec.replicas = deployment.spec.replicas - 1
    status_log = update_deployment(apps_v1, deployment)

    # updating the Knowledge

    return status_log

@app.post("/increaseScalability/")
def increaseScalability():

    # increaseScalability
    deployment = apps_v1.read_namespaced_deployment("kube-znn", "default")
    # scale down
    deployment.spec.replicas = deployment.spec.replicas + 1
    status_log = update_deployment(apps_v1, deployment)

    # updating the Knowledge

    return status_log