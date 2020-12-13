import re
from fastapi import FastAPI
import logging
import httpx
from pydantic import BaseModel
import datetime


app = FastAPI()

url_host_effectors = 'http://activatedeploymenteffector:5060'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}

# /


class DataEffector(BaseModel):
    deployment_name: str
    value: str
    dateevent: str

# request: DataEffector


class Strategy(BaseModel):
    name: str


def activateDeployment(deploymen_name, activate):
    logDatetime = str(datetime.datetime.today())
    operation = DataEffector(
        deployment_name=deploymen_name, value=activate, dateevent=logDatetime)

    response = httpx.get(
        f"{url_host_effectors}/setactivatedeploymenteffector", headers=headers, json=operation)

    return response


@app.post("/executingtactis")
async def executingtactis(request: Strategy):
    try:

        if(request.name == "NoFailureRate"):

            activateDeployment("scalabilitya", "1")
            activateDeployment("fidelitya", "1")
            activateDeployment("scalabilityb", "0")
            activateDeployment("fidelityb", "0")

            logging.warn("Effector of NoFailureRate.")

        elif (request.name == "LowFailureRate"):
            activateDeployment("scalabilitya", "0")
            activateDeployment("fidelitya", "1")
            activateDeployment("scalabilityb", "1")
            activateDeployment("fidelityb", "0")

            logging.warn("Effector of LowFailureRate.")
        else:
            activateDeployment("scalabilitya", "0")
            activateDeployment("fidelitya", "0")
            activateDeployment("scalabilityb", "1")
            activateDeployment("fidelityb", "1")

            logging.warn("Effector of HighFailureRate.")

    except httpx.RequestError as exc:
        logging.error(exc)

    return "Done"
