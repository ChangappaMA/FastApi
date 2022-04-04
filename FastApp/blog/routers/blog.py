from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from .oauth2 import get_current_user
from ..schemas import ShowBlog, Blog, User
from ..models import BlogModel
from ..database import get_db
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/', response_model=List[ShowBlog])
def get_all_blog(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_blogs(db)

@router.get('/{id}', status_code=200, response_model=ShowBlog)
def get_a_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_blog(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.create_blogs(db, request)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.update_blogs(id, db, request)
    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.delete_blogs(id, db)
