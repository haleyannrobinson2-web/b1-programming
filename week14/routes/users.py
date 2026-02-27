from fastapi import APIRouter, HTTPException
from schema import UserCreate
from user_store import UserStore

router = APIRouter()

store = UserStore("users.txt")

@router.get("/")
def get_users():
    return store.load()

@router.post("/")
def create_user(user: UserCreate):
    return store.create_user(user)

@router.get("/search")
def search_users(q: str):
    users = store.load()
    return [user for user in users if q.lower() in user["name"].lower()]

@router.get("/{user_id}")
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user(user_id: int, updated_user: UserCreate):
    success = store.update_user(user_id, updated_user)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = store.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
