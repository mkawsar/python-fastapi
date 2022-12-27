from fastapi import APIRouter, status, Form
from .schema import User

router = APIRouter(prefix='/api/v1/user')


@router.get('/list')
async def user_list():
    return ['John', 'Doe']


@router.get('/{userid}')
async def details(userid: int):
    return {'user id': userid}


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create(user: User):
    return user


@router.post('/login', status_code=status.HTTP_201_CREATED)
async def login(username: str = Form(), password: str = Form()):
    return {'username': username, 'password': password}
