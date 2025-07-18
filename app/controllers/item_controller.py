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

def update_item(item_id: int, item_data: Item, session: Session):
    item = session.get(Item, item_id)
    if not item:
        return None
    for key, value in item_data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    session.commit()
    session.refresh(item)
    return item

def delete_item(item_id: int, session: Session):
    item = session.get(Item, item_id)
    if item:
        session.delete(item)
        session.commit()
    return item