import datetime
from pydantic import BaseModel, ConfigDict


#Planner Schemas



class PlanSchemaAdd(BaseModel):
    user_id: int
    plan_name: str
    date: datetime.date

class PlanSchema(PlanSchemaAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class PlanSchemaId(BaseModel):
    ok: bool = True
    plan_id: int



class GoalSchemaAdd(BaseModel):
    user_id: int
    goal_name: str
    date: datetime.date

class GoalSchema(GoalSchemaAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class GoalSchemaId(BaseModel):
    ok: bool = True
    goal_id: int



class NoteSchemaAdd(BaseModel):
    user_id: int
    note_name: str
    date: datetime.date

class NoteSchema(NoteSchemaAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class NoteSchemaId(BaseModel):
    ok: bool = True
    note_id: int
