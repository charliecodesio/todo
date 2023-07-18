from fastapi import APIRouter, Query
from app.api.database import conn
from app.api.models import User

router = APIRouter()

@router.get("/users/")
async def get_user(user: str = Query(None, description="Filter by user")):
    with conn.connect() as connection:
        if user is not None:
            result = connection.execute("SELECT * FROM Users WHERE id =" + str(user))
        else:
            result = connection.execute("SELECT * FROM Users")
        rows = result.fetchall()
        items = []
        for row in rows:
            item = {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "description": row[3]
            }
            items.append(item)
        return {"users": items}

@router.post("/users")
async def create_user(user: User):
    with conn.connect() as connection:
        connection.execute("INSERT INTO Users (username, email, full_name) VALUES (?, ?, ?)", user.username, user.email, user.full_name)
        return {"message": "User created successfully", "item": user}

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    with conn.connect() as connection:
        connection.execute("UPDATE Users SET username = ?, email = ?, full_name = ? WHERE id = ?", user.username, user.email, user.full_name, user_id)
        return {"message": "User updated successfully", "user_id": user_id, "item": user}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    with conn.connect() as connection:
        connection.execute("DELETE FROM Users WHERE id = ?", user_id)
        return {"message": "User deleted successfully", "user_id": user_id}
