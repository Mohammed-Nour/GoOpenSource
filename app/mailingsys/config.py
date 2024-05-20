from typing import List
from pydantic import BaseModel


class MailBody(BaseModel):
    to: List[str]
    subject: str
    body: str
