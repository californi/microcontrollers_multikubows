from fastapi import FastAPI, Request
import httpx
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    message: str

app = FastAPI()

@app.post("/analyseroperationg")
async def operationG(message: Message):

    messageReturn = {
        'id': message.id, 
        'message': message.message + ' - Message from Selfdiagnosis - Operation G'
    }

    # updating Knowledge
    return messageReturn

@app.post("/analyseroperationh")
async def operationH(message: Message):

    messageReturn = {
        'id': message.id, 
        'message': message.message + ' - Message from Selfdiagnosis - Operation H'
    }

    # updating Knowledge
    return messageReturn

@app.post("/analyseroperationi")
async def operationI(message: Message):

    messageReturn = {
        'id': message.id, 
        'message': message.message + ' - Message from Selfdiagnosis - Operation I'
    }

    # updating Knowledge
    return messageReturn
