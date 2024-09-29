from models import Category
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from factory.alchemy import SQLAlchemyModelFactory
from factory import Faker
from config import get_settings

# このpythonファイルを実行することで、カテゴリーテーブルにデータを追加することができる。

SQLALCHEMY_DATABASE_URL = get_settings().sqlalchemy_database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

class CategoryFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Category
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    name = Faker("name")
    user_id = 1
    
    
num_categories = 2
categories = CategoryFactory.create_batch(num_categories)

session.add_all(categories)
session.commit()
session.close()