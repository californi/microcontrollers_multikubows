from fastapi import FastAPI
import logging
from pydantic import BaseModel


app = FastAPI()


class DataKnowledge(BaseModel):
    CpuFailureRate: str
    scalabilityaDesiredReplicas: str
    fidelityaDesiredReplicas: str
    scalabilitybDesiredReplicas: str
    fidelitybDesiredReplicas: str
    datelastevent: str


data = DataKnowledge()


@app.get("/getknowledge")
def getknowledge():
    return data


@app.post("/setknowledge")
async def setknowledge(request: DataKnowledge):
    data = request
    logging.warn(data)
