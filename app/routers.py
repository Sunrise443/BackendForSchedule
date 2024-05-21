from typing import Annotated

from fastapi import APIRouter, Depends

from app.repository import PlanRepo, GoalRepo, NoteRepo
from app.model import PlanSchema, PlanSchemaId, PlanSchemaAdd, GoalSchema, GoalSchemaAdd, GoalSchemaId, NoteSchema, NoteSchemaAdd, NoteSchemaId, UserSchema


router = APIRouter()



#Planner



@router.post("planner/plans", tags=["planner"])
async def add_plan(plan: Annotated[PlanSchemaAdd, Depends()]) -> PlanSchemaId:
    plan_id = await PlanRepo.add_one(plan)
    return{"ok": True, "plan_id": plan_id}

@router.get("planner/plans", tags=["planner"])
async def get_plans() -> list[PlanSchema]:
    plans = await PlanRepo.find_all()
    return plans



@router.post("planner/goals", tags=["planner"])
async def add_goal(goal: Annotated[GoalSchemaAdd, Depends()]) -> GoalSchemaId:
    goal_id = await GoalRepo.add_one(goal)
    return{"ok": True, "goal_id": goal_id}

@router.get("planner/goals", tags=["planner"])
async def get_goals() -> list[GoalSchema]:
    goals = await GoalRepo.find_all()
    return goals



@router.post("planner/notes", tags=["planner"])
async def add_note(note: Annotated[NoteSchemaAdd, Depends()]) -> NoteSchemaId:
    note_id = await NoteRepo.add_one(note)
    return{"ok": True, "note_id": note_id}

@router.get("planner/notes", tags=["planner"])
async def get_notes() -> list[NoteSchema]:
    notes = await NoteRepo.find_all()
    return notes



#Authentication
