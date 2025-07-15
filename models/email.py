from pydantic import BaseModel

class Email(BaseModel):
    id: int
    to: str
    subject: str
    body: str
