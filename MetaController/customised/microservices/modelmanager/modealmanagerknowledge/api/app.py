from fastapi import FastAPI
import logging
from model import DataKnowledge
import knowledge_db
import sqlite3

app = FastAPI()

knowledge_db.loadInitialKnowledge()


@app.post("/setknowledge")
async def setknowledge(request: DataKnowledge):
    knowledge_db.updateDataKnowledge(request)
    logging.warn(request)
    return "Done"


@app.get("/getknowledge")
def getknowledge():
    return knowledge_db.getAllComponents()
