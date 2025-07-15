from pydantic import BaseModel

class Push(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
