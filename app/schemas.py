from pydantic import BaseModel

class UserIn(BaseModel):
    name: str
    email: str

class UserOut(UserIn):
    id: int
