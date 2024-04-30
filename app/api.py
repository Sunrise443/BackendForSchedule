from fastapi import FastAPI, Body
from contextlib import asynccontextmanager

from app.database import create_tables
from app.model import UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.routers import router

#Само приложение

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Database is ready.")
    yield
    print("Turning off.")


app = FastAPI(lifespan=lifespan)
app.include_router(router)

#Registration and stuff
##DON'T FORGET TO HASH THE PASSWORDS
##CHANGE ERROR MESSAGES TO CODES (http cats)
##MOVE USERS (plans included) FROM TEMP STORAGE TO A DATABASE

users = []

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema = Body(...)):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False



@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
