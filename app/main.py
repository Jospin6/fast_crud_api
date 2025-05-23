from fastapi import FastAPI
from app.routes.item_route import router as item_router

app = FastAPI(title="FastAPI with PostgreSQL", version="0.1")

app.include_router(item_router, prefix="/api/v1/items", tags=["items"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
