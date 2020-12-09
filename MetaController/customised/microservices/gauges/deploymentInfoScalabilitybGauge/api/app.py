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


@app.get("/getdeploymentinfoscalabilitybgauge")
def getdeploymentinfoscalabilitybgauge():
    return DeploymentInfo.desiredReplicas


@app.post("/setdeploymentinfoscalabilitybgauge")
async def setdeploymentinfoscalabilitybgauge(request: DataProbe):
    DeploymentInfo.desiredReplicas = request.value
    logging.warn(request)
