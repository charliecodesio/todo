from fastapi import FastAPI
from api.routes import router
import uvicorn

app = FastAPI()

app.include_router(router, prefix="/app")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# from fastapi import APIRouter, FastAPI
# from app.api.models import Item, User
# from app.api.database import conn

# router = APIRouter()
# app = FastAPI()

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Items WHERE id =" + str(item_id))
    
#     rows = cursor.fetchall()
#     items = []
#     for row in rows:
#         item = {
#             "id": row[0],
#             "name": row[1],
#             "price": row[2],
#             "description": row[3]
#         }
#         items.append(item)
#     return {"items": items}

# @app.post("/items")
# async def create_item(item: Item):
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO Items (name, price, description) VALUES (?, ?, ?)", item.name, item.price, item.description)
#     conn.commit()
#     return {"message": "Item created successfully", "item": item}

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     # Update the item in the database
#     cursor = conn.cursor()
#     cursor.execute("UPDATE Items SET name = ?, price = ?, description = ? WHERE id = ?", item.name, item.price, item.description, item_id)
#     conn.commit()
#     return {"message": "Item updated successfully", "item_id": item_id, "item": item}

# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     # Delete the item from the database
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM Items WHERE id = ?", item_id)
#     conn.commit()

#     return {"message": "Item deleted successfully", "item_id": item_id}

# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Users WHERE id =" + str(user_id))
#     rows = cursor.fetchall()
#     items = []
#     for row in rows:
#         item = {
#             "id": row[0],
#             "name": row[1],
#             "price": row[2],
#             "description": row[3]
#         }
#         items.append(item)
#     return {"users": items}

# @app.post("/users")
# async def create_user(user: User):
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO Users (username, email, full_name) VALUES (?, ?, ?)", user.username, user.email, user.full_name)
#     conn.commit()
#     return {"message": "User created successfully", "item": user}

# @app.put("/users/{user_id}")
# async def update_user(user_id: int, user: User):
#     # Update the item in the database
#     cursor = conn.cursor()
#     cursor.execute("UPDATE Users SET username = ?, email = ?, full_name = ? WHERE id = ?", user.username, user.email, user.full_name, user_id)
#     conn.commit()
#     return {"message": "User updated successfully", "user_id": user_id, "item": user}

# @app.delete("/users/{user_id}")
# async def delete_user(user_id: int):
#     # Delete the item from the database
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM Users WHERE id = ?", user_id)
#     conn.commit()

#     return {"message": "User deleted successfully", "user_id": user_id}
