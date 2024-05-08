from fastapi import FastAPI
# import connection
import database

from bson import ObjectId
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome TEo FastAPI World"}