from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session
from ..schemas import UserDetails, User
from ..repository import user
from ..models import UserModel
from ..database import get_db



router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post('/', response_model=UserDetails)
def create_users(request: User, db: Session = Depends(get_db)):
    return user.create_user(db, request)


@router.get('/{id}', response_model=UserDetails)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)