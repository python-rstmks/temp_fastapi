from sqlalchemy.orm import Session
from sqlalchemy import select
# from schemas import category
from schemas.category import CategoryCreate
from models import Category
from fastapi_pagination import Page, add_pagination, paginate


def find_all(db: Session):
    query = select(Category)
    return db.execute(query).scalars().all()

def find_pagination(db: Session):
    query = select(Category)
    return db.execute(query).scalars().all()

def find_by_id(db: Session, id: int):
    query = select(Category).where(Category.id == id)
    return db.execute(query).scalars().first()

def find_by_name(db: Session, name: str):
    # return db.query(Category).filter(Category.name.like(f"%{name}%")).all()
    query = select(Category).where(Category.name.like(f"%{name}%"))
    return db.execute(query).scalars().all()

# def create(db: Session, category_create: category.CategoryCreate, user_id: int):
def create(db: Session, category_create: CategoryCreate):
    new_category = Category(**category_create.model_dump(), user_id=1)
    # new_category = Category(**category_create.model_dump())
    db.add(new_category)
    db.commit()
    return new_category

# ページネーションのためのページ数を返す
# 100件のカテゴリがある場合、1ページあたり7件表示する場合、ページ数は(100/17)+ 1 = 15ページになる

# limitはconfigから取得したい。
def page_count(db: Session):
    query = select(Category)
    count = db.execute(query).scalars().count()
    
    print(f'countは{count}です')
    return count // limit + 1

