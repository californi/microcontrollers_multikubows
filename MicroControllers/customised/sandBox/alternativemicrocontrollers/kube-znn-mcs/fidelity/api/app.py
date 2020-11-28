from fastapi import FastAPI, Request, Response
import httpx
import asyncio
from kubernetes import client, config
from starlette_exporter import PrometheusMiddleware, handle_metrics

def update_deployment(api_instance, deployment):
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name = deployment.metadata.name,
        namespace = deployment.metadata.namespace,
        body = deployment)

    return "Deployment updated. status= " + str(api_response.status)


app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)
config.load_incluster_config()
apps_v1 = client.AppsV1Api()


@app.post("/")
def hello_world():
    return "Testing prometheus"

    

@app.post("/decreaseFidelity/")
def decreaseFidelity():
    # decreaseFidelity
    deployment = apps_v1.read_namespaced_deployment("kube-znn", "default")
    # Rollout
    deployment.spec.template.spec.containers[0].image = "cmendes/znn:100k"
    status_log = update_deployment(apps_v1, deployment)

    # updating the Knowledge

    return status_log

@app.post("/increaseFidelity/")
def increaseFidelity():

    # increaseFidelity
    deployment = apps_v1.read_namespaced_deployment("kube-znn", "default")
    # Rollout
    deployment.spec.template.spec.containers[0].image = "cmendes/znn:800k"
    status_log = update_deployment(apps_v1, deployment)

    # updating the Knowledge

    return status_log    