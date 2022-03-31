from pydantic import BaseModel
from typing import List
class Blog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str


class UserDetails(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(Blog):

    author: UserDetails
    class Config():
        orm_mode = True