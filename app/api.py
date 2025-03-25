import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from app.database import create_tables, delete_tables
from app.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Databases are clear")
    await create_tables()
    print("Databases are ready")
    yield
    print("Turning off")



app = FastAPI(lifespan=lifespan)
app.include_router(router)



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods="*",
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
