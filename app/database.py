import datetime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine (
    "sqlite+aiosqlite:///app/plansandgoals6777.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass


class PlansOrm(Model):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]
    plan_name: Mapped[str]
    date: Mapped[datetime.date]

class GoalsOrm(Model):
    __tablename__ = "goals"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]
    goal_name: Mapped[str]
    date: Mapped[datetime.date]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
