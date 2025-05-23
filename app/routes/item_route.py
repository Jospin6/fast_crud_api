# app/routes/item_route.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.controllers.item_controller import create_item, get_all_items, get_item_by_id
from app.schemas.item_schema import ItemSchema

router = APIRouter()

@router.get("/", response_model=list[ItemSchema])
def route_get_items(db: Session = Depends(get_db)):
    return get_all_items(db)

@router.get("/{item_id}", response_model=ItemSchema)
def route_get_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=ItemSchema)
def route_create_item(item: ItemSchema, db: Session = Depends(get_db)):
    return create_item(db, item)
