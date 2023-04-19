from data.interview import InterviewKiraTalkDB, InterviewDataInterface


class InterviewService:
    def get_interview_data_access(self) -> InterviewDataInterface:
        # This could be more complex in selection eventually if needed
        return InterviewKiraTalkDB()

    def __init__(self) -> None:
        self.db = self.get_interview_data_access()

    def get_interview_by_uid(self, interview_uid: str):
        i = self.db.get_interview_by_uid(interview_uid)

        # ... do some business logicy stuff

        return i
