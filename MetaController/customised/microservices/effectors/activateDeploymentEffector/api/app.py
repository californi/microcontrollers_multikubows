from fastapi import FastAPI
import logging
from pydantic import BaseModel
from kubernetes import client, config
from kubernetes.client.rest import ApiException

app = FastAPI()


def activate_deployment(api, deployment_name, activate):
    deployment = api.read_namespaced_deployment(
        deployment_name, "default")

    if(activate):
        deployment.spec.replicas = 1
    else:
        deployment.spec.replicas = 0

    # Update the deployment
    api_response = api.patch_namespaced_deployment(
        name=deployment_name,
        namespace="default",
        body=deployment)


class DataEffector(BaseModel):
    deployment_name: str
    value: str
    dateevent: str


@app.post("/setactivatedeploymenteffector")
async def setactivatedeploymenteffector(request: DataEffector):

    try:
        config.load_incluster_config()  # de dentro do cluster K8s
        apps_v1 = client.AppsV1Api()

        activate = False
        if(request.value == "1"):
            activate = True

        activate_deployment(apps_v1, request.deployment_name, activate)

        logging.warn(request)
        return request

    except ApiException as e:
        if e.status == 404:
            return "Deployment not found: %s" % e
        else:
            return "Error unknown: %s" % e
