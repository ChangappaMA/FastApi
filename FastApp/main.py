from typing import Optional
from fastapi import FastAPI

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
