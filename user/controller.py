from fastapi import APIRouter
router = APIRouter(prefix='/api/v1/user')

@router.get('/list')
async def user_list():
    return ['John', 'Doe']