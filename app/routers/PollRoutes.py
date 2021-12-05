
from fastapi import APIRouter

# Models
from app.models.Poll import Poll
from app.services.PollService import PollService
router = APIRouter()

pollService: PollService


@router.get("/polls/{pollId}", tags="polls")
async def create_item(pollId: str):

    try:
        poll = pollService.retrievePoll()
    except ValueError:
        print("Failed to retrieve poll with id {0}".format(pollId))
    return poll


@router.post("/polls/", tags="polls")
async def create_item(poll: Poll):

    try:
        createdPoll = pollService.createPoll(poll)
    except ValueError:
        print("Failed to create poll")

    return createdPoll
