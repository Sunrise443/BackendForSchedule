from app.model import PlanSchemaAdd, PlanSchema, GoalSchema, GoalSchemaAdd
from app.database import new_session, PlansOrm, GoalsOrm
import select

class PlanRepo:
    @classmethod
    async def add_one(cls, plan_data: PlanSchemaAdd) -> int:
        async with new_session() as session:
            plan_dict = plan_data.model_dump()

            plan = PlansOrm(**plan_dict)
            session.add(plan)
            await session.flush()
            await session.commit()
            return plan.id
    
    @classmethod
    async def find_all(cls) -> list[PlanSchema]:
        async with new_session() as session:
            query = select(PlansOrm)
            result = await session.execute(query)
            plan_models = result.scalars().all()
            plan_schemas = [PlanSchema.model_validate(plan_model) for plan_model in plan_models]
            return plan_schemas

class GoalRepo:
    @classmethod
    async def add_one(cls, goal_data: GoalSchemaAdd) -> int:
        async with new_session() as session:
            goal_dict = goal_data.model_dump()

            goal = GoalsOrm(**goal_dict)
            session.add(goal)
            await session.flush()
            await session.commit()
            return goal.id
    
    @classmethod
    async def find_all(cls) -> list[GoalSchema]:
        async with new_session() as session:
            query = select(GoalsOrm)
            result = await session.execute(query)
            goal_models = result.scalars().all()
            goal_schemas = [GoalSchema.model_validate(goal_model) for goal_model in goal_models]
            return goal_schemas
