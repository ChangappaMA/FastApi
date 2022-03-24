from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"data": {"name": "Chang"}}

@app.get('/about')
def about():
    return {"data": {"about": "Fastapi App"}}