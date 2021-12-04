
from typing import Optional

from fastapi import FastAPI

from models.Poll import Poll


app = FastAPI()

@app.get("/polls/{pollId}")
async def create_item(pollId: str):
    
    
    return pollId

@app.post("/polls/")
async def create_item(poll: Poll):
    
    return poll
