from sqlalchemy import select

from app.database import GoalOrm, NoteOrm, new_session, PlanOrm
from app.model import GoalSchemaAdd, GoalSchema, NoteSchemaAdd, NoteSchema, PlanSchemaAdd, PlanSchema


class PlanRepo:
    @classmethod
    async def add_one(cls, plan_data: PlanSchemaAdd) -> int:
        async with new_session() as session:
            plan_dict = plan_data.model_dump()

            plan = PlanOrm(**plan_dict)
            session.add(plan)
            await session.flush()
            await session.commit()
            return plan.id
        
    @classmethod
    async def find_all(cls) -> list[PlanSchema]:
        async with new_session() as session:
            query = select(PlanOrm)
            result = await session.execute(query)
            plan_models = result.scalars().all()
            plan_schemas = [PlanSchema.model_validate(plan_model) for plan_model in plan_models]
            return plan_schemas


class GoalRepo:
    @classmethod
    async def add_one(cls, goal_data: GoalSchemaAdd) -> int:
        async with new_session() as session:
            goal_dict = goal_data.model_dump()

            goal = GoalOrm(**goal_dict)
            session.add(goal)
            await session.flush()
            await session.commit()
            return goal.id
        
    @classmethod
    async def find_all(cls) -> list[GoalSchema]:
        async with new_session() as session:
            query = select(GoalOrm)
            result = await session.execute(query)
            goal_models = result.scalars().all()
            goal_schemas = [GoalSchema.model_validate(goal_model) for goal_model in goal_models]
            return goal_schemas


class NoteRepo:
    @classmethod
    async def add_one(cls, note_data: NoteSchemaAdd) -> int:
        async with new_session() as session:
            note_dict = note_data.model_dump()

            note = NoteOrm(**note_dict)
            session.add(note)
            await session.flush()
            await session.commit()
            return note.id
        
    @classmethod
    async def find_all(cls) -> list[NoteSchema]:
        async with new_session() as session:
            query = select(NoteOrm)
            result = await session.execute(query)
            note_models = result.scalars().all()
            note_schemas = [NoteSchema.model_validate(note_model) for note_model in note_models]
            return note_schemas
