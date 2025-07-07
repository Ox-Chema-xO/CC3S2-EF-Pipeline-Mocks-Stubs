from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_get_correct_return():
    response = client.get("/")
    assert response.status_code == 200
