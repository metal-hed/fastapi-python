from abc import ABCMeta, abstractmethod
from datetime import datetime

from .interface import UserAccess, UserAccessModelInterface

class UserAccessModel(UserAccessModelInterface):

    def __init__(self, database) -> None:
        super().__init__()
        self.db = database

    # In reality this would do the look-up in the DB and return it
    def user_has_access(self, interview_uid: str) -> UserAccess:

        # @TODO - See if user has access to the interview

        i = UserAccess(id=1, uid=interview_uid, name="My First Interview", created_on=datetime.today())
        if not i:
            # @TODO - throw error
            return None
        return i
