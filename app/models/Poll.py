from pydantic import BaseModel
from typing import List, Optional

from .ResponsePolicy import ResponsePolicy

class Poll(BaseModel):
    id: Optional[str]
    title: str
    options: List[str]
    allowMultipleAnswers: bool
    botPrevention: bool
    responsePolicy: ResponsePolicy
