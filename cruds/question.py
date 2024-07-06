from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.subcategory import QuestionCreate, QuestionUpdate
from models import Question, CategoryQuestion, SubcategoryQuestion


def find_all(db: Session):
    return db.query(Question).all()

def find_all_in_subcategory(db: Session, subcategory_id: int):
    query = select(Question).where(SubcategoryQuestion.subcategory_id == subcategory_id)
    return db.execute(query).scalars().all()

def find_all_in_category(db: Session, category_id: int):
    query = select(Question).where(CategoryQuestion.category_id == category_id)
    return db.execute(query).scalars().all()

def find_by_id(db: Session, id: int):
    query = select(Question).where(Question.id == id)
    return db.execute(query).scalars().first()

def find_by_name(db: Session, name: str):
    return db.query(Question).filter(Question.name.like(f"%{name}%")).all()

def create(db: Session, question_create: QuestionCreate, category_id: int, subcategory_id: int):
    new_question = Question(**question_create.model_dump(), category_id=category_id, subcategory_id=subcategory_id)
    db.add(new_question)
    db.commit()
    return new_question


def update(db: Session, id: int, question_update: QuestionUpdate, category_id: int, subcategory_id: int):
    question = find_by_id(db, id)
    if subcategory is None:
        return None

    subcategory.name = subcategory.name if question_update.name is None else subcategory_update.name
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
