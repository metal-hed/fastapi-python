from routers import interview
from fastapi import FastAPI

app = FastAPI()

app.include_router(interview.router)




