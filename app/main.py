from fastapi import FastAPI
from .database import Base, engine
from app.health import healthRouter
from app.users.router import usersRouter 
from app.tasks.router import tasksRouter
from app.auth.router import authRouter

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskManager")

app.include_router(healthRouter)
app.include_router(usersRouter)
app.include_router(tasksRouter)
app.include_router(authRouter)
