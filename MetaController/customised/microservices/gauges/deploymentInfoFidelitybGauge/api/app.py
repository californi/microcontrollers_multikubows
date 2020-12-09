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


@app.get("/getdeploymentinfofidelitybgauge")
def getdeploymentinfofidelitybgauge():
    return DeploymentInfo.desiredReplicas


@app.post("/setdeploymentinfofidelitybgauge")
async def setdeploymentinfofidelitybgauge(request: DataProbe):
    DeploymentInfo.desiredReplicas = request.value
    logging.warn(request)
