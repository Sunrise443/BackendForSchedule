from fastapi import APIRouter, Depends
from typing import Annotated

from app.repository import PlanRepo, GoalRepo
from app.model import PlanSchema, PlanSchemaAdd, GoalSchema, GoalSchemaAdd
from app.auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/planner")


@router.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello visitors!"}

#Plans and goals (The planner. Needs to be linked with the date somehow)

@router.get("", tags=["planner"])
async def get_all() -> PlanSchema:
    plans = await PlanRepo.find_all()
    goals = await GoalRepo.find_all()
    return {"plans_data": plans, "goals_data": goals}
        

@router.post("/plans", dependencies=[Depends(JWTBearer())], tags=["planner"])
async def add_plan(plan: Annotated[PlanSchemaAdd, Depends()]) -> PlanSchema:
    plan.id = await PlanRepo.add_one(plan)
    return {"data": "plan added", "plan_id": plan.id}

@router.post("/goals", dependencies=[Depends(JWTBearer())], tags=["planner"])
async def add_goal(goal: Annotated[GoalSchemaAdd, Depends()]) -> GoalSchema:
    goal.id = await GoalRepo.add_one(goal)
    return {"data": "goal added", "goal_id": goal.id}
