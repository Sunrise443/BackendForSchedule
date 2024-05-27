from fastapi import FastAPI, HTTPException

from contextlib import asynccontextmanager

from app.database import create_tables, delete_tables
from app.routers import router

from app.database_users import create_tables_users, delete_tables_users



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

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

#users = []
#здесь как раз нужно соединение с базой данных
@app.post("/registr")
async def register(user:User):
    if user.username in [user.usernamefor user in users]: #Рит,это мы сравниваем, существует ли это имя уже в базе данных.
        raise HTTPException(status_code=400, detail="Username already exists")
    users.append(user)#dobavili usera v basu dannih
    return{"message": "User registered successfully"}



from passlib.context import CryptContext

pwd_context = CryptContext(schemes = [bcrypt], deprecated = "auto")
app = FastApi()

def get_pwd_hash(password):
    return pwd_context.hash(password)
 #password = "random12345" #пример использования 
 #hash_pwd = get_pwd_hash(password)
 #print(hash_pwd)
  
def verify_password(plain_pwd, hash_pwd): #проверка пароля 
    return pwd_context.verify(plain_pwd, hash_pwd)
