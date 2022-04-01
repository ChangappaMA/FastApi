from fastapi import FastAPI

from .models import Base
from .database import engine
from .routers import blog, user, auth


app = FastAPI()
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)


Base.metadata.create_all(bind=engine)




    ####generate JWT TOKEN