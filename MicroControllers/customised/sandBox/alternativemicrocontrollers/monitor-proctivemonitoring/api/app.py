from fastapi import FastAPI, Request, Response
import httpx
from pydantic import BaseModel
import asyncio

class Message(BaseModel):
    id: int
    message: str

app = FastAPI()

#url_host = 'http://<service-name>:<port>'
url_host = 'http://analyser:5001'
#microcontrollers Base64    bWljcm9jb250cm9sbGVycw==
headers = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}

@app.post("/monitoroperationa/")
def operationA(message: Message):

    message_dict = message.dict()

    # Requesting to analyser-Selfdiagnosis
    message_dict.update({"message": message.message + " from proactive monitoring - operation A" })

    response = httpx.post(f"{url_host}/analyseroperationg", 
        headers=headers, 
        json=message_dict) 

    #updating the Knowledge

    return response.json()

@app.post("/monitoroperationb/")
def operationB(message: Message):

    message_dict = message.dict()

    # Requesting to analyser-Selfdiagnosis

    message_dict.update({"message": message.message + " from proactive monitoring - operation B" })

    response = httpx.post(f"{url_host}/analyseroperationh", 
        headers=headers, 
        json=message_dict) 

    #updating the Knowledge

    return response.json()    

@app.post("/monitoroperationc/")
def operationC(message: Message):

    message_dict = message.dict()

    # Requesting to analyser-ReliabilityEstimation

    message_dict.update({"message": message.message + " from proactive monitoring - operation C" })

    response = httpx.post(f"{url_host}/analyseroperationj", 
        headers=headers, 
        json=message_dict) 

    #updating the Knowledge

    return response.json()    