from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_items():
    """
    It should return a list of items with status code 200.
    """
    response = client.get("/api/v1/items")
    assert response.status_code == 200

def test_getItem():
    """
    It should return a specific item with status code 200 when ID exists.
    """
    id = 1
    response = client.get(f"/api/v1/items/{id}")
    assert response.status_code == 200

def test_create_item():
    """
    It should create a new item and return it with status code 200.
    """
    body = {"id": 21, "name": "jn ndagano", "price": 200.0, "categ": "admin"}
    response = client.post("/api/v1/items/", json=body)
    assert response.status_code == 200
    assert response.json() == body