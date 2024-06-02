from sqlalchemy.orm import Session
from sqlalchemy import select
# from schemas import category
from schemas.category import CategoryCreate
from models import Category


def find_all(db: Session):
    query = select(Category)
    return db.execute(query).scalars().all()

def find_by_id(db: Session, id: int, user_id: int):
    query = select(Category).where(Category.id == id, Category.user_id == user_id)
    return db.execute(query).scalars().first()

def find_by_name(db: Session, name: str):
    # return db.query(Category).filter(Category.name.like(f"%{name}%")).all()
    query = select(Category).where(Category.name.like(f"%{name}%"))
    return db.execute(query).scalars().all()

# def create(db: Session, category_create: category.CategoryCreate, user_id: int):
def create(db: Session, category_create: CategoryCreate, user_id: int):
    new_category = Category(**category_create.model_dump(), user_id=user_id)
    db.add(new_category)
    db.commit()
    return new_category

