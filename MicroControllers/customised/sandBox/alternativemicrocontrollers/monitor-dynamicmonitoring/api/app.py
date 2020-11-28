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

@app.post("/monitoroperationd/")
def operationD(message: Message):

    message_dict = message.dict()

    # Requesting to analyser-Selfdiagnosis
    message_dict.update({"message": message.message + " from dynamic monitoring - operation D" })

    response = httpx.post(f"{url_host}/analyseroperationi", 
        headers=headers, 
        json=message_dict) 

    #updating the Knowledge

    return response.json()

@app.post("/monitoroperatione/")
def operationE(message: Message):

    message_dict = message.dict()

    # Requesting to analyser-ReliabilityEstimation
    message_dict.update({"message": message.message + " from dynamic monitoring - operation E" })

    response = httpx.post(f"{url_host}/analyseroperationk", 
        headers=headers, 
        json=message_dict) 

    #updating the Knowledge

    return response.json()

@app.post("/monitoroperationf/")
def operationF(message: Message):

    message_dict = message.dict()

    # Requesting to analyser-ReliabilityEstimation
    message_dict.update({"message": message.message + " from dynamic monitoring - operation F" })

    response = httpx.post(f"{url_host}/analyseroperationl", 
        headers=headers, 
        json=message_dict) 

    #updating the Knowledge

    return response.json()
