from fastapi import FastAPI, HTTPException
from app.schemas import UserIn, UserOut
from app.storage import add_user, get_all_users, get_user_by_id, delete_user_by_id
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import status

app = FastAPI(
    title="miceAPI",
    description="API for handling user requests via JSON storage, later connecting mysql",
    version="1.0.0"
)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return get_swagger_ui_html(
        title="miceAPI - Swagger UI"
    )

@app.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED, tags=["requests"])
async def create_user(user: UserIn):
    new_user = await add_user(user.dict())
    return new_user

@app.get("/users/", response_model=list[UserOut], tags=["requests"])
async def list_users():
    return await get_all_users()

@app.get("/users/{user_id}", response_model=UserOut, tags=["requests"])
async def get_user(user_id: int):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}", tags=["requests"])
async def delete_user(user_id: int):
    success = await delete_user_by_id(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User with id {user_id} deleted successfully"}


if __name__ == "__main__":
    pass
    # uvicorn app.main:app --host 0.0.0.0 --port 3131 --reload
    # localhost:3131/docs