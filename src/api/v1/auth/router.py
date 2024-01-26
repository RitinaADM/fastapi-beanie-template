from fastapi import APIRouter
from src.api.v1.users.schemas import UserCreate, UserRead
from src.services.users import (
    SECRET,
    auth_backend,
    fastapi_users,
    google_oauth_client,
)


auth_router = APIRouter()

auth_router.include_router(fastapi_users.get_auth_router(auth_backend),
                           prefix="/auth/jwt", tags=["auth"])

auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
                           prefix="/auth", tags=["auth"])

auth_router.include_router(fastapi_users.get_reset_password_router(),
                           prefix="/auth", tags=["auth"])

auth_router.include_router(fastapi_users.get_verify_router(UserRead),
                           prefix="/auth", tags=["auth"])

auth_router.include_router(fastapi_users.get_oauth_router(google_oauth_client, auth_backend, SECRET),
                           prefix="/auth/google", tags=["auth"])

