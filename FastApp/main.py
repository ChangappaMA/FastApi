from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Blog(BaseModel):
    title: str
    body: str
    publish: Optional[bool]

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f'{limit} published blogs from the database'}
    return {"data": "All the blocks"}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All Unpublished Blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with the title '{blog.title}'"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port= 9000)

#start at 1:38:54 (Get blogs from database)