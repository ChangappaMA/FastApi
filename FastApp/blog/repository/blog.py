from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import BlogModel
from ..schemas import Blog




def get_blogs(db: Session):
    blogs = db.query(BlogModel).all()
    return blogs


def get_blog(id:int , db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    return blog


def create_blogs(db: Session, request: Blog):
    new_blog = BlogModel(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_blogs(id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_blogs(id:int, db:Session, request: Blog):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'Updated'