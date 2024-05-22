from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Basic(declarative_base):
    pass

class User(Basic):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)

engine = create_engine('sqlite:///users.db', echo=True)  


Session = sessionmaker(bind=engine)
session = Session()

async def create_tables_users():
    async with engine.begin() as conn:
        await conn.run_sync(Basic.metadata.create_all)

async def delete_tables_users():
    async with engine.begin() as conn:
        await conn.run_sync(Basic.metadata.drop_all)
