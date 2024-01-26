from fastapi import APIRouter

from src.api.v1.users.schemas import UserCreate, UserRead, UserUpdate
from src.services.users import (
    fastapi_users,
)
users_router = APIRouter()

users_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate),
                            prefix="/users", tags=["users"])
