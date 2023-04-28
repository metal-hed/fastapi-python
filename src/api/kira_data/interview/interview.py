from abc import ABCMeta, abstractmethod
from datetime import datetime

from .interface import Interview, InterviewModelInterface

class InterviewModel(InterviewModelInterface):

    def __init__(self, database) -> None:
        super().__init__()
        self.db = database

    # In reality this would do the look-up in the DB and return it
    def get_interview_by_uid(self, interview_uid: str) -> Interview:

        # @TODO - Validate data

        i = Interview(id=1, uid=interview_uid, name="My First Interview", created_on=datetime.today())
        if not i:
            # @TODO - throw error
            return None
        return i
