from fastapi import FastAPI
from app.dao import UsersDAO
from app.db import engine, Base


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



@app.get('/')
async def home():
    try:
        s = await UsersDAO.add(
            username="username",
            email="email",
            password="password"
        )
    except Exception:
        s = await UsersDAO.find_one_or_none(
            username="username",
            email="email",
            password="password"
        )
        return {
            'username': s.username,
            'email': s.email,
            'password': s.password
        }
