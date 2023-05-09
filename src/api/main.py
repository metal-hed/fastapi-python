import interview.routes as interview
from fastapi import FastAPI

app = FastAPI()

app.include_router(interview.router)




 