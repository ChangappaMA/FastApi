from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from ..hashing import Hash
from ..models import UserModel
from ..schemas import Login
from ..database import get_db

from .token import create_access_token


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Invalid Credentials")

    access_token = create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
