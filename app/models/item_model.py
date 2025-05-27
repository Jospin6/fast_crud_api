# app/models/item_model.py
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID

class Item(SQLModel, table=True):
    id: Optional[UUID] = Field(default=None, primary_key=True)
    name: str
