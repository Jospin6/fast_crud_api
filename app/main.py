from fastapi import FastAPI

from app.api.v1.endpoints import items

app = FastAPI(title="FastAPI with PostgreSQL", version="0.1")

app.include_router(items.router, prefix="/api/v1/items", tags=["items"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
