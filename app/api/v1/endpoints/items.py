from pydantic import BaseModel
from fastapi import APIRouter


router = APIRouter()

class Item(BaseModel):
    id: int
    name: str
    price: float
    categ: str

items: Item =[
    {"id": 1, "name": "item1", "price": 10.0, "categ": "admin"},
    {"id": 2, "name": "item2", "price": 20.0, "categ": "user"},
    {"id": 3, "name": "item3", "price": 30.0, "categ": "user"},
    {"id": 4, "name": "item4", "price": 40.0, "categ": "admin"},
    {"id": 5, "name": "item5", "price": 50.0, "categ": "user"},
    {"id": 6, "name": "item6", "price": 60.0, "categ": "admin"},
    {"id": 7, "name": "item7", "price": 70.0, "categ": "admin"},
    {"id": 8, "name": "item8", "price": 80.0, "categ": "user"},
    {"id": 9, "name": "item9", "price": 90.0, "categ": "admin"},
    {"id": 10, "name": "item10", "price": 100.0, "categ": "admin"},
]

@router.get("/")
async def getItems(q: str = None):
    if q:
        return [item for item in items if q.lower() in item["categ"].lower()]
    return items

@router.get("/{item_id}")
async def getItem(item_id: int):
    return [item for item in items if item["id"] == item_id]

@router.post("/")
async def createItem(item: Item):
    items.append(item)
    return item

@router.put("/{item_id}")
async def updateItem(item_id: int, item: Item):
    for i in range(len(items)):
        if items[i]["id"] == item_id:
            items[i] = item
            return item
    return {"message": "Item not found"}

@router.delete("/{item_id}")
async def deleteItem(item_id: int):
    for i in range(len(items)):
        if items[i]["id"] == item_id:
            item = items[i]
            del items[i]
            return item
    return {"message": "Item not found"}