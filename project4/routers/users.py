from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from ..models import Todos,Users
from ..database import SessionLocal
from pydantic import BaseModel,Field
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix='/users',
    tags=['users']
)

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class UserVerification(BaseModel):
     password:str
     new_password:str = Field(min_length=6)
 




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        
# this is dependency injection
db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]

@router.get("/get_user",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return db.query(Users).filter(Users.id == user.get("user_id")).first()

@router.put("/password",status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user:user_dependency,db:db_dependency,user_verification:UserVerification):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    
    user_model = db.query(Users).filter(Users.id == user.get("user_id")).first()
    
    if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail='Error on password change')
    
    hashed_password = bcrypt_context.hash(user_verification.new_password)
    user_model.hashed_password = hashed_password
    
    db.add(user_model)
    db.commit()
    
    
@router.put("/phone_number/{phone_number}",status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(user:user_dependency,db:db_dependency,phone_number:str):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    
    user_model = db.query(Users).filter(Users.id == user.get("user_id")).first()
    
    user_model.phone_number = phone_number
    
    db.add(user_model)
    db.commit()
    