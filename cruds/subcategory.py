from sqlalchemy.orm import Session
from schemas.subcategory import SubCategoryCreate, SubCategoryUpdate
from models import SubCategory


def find_all(db: Session):
    return db.query(SubCategory).all()


def find_by_id(db: Session, id: int, user_id: int):
    return db.query(SubCategory).filter(SubCategory.id == id).filter(SubCategory.user_id == user_id).first()


def find_by_name(db: Session, name: str):
    return db.query(SubCategory).filter(SubCategory.name.like(f"%{name}%")).all()


def create(db: Session, subcategory_create: SubCategoryCreate, user_id: int, category_id: int):
    new_subcategory = SubCategory(**subcategory_create.model_dump(), user_id=user_id)
    db.add(new_subcategory)
    db.commit()
    return new_subcategory


def update(db: Session, id: int, subcategory_update: SubCategoryUpdate, user_id: int):
    subcategory = find_by_id(db, id, user_id)
    if subcategory is None:
        return None

    subcategory.name = subcategory.name if subcategory_update.name is None else subcategory_update.name
    db.add(subcategory)
    db.commit()
    return subcategory


def delete(db: Session, id: int, user_id: int):
    subcategory = find_by_id(db, id, user_id)
    if subcategory is None:
        return None
    db.delete(subcategory)
    db.commit()
    return subcategory
