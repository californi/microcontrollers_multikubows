from fastapi import FastAPI, Request
import httpx
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    message: str

app = FastAPI()


@app.post("/analyseroperationj")
async def operationJ(message: Message):

    messageReturn = {
        'id': message.id, 
        'message': message.message + ' - Message from Selfdiagnosis - Operation J'
    }

    # updating Knowledge
    return messageReturn

@app.post("/analyseroperationk")
async def operationK(message: Message):

    messageReturn = {
        'id': message.id, 
        'message': message.message + ' - Message from Selfdiagnosis - Operation K'
    }

    # updating Knowledge
    return messageReturn

@app.post("/analyseroperationl")
async def operationL(message: Message):

    messageReturn = {
        'id': message.id, 
        'message': message.message + ' - Message from Selfdiagnosis - Operation L'
    }

    # updating Knowledge
    return messageReturn
