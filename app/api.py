from fastapi import FastAPI, HTTPException

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


app = FastAPI(lifespan=lifespan)
app.include_router(router)

@app.get("/notfound", status_code=404)
def notfound():
    return  {"message": "Resource Not Found"}



fake_user_db = {
    "username": "admin",
    "password": "secret"
}

@app.post("/login")
async def login(username: str, password: str):
    if username != fake_user_db["username"] or password != fake_user_db["password"]:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"message": "Login successful"}

@app.get("/error")
async def connection_error():
    raise HTTPException(status_code=102, detail="System Error(102)")