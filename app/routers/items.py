from fastapi import APIRouter, Query
from app.config.database import conn
from app.config.models import Item

router = APIRouter()

@router.get("/items/")
async def get_item(item: str = Query(None, description="Filter by user")):
    with conn.connect() as connection:
        if item is not None:
            result = connection.execute("SELECT * FROM items WHERE id = " + str(item) )
        else: 
            result = connection.execute("SELECT * FROM items")

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
        return {"items": items}

@router.post("/items")
async def create_item(item: Item):
    with conn.connect() as connection:
        connection.execute( "INSERT INTO items (name, price, description) VALUES (?, ?, ?)", item.name, item.price, item.description)
    return {"message": "Item created successfully", "item": item}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    with conn.connect() as connection:
        connection.execute("UPDATE Items SET name = ?, price = ?, description = ? WHERE id = ?", item.name, item.price, item.description, item_id)
    return {"message": "Item updated successfully", "item_id": item_id, "item": item}

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    with conn.connect() as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Items WHERE id = ?", item_id)
    return {"message": "Item deleted successfully", "item_id": item_id}
