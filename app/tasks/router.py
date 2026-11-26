from fastapi import APIRouter
from .models import Task

tasksRouter = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@tasksRouter.get("/")
def delet_me():
    return {
        "200"
    }