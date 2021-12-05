

# dependencies
from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient

# Routes
from app.routers import PollRoutes


if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)

mongoClient = MongoClient()
db = mongoClient["todo-mongo-client-connection-string"]

app = FastAPI()

app.include_router(PollRoutes.router)
