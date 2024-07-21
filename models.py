from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, ARRAY, Boolean
from sqlalchemy.orm import relationship
from database import Base
from schemas import item


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    # id = mapped_column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(item.ItemStatus), nullable=False, default=item.ItemStatus.ON_SALE)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user = relationship("User", back_populates="items")
    
# =================================================================================================
    
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user = relationship("User", back_populates="categories")
    subcategories = relationship("SubCategory", back_populates="category")
    questions = relationship("CategoryQuestion", back_populates="category")
    
class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    category_id = Column(
        Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )

    # category = relationship("Category", back_populates="subcategory")
    # ↓なぜsubcategoriesと複数形なのか
    category = relationship("Category", back_populates="subcategories")
    
    questions = relationship("SubCategoryQuestion", back_populates="subcategory")

    
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    problem = Column(String, nullable=False)
    answer = Column(ARRAY(String), nullable=False)
    is_correct = Column(Boolean, nullable=False, default=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    
    subcategories = relationship("SubCategoryQuestion", back_populates="question")
    categories = relationship("CategoryQuestion", back_populates="question")
    
class SubCategoryQuestion(Base):
    __tablename__ = "subcategory_question"
    subcategory_id = Column(
        Integer, ForeignKey("subcategories.id"), primary_key=True
    )
    question_id = Column(
        Integer, ForeignKey("questions.id"), primary_key=True
    )
    subcategory = relationship("SubCategory", back_populates="questions")
    question = relationship("Question", back_populates="subcategories")
    
class CategoryQuestion(Base):
    __tablename__ = "category_question"
    category_id = Column(
        Integer, ForeignKey("categories.id"), primary_key=True
    )
    question_id = Column(
        Integer, ForeignKey("questions.id"), primary_key=True
    )
    category = relationship("Category", back_populates="questions")
    question = relationship("Question", back_populates="categories")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    items = relationship("Item", back_populates="user")
    categories = relationship("Category", back_populates="user")
