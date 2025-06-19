import json
from pathlib import Path
from typing import List, Optional

data_file = Path("users.json")

def read_users() -> List[dict]:
    if data_file.exists():
        with open(data_file, "r") as f:
            return json.load(f)
    return []

def write_users(users: List[dict]) -> None:
    with open(data_file, "w") as f:
        json.dump(users, f, indent=2)

def add_user(user_data: dict) -> dict:
    users = read_users()
    user_data["id"] = (max([u["id"] for u in users], default=0) + 1)
    users.append(user_data)
    write_users(users)
    return user_data

def get_all_users() -> List[dict]:
    return read_users()

def get_user_by_id(user_id: int) -> Optional[dict]:
    return next((u for u in read_users() if u["id"] == user_id), None)
