import os
import sys

app_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(app_dir)

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session, sessionmaker
from models import Base, Item
from schemass import DecodedToken
from main import app
from database import get_db
from cruds.auth import get_current_user


@pytest.fixture()
def session_fixture():
    engine = create_engine(
        url="sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        item1 = Item(name="PC1", price=10000, description="test1", user_id="1")
        item2 = Item(name="PC2", price=10000, description="test2", user_id="2")
        db.add(item1)
        db.add(item2)
        db.commit()
        yield db
    finally:
        db.close()

@pytest.fixture()
def session_fixture():
    engine = create_engine()

@pytest.fixture()
def user_fixture():
    return DecodedToken(username="user1", user_id=1)


@pytest.fixture()
def client_fixture(session_fixture: Session, user_fixture: DecodedToken):
    def override_get_db():
        return session_fixture

    def override_get_current_user():
        return user_fixture

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user

    client = TestClient(app)
    yield client

    app.dependency_overrides.clear()
