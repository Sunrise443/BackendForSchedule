from fastapi import FastAPI


from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT


plans = [
    {
        "id": 1,
        "plan_name": "Buying apples",
    }
]


goals = [
    {
        "id": 1,
        "goal_name": "Buying a car"
    }
]


users = []


app = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello visitors!"}


@app.get("/posts", tags=["posts"])
async def get_root() -> dict:
    return {"plans_data": plans, "goals_data": goals}


@app.get("/posts/{id}", tags=["posts"])
async def get_single_post (id: int) -> dict:
    if id > len(plans):
        return {
            "error": "No such plan with the supplied ID."
        }
    
    for plan in plans:
        if plan["id"] == id:
            return {
                "plan_data": plan
            }
        

@app.post("/posts", tags=["posts"])
async def add_plan(plan: PostSchema) -> dict:
    plan.id = len(plans) + 1
    plans.append(plan.dict())
    return {
        "data": "plan added"
    }


#Registration and stuff
##DON'T FORGET TO HASH THE PASSWORDS
##Doesn't recognise Body

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False



@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
