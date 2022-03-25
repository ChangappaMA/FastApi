from typing import final
from fastapi import FastAPI, Depends
from .schemas import Blog
from .models import Base, BlogModel
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create_blog(blog: Blog, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog