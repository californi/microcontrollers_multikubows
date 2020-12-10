from fastapi import FastAPI
import logging
import time
import httpx

app = FastAPI()

url_host_modelmanagerknowledge = 'http://modelmanagerknowledge:5071'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


@app.post("/findingStrategy")
async def findingStrategy():
    try:
        # retrieving knowledge
        response = httpx.get(
            f"{url_host_modelmanagerknowledge}/getknowledge", headers=headers)
        currentKnowledge = response.json()

        cpuFailureRate = float(currentKnowledge[0]["property_value"])

        if (cpuFailureRate == 0.0):
            logging.warn("Tactic of NoFailureRate")
            pass
        elif (cpuFailureRate > 0.0 and cpuFailureRate <= 0.5):
            logging.warn("Tactic of LowFailureRate")
            pass
        else:
            logging.warn("Tactic of HighFailureRate")
            pass

    except httpx.RequestError as exc:
        logging.error(exc)

    return "Done"
