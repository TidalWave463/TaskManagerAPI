from fastapi import FastAPI
from app.health import healthRouter

app = FastAPI(title="TaskManager")

app.include_router(healthRouter)