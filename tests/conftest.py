import os
os.environ["DATABASE_URL"] = "sqlite:///./test_shop.db"

import pytest
from fastapi.testclient import TestClient
from app.database import Base, engine
from app.main import app

@pytest.fixture(autouse=True)
def clean_database():
    Base.metadata.drop_all(bind=engine); Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(): return TestClient(app)

@pytest.fixture
def user(client):
    return client.post("/users", json={"name":"QA User","email":"qa@example.com","age":30,"password":"password123"}).json()

@pytest.fixture
def product(client):
    return client.post("/products", json={"name":"Keyboard","price":25.5,"stock":10}).json()
