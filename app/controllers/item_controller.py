# app/controllers/item_controller.py
from fastapi import Depends
from sqlmodel import Session, select
from app.models.item_model import Item


def create_item(item: Item, session: Session):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def get_items(session: Session):
    return session.exec(select(Item)).all()

def get_item_by_id(item_id: int, session: Session):
    return session.get(Item, item_id)

def delete_item(item_id: int, session: Session):
    item = session.get(Item, item_id)
    if item:
        session.delete(item)
        session.commit()
    return item