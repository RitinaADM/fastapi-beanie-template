from beanie import init_beanie
from fastapi import Depends, FastAPI
from src.db.db import User, db
from src.api.v1.users.router import users_router
from src.api.v1.auth.router import auth_router
from src.services.users import current_active_user


app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    await init_beanie(
        database=db,
        document_models=[
            User
        ],
    )