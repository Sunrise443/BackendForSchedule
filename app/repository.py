from app.model import PlanSchemaAdd
from database import new_session, PlansOrm
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
    async def find_all(cls):
        async with new_session() as session:
            query = select(PlansOrm)
            result = await session.execute(query)
            plan_models = result.scalars().all()
            return plan_models
