from fastapi import APIRouter
from .models import Task

authRouter = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@authRouter.get("/")
def delet_me():
    return {
        "200"
    }