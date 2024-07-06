from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import question as question_cruds, auth as auth_cruds
from schemas.question import QuestionResponse, QuestionUpdate, QuestionCreate
from schemas.auth import DecodedToken
from database import get_db
from cruds import question as question_cruds, category as category_cruds


DbDependency = Annotated[Session, Depends(get_db)]

UserDependency = Annotated[DecodedToken, Depends(auth_cruds.get_current_user)]

# 
router = APIRouter(prefix="/questions", tags=["Questions"])

# tags は、FastAPIでAPIルーターやエンドポイントにメタデータを追加するために使用されるオプションの引数です。これにより、APIドキュメント（例えば、Swagger UI）においてAPIエンドポイントをカテゴリごとにグループ化することができます。

@router.get("", response_model=list[QuestionResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DbDependency):
    return question_cruds.find_all(db)


@router.get("/{id}", response_model=QuestionResponse, status_code=status.HTTP_200_OK)
async def find_by_id(db: DbDependency, user: UserDependency, id: int = Path(gt=0)):
    found_question = question_cruds.find_by_id(db, id, user.user_id)
    if not found_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return found_question

@router.get("/category_id/{category_id}", response_model=list[QuestionResponse], status_code=status.HTTP_200_OK)
# async def find_all_questions_in_category(db: DbDependency, user:UserDependency, category_id: int = Path(gt=0)):
async def find_all_questions_in_category(db: DbDependency, category_id: int = Path(gt=0)):
    return question_cruds.find_all_questions_in_category(db, category_id)

@router.get("/", response_model=list[QuestionResponse], status_code=status.HTTP_200_OK)
async def find_by_name(
    db: DbDependency, name: str = Query(min_length=2, max_length=20)
):
    return question_cruds.find_by_name(db, name)


@router.post("/{category_id}/{subcategory_id}", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DbDependency, category_id: int, question_create: QuestionCreate):
    found_category = category_cruds.find_by_id(db, category_id, subcategory_id)
    if not found_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return question_cruds.create(db, question_create, category_id)


@router.put("/{id}", response_model=QuestionResponse, status_code=status.HTTP_200_OK)
async def update(
    db: DbDependency,
    user: UserDependency,
    question_update: QuestionUpdate,
    id: int = Path(gt=0),
):
    updated_item = question_cruds.update(db, id, question_update, user.user_id)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Question not updated")
    return updated_item


@router.delete("/{id}", response_model=QuestionResponse, status_code=status.HTTP_200_OK)
async def delete(db: DbDependency, user: UserDependency, id: int = Path(gt=0)):
    deleted_item = question_cruds.delete(db, id, user.user_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return deleted_item
