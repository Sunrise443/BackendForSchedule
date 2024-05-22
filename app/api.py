from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.database import create_tables, delete_tables
from app.routers import router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database is clear")
    await create_tables()
    print("Database is ready")
    yield
    print("Turning off")


#lkdkdkg
    
    
app = FastAPI(lifespan=lifespan)
app.include_router(router)
