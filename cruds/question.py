from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.question import QuestionCreate, QuestionUpdate
from models import Question, CategoryQuestion, SubCategoryQuestion



def find_all(db: Session):
    return db.query(Question).all()

def find_all_in_question(db: Session, question_id: int):
    query1 = select(SubCategoryQuestion).where(SubCategoryQuestion.question_id == question_id)
    print(query1)
    # query = select(Question).where(SubcategoryQuestion.question_id == question_id)
    return db.execute(query1).scalars().all()

def find_all_in_category(db: Session, category_id: int):
    query = select(Question).where(CategoryQuestion.category_id == category_id)
    return db.execute(query).scalars().all()

def find_by_id(db: Session, id: int):
    query = select(Question).where(Question.id == id)
    return db.execute(query).scalars().first()

def find_by_name(db: Session, name: str):
    return db.query(Question).filter(Question.name.like(f"%{name}%")).all()

def create(db: Session, question_create: QuestionCreate, category_id: int, question_id: int):
    new_question = Question(**question_create.model_dump(), category_id=category_id, question_id=question_id)
    db.add(new_question)
    db.commit()
    return new_question


def update(db: Session, id: int, question_update: QuestionUpdate, category_id: int, question_id: int):
    question = find_by_id(db, id)
    if question is None:
        return None

    question.name = question.name if question_update.name is None else question_update.name
    db.add(question)
    db.commit()
    return question


def delete(db: Session, id: int, user_id: int):
    question = find_by_id(db, id, user_id)
    if question is None:
        return None
    db.delete(question)
    db.commit()
    return question
