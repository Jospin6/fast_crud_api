from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_items():
    response = client.get("/api/v1/items")
    assert response.status_code == 200

def test_getItem():
    id = 1
    response = client.get(f"/api/v1/items/{id}")
    assert response.status_code == 200

def test_create_item():
    body = {"id": 21, "name": "jn ndagano", "price": 200.0, "categ": "admin"}
    response = client.post("/api/v1/items/", json=body)
    assert response.status_code == 200
    assert response.json() == body
# Run the tests with the following command: pytest tests/test_items.py