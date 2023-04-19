from pydantic import BaseModel
from datetime import datetime


# This can be how we define the data for THIS API
class Interview(BaseModel):
    id: int
    uid: str
    name: str
    created_on: datetime
