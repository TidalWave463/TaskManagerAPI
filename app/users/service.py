from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import User
from .schemas import Registr

password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def userchecker(db: Session, username):
    ab = select(User).where(User.username == username)
    return db.scalar(ab)

class UserAlreadyExistsError(Exception):
    pass

def new_user(user_data: Registr, db:Session):
   if userchecker(db, user_data.username):
       raise UserAlreadyExistsError()
   hash_password = get_password_hash(user_data.password)

   new_user = User(**user_data.model_dump(exclude={"password"}), password=hash_password)
   
   
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   
   return new_user