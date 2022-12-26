from fastapi import FastAPI
from user import controller as UserController

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}

app.include_router(UserController.router)