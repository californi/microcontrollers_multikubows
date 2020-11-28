
from logging import exception
from fastapi import FastAPI, Depends
from configdb import MONGODB_DB_NAME
from mongodb import close_mongo_connection, connect_to_mongo, get_nosql_db, AsyncIOMotorClient
import pymongo
import logging
from pydantic import BaseModel

app = FastAPI()


class RegisterRequest(BaseModel):
    id: int
    content: str


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    try:
        await db.create_collection("failures")
        failures_collection = db.failures
    except pymongo.errors.CollectionInvalid as e:
        logging.info(e)
        pass


@app.post("/create")
async def create_failure(request: RegisterRequest, client: AsyncIOMotorClient = Depends(get_nosql_db)):
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
