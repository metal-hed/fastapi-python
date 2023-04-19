from models.interview import Interview

from abc import ABCMeta, abstractmethod
from datetime import datetime


class InterviewDataInterface(metaclass=ABCMeta):
    @abstractmethod
    async def get_interview_by_uid(self, interview_uid: str) -> Interview:
        pass


# This is one implementation
class InterviewKiraTalkDB(InterviewDataInterface):
    # In reality this would do the look-up in the DB and return it
    def get_interview_by_uid(self, interview_uid: str) -> Interview:
        i = Interview(id=1, uid=interview_uid, name="My First Interview", created_on=datetime.today())

        return i


# A second implementation
class InterviewCleanModelsDB(InterviewDataInterface):
    async def get_interview_by_uid(self, interview_uid: str) -> Interview:
        pass


# A third implementation, this will not work on instantiation as it does not adhere to the contract
class InterviewBrokenImplementation(InterviewDataInterface):
    async def get_interview_by_uid(self, interview_uid: str, another_parameter) -> Interview:
        pass
