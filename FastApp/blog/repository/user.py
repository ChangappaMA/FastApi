from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..schemas import User
from ..hashing import Hash
from ..models import UserModel



def create_user(db:Session, request: User):
    hashedPassword = Hash.bcrypt(request.password)
    user = UserModel(name=request.name, email=request.email, password=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(id:int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    return user