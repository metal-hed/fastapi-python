from abc import ABCMeta, abstractmethod
from datetime import datetime
from pydantic import BaseModel


# This can be how we define the data for THIS API
class Interview(BaseModel):
    id: int
    uid: str
    name: str
    created_on: datetime

# Abstraction layer interface
class InterviewModelInterface(metaclass=ABCMeta):

    @abstractmethod
    async def __init__(self, datasource) -> None:
        pass

    @abstractmethod
    async def get_interview_by_uid(self, interview_uid: str) -> Interview:
        pass
