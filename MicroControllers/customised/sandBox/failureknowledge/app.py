from prometheus_fastapi_instrumentator import Instrumentator
from logging import exception
from fastapi import FastAPI, Depends
from configdb import MONGODB_DB_NAME
from mongodb import close_mongo_connection, connect_to_mongo, get_nosql_db, AsyncIOMotorClient
import pymongo
import logging
from pydantic import BaseModel


app = FastAPI()
Instrumentator().instrument(app).expose(app)


class CreateRequest(BaseModel):
    id: int
    content: str


@app.get("/hello")
def hello_world(request: CreateRequest):
    return "Hello"


@app.post("/create")
async def create_failure(request: CreateRequest, client: AsyncIOMotorClient = Depends(get_nosql_db)):
    try:
        db = client[MONGODB_DB_NAME]
        collection = db.failures

        failure = {}
        failure["id"] = request.id
        failure["content"] = request.content
        response = await collection.insert_one(failure)

        return {"id_inserted": str(response.inserted_id)}
    except exception as e:
        return {"error": e}


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
