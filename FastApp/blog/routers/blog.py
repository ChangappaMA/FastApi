from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..schemas import ShowBlog, Blog
from ..models import BlogModel
from ..database import get_db


router = APIRouter()

@router.get('/blog', response_model=List[ShowBlog], tags=['Blogs'])
def get_all_blog(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs

@router.get('/blog/{id}', status_code=200, response_model=ShowBlog, tags=['Blogs'])
def get_a_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    return blog


@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'])
def create_blog(blog: Blog, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
def update_blog(id: int, blog: Blog, db: Session = Depends(get_db)):
    blogg = db.query(BlogModel).filter(BlogModel.id == id)
    if not blogg.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blogg.update(blog.dict())
    db.commit()
    return 'Updated'
    

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"
