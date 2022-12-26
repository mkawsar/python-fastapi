from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from user import controller as user_controller

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


app.include_router(user_controller.router)
