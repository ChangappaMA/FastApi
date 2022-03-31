import imp
from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session
from ..schemas import UserDetails, User
from ..hashing import Hash
from ..models import UserModel
from ..database import get_db



router = APIRouter()

@router.post('/users', response_model=UserDetails, tags=["User"])
def create_users(request: User, db: Session = Depends(get_db)):
    hashedPassword = Hash.bcrypt(request.password)
    user = UserModel(name=request.name, email=request.email, password=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get('/user/{id}', response_model=UserDetails, tags=["User"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    return user