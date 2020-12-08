from fastapi import FastAPI
import logging
from pydantic import BaseModel

app = FastAPI()


class DataProbe(BaseModel):
    name: str
    type: str
    value: str
    dateevent: str


class CpuFailure:
    rate = 0.0


@app.get("/getcpufailuregauge")
def getcpufailuregauge():
    return CpuFailure.rate


@app.post("/setcpufailuregauge")
async def setcpufailuregauge(request: DataProbe):
    CpuFailure.rate = request.value
    logging.warn(request)
