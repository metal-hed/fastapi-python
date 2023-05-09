from kira_data.interview.interface import Interview, InterviewModelInterface
from kira_data.interview.interview import InterviewModel 

from kira_data.user_access.interface import UserAccess, UserAccessModelInterface
from kira_data.user_access.user_access import UserAccessModel

class InterviewService:
    # Set up the abstraction layer that we can switch out layer
    def get_interview_data_access(self, datasource) -> InterviewModelInterface:
        return InterviewModel(datasource) 

    def get_user_data_access(self, datasource) -> UserAccessModelInterface:
        return UserAccessModel(datasource) 

    def __init__(self, database) -> None:
        self.interview_model = self.get_interview_data_access(database)
        self.user_access_model = self.get_user_data_access(database)

    ################################################
    # Interview Business Logic
    # (Consumes our Abstraction Layer via self.model)
    ################################################
    def get_interview_by_uid(self, interview_uid: str):
        i = self.interview_model.get_interview_by_uid(interview_uid)

        # ... do some business logicy stuff

        return i


    def switch_to_interview(self, interview_uid: str):
        i = self.interview_model.get_interview_by_uid(interview_uid)
        if not i:
            # THROW 404
            pass 

        if not self.user_access_model.user_has_access(interview_uid):
            # THROW 404
            pass 

        # DO SWITCHING LOGIC

        return i