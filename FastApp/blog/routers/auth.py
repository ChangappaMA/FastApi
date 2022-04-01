from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..hashing import Hash

from ..models import UserModel
from ..schemas import Login
from ..database import get_db


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post('/')
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Invalid Credentials")

    ####generate JWT TOKEN
    
    return user
