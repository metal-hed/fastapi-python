from abc import ABCMeta, abstractmethod
from datetime import datetime
from pydantic import BaseModel


# This can be how we define the data for THIS API
class UserAccess(BaseModel):
    id: int
    user_id: str
    permission: str
    has_access: str
    created_on: datetime

# Abstraction layer interface
class UserAccessModelInterface(metaclass=ABCMeta):

    @abstractmethod
    async def __init__(self, datasource) -> None:
        pass

    @abstractmethod
    async def user_has_access(self, interview_uid: str) -> UserAccess:
        pass
