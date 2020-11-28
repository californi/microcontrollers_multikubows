from fastapi import FastAPI, Request, Response
import httpx
from pydantic import BaseModel
import asyncio

app = FastAPI()

#Configuration1
colTargets = {
  "M1": ["A2"]
  #"M2": ["A1", "A3"],
}


@app.post("/targets/")
def targets(origin: str):
    response = colTargets.get(origin)
      
    return response