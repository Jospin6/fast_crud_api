# app/routes/item_route.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.config.db import get_session
from app.controllers.item_controller import create_item, get_items, get_item_by_id
from app.models.item_model import Item

router = APIRouter()

@router.get("/")
def route_get_items(session: Session = Depends(get_session)):
    return get_items(session)

@router.get("/{item_id}")
def route_get_item(item_id: int, session: Session = Depends(get_session)):
    item = get_item_by_id(item_id, session)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
def route_create_item(item: Item, session: Session = Depends(get_session)):
    return create_item(item, session)
