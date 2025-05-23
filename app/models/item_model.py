# app/models/item_model.py
from sqlalchemy import Column, Integer, String
from app.config.db import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
