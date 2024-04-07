from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import create_tables, delete_tables
from app.router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Cleared")
    await create_tables()
    print("Load completed")
    yield
    print("Reloading")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
