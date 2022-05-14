from fastapi import APIRouter

from template.logic.user_service import UserService
from template.models.user import User


router = APIRouter(prefix='/users')
user_service = UserService()


@router.post("/")
async def greet(user: User) -> str:
    return user_service.greet(user)
