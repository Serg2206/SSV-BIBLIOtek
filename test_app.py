from fastapi.testclient import TestClient
from app import app  # Импорт приложения FastAPI из файла app.py

# Создание тестового клиента
client = TestClient(app)

def test_read_root():
    """Тест для маршрута '/'."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "SSV-BIBKIOtek API is running!"}

def test_hello_route():
    """Тест для маршрута '/hello/{name}'."""
    name = "TestUser"
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Привет, {name}!"}
