from fastapi import FastAPI, HTTPException

from contextlib import asynccontextmanager

from app.database import create_tables, delete_tables
from app.routers import router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database is clear")
    await create_tables()
    print("Database is ready")
    yield
    print("Turning off")


app = FastAPI(lifespan=lifespan)
app.include_router(router)

@app.get("/notfound", status_code=404)
def notfound():
    return  {"message": "Resource Not Found"}



fake_user_db = {
    "username": "admit",
    "password": "secret"
}

@app.post("/login")
async def login(username: str, password: str):
    if username != fake_user_db["username"] or password != fake_user_db["password"]:
        raise HTTPException(status_code=401, detail = "Incorrect username or password")
    return {"message": "Login succesful"}

@app.get("/error")
async def connection_error():
    raise HTTPException(status_code=102, detail = "System Error(102)")





#
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    }
}

security = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

def get_current_user(token: str = Depends(security)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = fake_users_db.get(token)
    if user is None:
        raise credentials_exception
    return User(**user)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or form_data.password != "password":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user["username"], "token_type": "bearer"}

@app.get("/secure_endpoint")
async def secure_endpoint(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username}