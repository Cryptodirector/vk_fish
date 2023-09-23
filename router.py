from fastapi import APIRouter, Form
from service import save


router = APIRouter(
    prefix='/save',
    tags=['Сохранение']
)


@router.post('/save_acc')
async def save_a(login: str = Form(...), password: str = Form(...)):
    return await save(login=login, password=password)

