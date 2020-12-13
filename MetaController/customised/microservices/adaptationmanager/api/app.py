from fastapi import FastAPI
import logging
import httpx
from pydantic import BaseModel

app = FastAPI()

url_host_modelmanagerknowledge = 'http://modelmanagerknowledge:5071'
url_host_strategyexecutor = 'http://stratetyexecutor:5091'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


class Strategy(BaseModel):
    name: str


def executingStrategy(s):
    strategy = Strategy(name=s)
    response = httpx.post(
        f"{url_host_strategyexecutor}/executingtactis", headers=headers, json=strategy)


@app.post("/findingstrategy")
async def findingStrategy():
    try:
        # retrieving knowledge
        response = httpx.get(
            f"{url_host_modelmanagerknowledge}/getknowledge", headers=headers)
        currentKnowledge = response.json()

        cpuFailureRate = float(currentKnowledge[0]["property_value"])

        if (cpuFailureRate == 0.0):
            executingStrategy("NoFailureRate")
            logging.warn("Tactic of NoFailureRate")

        elif (cpuFailureRate > 0.0 and cpuFailureRate <= 0.5):
            executingStrategy("LowFailureRate")
            logging.warn("Tactic of LowFailureRate")

        else:
            executingStrategy("HighFailureRate")
            logging.warn("Tactic of HighFailureRate")

    except httpx.RequestError as exc:
        logging.error(exc)

    return "Done"
