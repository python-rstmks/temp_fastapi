from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.question import QuestionCreate, QuestionUpdate
from models import Question, SubCategoryQuestion, CategoryQuestion
from sqlalchemy.exc import SQLAlchemyError



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

def find_all_in_subcategory(db: Session, subcategory_id: int):
    query1 = select(SubCategoryQuestion.question_id).where(SubCategoryQuestion.subcategory_id == subcategory_id)
    question_ids = db.execute(query1).scalars().all()
    query = select(Question).where(Question.id.in_(question_ids))
    return db.execute(query).scalars().all()

def find_by_id(db: Session, id: int):
    query = select(Question).where(Question.id == id)
    return db.execute(query).scalars().first()

def find_by_name(db: Session, name: str):
    return db.query(Question).filter(Question.name.like(f"%{name}%")).all()


def create(db: Session, question_create: QuestionCreate):
    try:
        question_data = question_create.model_dump(exclude={"category_id", "subcategory_id"})
        new_question = Question(**question_data)
        db.add(new_question)
        db.commit()

        new_category_question = CategoryQuestion(category_id=question_create.category_id, question_id=new_question.id)
        new_subcategory_question = SubCategoryQuestion(subcategory_id=question_create.subcategory_id, question_id=new_question.id)
        db.add(new_category_question)
        db.add(new_subcategory_question)
        
        db.commit()
        
        return new_question
    except SQLAlchemyError as e:
        db.rollback()
        raise e



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
