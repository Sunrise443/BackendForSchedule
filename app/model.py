from pydantic import BaseModel, Field, EmailStr

#Posts (plans, goals and stuff)

class PostSchema(BaseModel):
    id: int = Field (default=None)
    task_name: str = Field (...)
    

    class Config:
        schema_extra = {
            "example": {
                "task_name": "Cleaning the house"
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
