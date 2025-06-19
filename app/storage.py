import json
from pathlib import Path
from typing import List, Optional
import aiofiles

data_file = Path("users.json")

async def read_users() -> List[dict]:
    if data_file.exists():
        async with aiofiles.open(data_file, "r") as f:
            content = await f.read()
            return json.loads(content)
    return []

async def write_users(users: List[dict]) -> None:
    async with aiofiles.open(data_file, "w") as f:
        content = json.dumps(users, indent=2)
        await f.write(content)

async def add_user(user_data: dict) -> dict:
    users = await read_users()
    user_data["id"] = (max([u["id"] for u in users], default=0) + 1)
    users.append(user_data)
    await write_users(users)
    return user_data

async def get_all_users() -> List[dict]:
    return await read_users()

async def get_user_by_id(user_id: int) -> Optional[dict]:
    users = await read_users()
    return next((u for u in users if u["id"] == user_id), None)


async def delete_user_by_id(user_id: int) -> bool:
    users = await read_users()
    filtered_users = [u for u in users if u["id"] != user_id]

    if len(users) == len(filtered_users):
        return False  # user not found

    await write_users(filtered_users)
    return True
