from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Generator
from .schemas import Registr, RegistrResponse
from ..database import engine
from . import service

usersRouter = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db() -> Generator[Session, None, None]:
  with Session(engine) as session:
    yield session

@usersRouter.post("/register", response_model=RegistrResponse)
def register_new_user(user_data: Registr, db: Session = Depends(get_db)):
    try:
       return service.new_user(db=db, user_data=user_data)
    except service.UserAlreadyExistsError as e:
       return HTTPException(status_code=409, detail="Пользователь уже существует")
       
