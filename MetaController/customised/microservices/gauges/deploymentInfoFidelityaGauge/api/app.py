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


@app.get("/getdeploymentinfofidelityagauge")
def getdeploymentinfofidelityagauge():
    return DeploymentInfo.desiredReplicas


@app.post("/setdeploymentinfofidelityagauge")
async def setdeploymentinfofidelityagauge(request: DataProbe):
    DeploymentInfo.desiredReplicas = request.value
    logging.warn(request)
