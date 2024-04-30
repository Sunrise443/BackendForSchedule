from pydantic import BaseModel, Field, EmailStr, ConfigDict

#Plans and goals

class PlanSchemaAdd(BaseModel):
    user_id: int = Field (default=None)
    plan_name: str = Field (...)
    date: int = Field (...)

    class Config:
        schema_extra = {
            "example": {
                "plan_name": "Cleaning the house"
            }
        }

class PlanSchema(PlanSchemaAdd):
    id: int = Field (default=None)
    user_id: int = Field (default=None)
    plan_name: str = Field (...)
    date: int = Field (...)

    class Config:
        schema_extra = {
            "example": {
                "plan_name": "Cleaning the house"
            }
        }


class GoalSchema(BaseModel):
    id: int = Field (default=None)
    user_id: int = Field (default=None)
    goal_name: str = Field (...)
    date: int = Field (...)

    class Config:
        schema_extra = {
            "example": {
                "goal_name": "Buying a car"
            }
        }

class GoalSchemaAdd(BaseModel):
    user_id: int = Field (default=None)
    goal_name: str = Field (...)
    date: int = Field (...)

    class Config:
        schema_extra = {
            "example": {
                "goal_name": "Buying a car"
            }
        }


#Registration and stuff

class UserSchema(BaseModel):
    nickname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "nickname": "Sunny",
                "email": "sunny@gmail.com",
                "password": "1234"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "sunny@gmail.com",
                "password": "1234"
            }
        }


#Users

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str

class UserPrivate(User):
    hashed_password: str
