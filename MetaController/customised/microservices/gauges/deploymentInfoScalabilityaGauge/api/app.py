from fastapi import FastAPI
import logging
from pydantic import BaseModel

app = FastAPI()


class DataProbe(BaseModel):
    name: str
    type: str
    value: str
    dateevent: str


class DeploymentInfo:
    desiredReplicas = 0


@app.get("/getdeploymentinfoscalabilityagauge")
def getdeploymentinfoscalabilityagauge():
    return DeploymentInfo.desiredReplicas


@app.post("/setdeploymentinfoscalabilityagauge")
async def setdeploymentinfoscalabilityagauge(request: DataProbe):
    DeploymentInfo.desiredReplicas = request.value
    logging.warn(request)
