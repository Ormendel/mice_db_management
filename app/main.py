import uvicorn
from fastapi import FastAPI, HTTPException
from app.schemas import UserIn, UserOut
from app.storage import add_user, get_all_users, get_user_by_id

app = FastAPI()

@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    new_user = add_user(user.dict())
    return new_user

@app.get("/users/", response_model=list[UserOut])
def list_users():
    return get_all_users()

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

if __name__ == "__main__":
    pass
    # uvicorn app.main:app --host 0.0.0.0 --port 3131 --reload
    # localhost:3131/docs
