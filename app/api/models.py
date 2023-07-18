from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str

class User(BaseModel):
    username: str
    email: str
    full_name: str