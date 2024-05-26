from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine("sqlite+aiosqlite:///app/planner.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class PlanOrm(Model):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    plan_name: Mapped[str]
    date: Mapped[str]

class GoalOrm(Model):
    __tablename__ = "goals"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    goal_name: Mapped[str]
    date: Mapped[str]

class NoteOrm(Model):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    note_name: Mapped[str]
    date: Mapped[str]
