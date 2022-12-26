from fastapi import APIRouter
from . import model as user_model

router = APIRouter(prefix='/api/v1/user')


@router.get('/list')
async def user_list():
    return ['John', 'Doe']


@router.get('/{userid}')
async def details(userid: int):
    return {'user id': userid}


@router.post('/create')
async def create(user: user_model.User):
    return user
