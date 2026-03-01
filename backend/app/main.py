from fastapi import FastAPI
import uvicorn

from .database import engine, Base
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

from .routers import tasks
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)