from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.subcategory import QuestionCreate, QuestionUpdate
from models import Question


def find_all(db: Session):
    return db.query(Question).all()

def find_all_in_subcategory(db: Session, category_id: int):
    query = select(Question).where(Question.category_id == category_id)
    return db.execute(query).scalars().all()

def find_by_id(db: Session, id: int, user_id: int):
    return db.query(Question).filter(Question.id == id).filter(Question.user_id == user_id).first()

def find_by_name(db: Session, name: str):
    return db.query(Question).filter(Question.name.like(f"%{name}%")).all()

def create(db: Session, subcategory_create: QuestionCreate, category_id: int):
    new_subcategory = Question(**subcategory_create.model_dump(), category_id=category_id)
    db.add(new_subcategory)
    db.commit()
    return new_subcategory


def update(db: Session, id: int, subcategory_update: QuestionUpdate, user_id: int):
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
