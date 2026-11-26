from fastapi import APIRouter
from .models import User

usersRouter = APIRouter(
    prefix="/users",
    tags=["users"]
)

@usersRouter.get("/")
def delet_me():
    return {
        "200"
    }