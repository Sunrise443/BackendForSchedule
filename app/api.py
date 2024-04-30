from typing import Annotated
from fastapi import FastAPI, Body, Depends
from contextlib import asynccontextmanager


from app.database import create_tables
from app.model import GoalSchema, PlanSchemaAdd, UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer
from app.repository import PlanRepo


#Базы данных требуется заменить

plans = [
    {
        "id": 1,
        "plan_name": "Buying apples",
    }
]


goals = [
    {
        "id": 1,
        "goal_name": "Buying a car"
    }
]


users = []

#Само приложение


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Database is ready.")
    yield
    print("Turning off.")


app = FastAPI(lifespan=lifespan)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello visitors!"}


#Plans and goals (The planner. Needs to be linked with the date somehow)


@app.get("/planner", tags=["planner"])
async def get_root() -> dict:
    return {"plans_data": plans, "goals_data": goals}
        

@app.post("/planner_plans", tags=["planner"])
async def add_plan(plan: Annotated[PlanSchemaAdd, Depends()]):
    plan.id = await PlanRepo.add_one(plan)
    return {"data": "plan added", "plan_id": plan.id}

@app.post("/planner_goals", dependencies=[Depends(JWTBearer())], tags=["planner"])
async def add_goal(goal: GoalSchema) -> dict:
    goal.id = len(goals) + 1
    plans.append(goal.dict())
    return {
        "data": "goal added"
    }



#Registration and stuff
##DON'T FORGET TO HASH THE PASSWORDS
##CHANGE ERROR MESSAGES TO CODES (http cats)
##MOVE USERS (plans included) FROM TEMP STORAGE TO A DATABASE
##ROUTERS FOR UPDATING AND DELETING TASKS

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
