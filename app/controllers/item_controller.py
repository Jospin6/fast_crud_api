# app/controllers/item_controller.py
from fastapi import Depends
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.models.item_model import Item
from app.schemas.item_schema import ItemCreate

def get_all_items(db: Session):
    return db.query(Item).all()

def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = Item(name=item.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item