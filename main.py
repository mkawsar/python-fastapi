from fastapi import FastAPI
from user import controller as user_controller

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Hello World'}


app.include_router(user_controller.router)
