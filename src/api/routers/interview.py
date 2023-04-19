from fastapi import APIRouter
from service.interview import InterviewService
from models.interview import Interview


router = APIRouter(
    prefix="/interviews",
    tags=["interviews"]
)

service = InterviewService()


@router.get(
    "/{interview_uid}",
    summary="Search for an interview by uid",
    response_description="An interview",
    response_model=Interview
)
async def get_interview_by_uid(interview_uid: str):
    return service.get_interview_by_uid(interview_uid)
