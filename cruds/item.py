from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import item
from models import Item


def find_all(db: Session):
    query = select(Item)
    return db.execute(query).scalars().all()


def find_by_id(db: Session, id: int, user_id: int):
    query = select(Item).where(Item.id == id, Item.user_id == user_id)
    return db.execute(query).scalars().first()


def find_by_name(db: Session, name: str):
    query = select(Item).where(Item.name.like(f"%{name}%"))
    return db.execute(query).scalars().all()

def create(db: Session, item_create: item.ItemCreate, user_id: int):
    new_item = Item(**item_create.model_dump(), user_id=user_id)
    print(item_create.model_dump())
    print("sakamotosora")
    db.add(new_item)
    db.commit()
    return new_item


def update(db: Session, id: int, item_update: item.ItemUpdate, user_id: int):
    item = find_by_id(db, id, user_id)
    if item is None:
        return None

    item.name = item.name if item_update.name is None else item_update.name
    item.price = item.price if item_update.price is None else item_update.price
    item.description = (
        item.description if item_update.description is None else item_update.description
    )
    item.status = item.status if item_update.status is None else item_update.status
    db.add(item)
    db.commit()
    return item


def delete(db: Session, id: int, user_id: int):
    item = find_by_id(db, id, user_id)
    if item is None:
        return None
    db.delete(item)
    db.commit()
    return item
