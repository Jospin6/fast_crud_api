# app/schemas/item_schema.py
from pydantic import BaseModel

# Pour la création (requête POST)
class ItemCreate(BaseModel):
    name: str

# Pour la lecture (réponse avec id)
class ItemSchema(ItemCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
