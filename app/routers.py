from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.database import UserOrm
from app.repository import PlanRepo, GoalRepo, NoteRepo, UserRepo
from app.model import PlanSchema, PlanSchemaId, PlanSchemaAdd, GoalSchema, GoalSchemaAdd, GoalSchemaId, NoteSchema, NoteSchemaAdd, NoteSchemaId, UserSchema


router = APIRouter()



#Planner


@router.post("/planner/plans", tags=["planner"])
async def add_plan(plan: Annotated[PlanSchemaAdd, Depends()]) -> PlanSchemaId:
    plan_id = await PlanRepo.add_one(plan)
    return{"ok": True, "plan_id": plan_id}

@router.get("/planner/plans", tags=["planner"])
async def get_plans() -> list[PlanSchema]:
    plans = await PlanRepo.find_all()
    return plans



@router.post("/planner/goals", tags=["planner"])
async def add_goal(goal: Annotated[GoalSchemaAdd, Depends()]) -> GoalSchemaId:
    goal_id = await GoalRepo.add_one(goal)
    return{"ok": True, "goal_id": goal_id}

@router.get("/planner/goals", tags=["planner"])
async def get_goals() -> list[GoalSchema]:
    goals = await GoalRepo.find_all()
    return goals



@router.post("/planner/notes", tags=["planner"])
async def add_note(note: Annotated[NoteSchemaAdd, Depends()]) -> NoteSchemaId:
    note_id = await NoteRepo.add_one(note)
    return{"ok": True, "note_id": note_id}

@router.get("/planner/notes", tags=["planner"])
async def get_notes() -> list[NoteSchema]:
    notes = await NoteRepo.find_all()
    return notes



#Authentication


@router.post("/registr", tags=["user"])
async def register(user: Annotated[UserSchema, Depends()]) -> str:
    if UserOrm.name in UserOrm:
        raise HTTPException(status_code=400, detail="Username already exists")
    await UserRepo.add_one(user)
    return{"message": "User registered successfully"}


@router.post("/login", tags=["user"])
async def login(username: str, password: str):
    if username != UserOrm.name or password != UserOrm.password:
        raise HTTPException(status_code=401, detail = "Incorrect username or password")
    return {"message": "Login succesful"}

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def get_pwd_hash(password):
    return pwd_context.hash(password)
 #password = "random12345" #пример использования 
 #hash_pwd = get_pwd_hash(password)
 #print(hash_pwd)
  
def verify_password(plain_pwd, hash_pwd): #проверка пароля 
    return pwd_context.verify(plain_pwd, hash_pwd)


security = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(security)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = UserOrm.get(token)
    if user is None:
        raise credentials_exception
    return UserSchema(**user)

@router.post("/token", tags=["user"])
async def login1(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserOrm.get(form_data.name)
    if not user or form_data.password != "password":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user["username"], "token_type": "bearer"}

@router.get("/secure_endpoint", tags=["user"])
async def secure_endpoint(current_user: UserSchema = Depends(get_current_user)):
    return {"username": current_user.username}



#Errors


@router.get("/notfound", status_code=404, tags=["errors"])
def not_found():
    return  {"message": "Resource Not Found"}

@router.get("/error", tags=["errors"])
async def connection_error():
    raise HTTPException(status_code=102, detail = "System Error(102)")
