from fastapi import FastAPI
import uvicorn

from .database import engine, Base
from . import models
from app.routes.tasks import router as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello world"}

app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)