from fastapi import FastAPI
from app.routers import users, items
import uvicorn

app = FastAPI()

# app.include_router(router, prefix="/app")

router = users.router

app.include_router(router)
app.include_router(items.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)