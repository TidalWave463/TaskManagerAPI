from fastapi import APIRouter
from .models import Task

usersRouter = APIRouter(
    prefix="/users",
    tags=["users"]
)

@usersRouter.get("/")
def delet_me():
    return {
        "200"
    }