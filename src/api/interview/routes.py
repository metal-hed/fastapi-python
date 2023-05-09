from fastapi import APIRouter, Body
from kira_data.interview.interview import Interview 

from .service import InterviewService

router = APIRouter(
    prefix="/interview",
    tags=["interviews"] 
)
####################################
# /interview/details/ID
####################################
@router.get(
    "/details",
    summary="View details about an interview by id",
    response_description="An interview",
    response_model=Interview
)
async def get_interview_by_uid(interview_id: str = Body(...)):
    with Database() as database:
        service = InterviewService(database)
        return service.get_interview_by_uid(interview_id)

####################################
# /interview/switch
####################################
@router.get(
    "/switch",
    summary="Switch to active interview by id",
    response_description="An interview",
    response_model=Interview
)
async def switch_to_interview(interview_id: str = Body(...)):
    with Database() as database:
        service = InterviewService(database)
        return service.switch_to_interview(interview_id)