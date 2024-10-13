from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import subcategory as subcategory_cruds, auth as auth_cruds
from schemas.subcategory import SubCategoryResponse, SubCategoryUpdate, SubCategoryCreate
from schemas.auth import DecodedToken
from database import get_db
from cruds import category as category_cruds


DbDependency = Annotated[Session, Depends(get_db)]

UserDependency = Annotated[DecodedToken, Depends(auth_cruds.get_current_user)]

# 
router = APIRouter(prefix="/subcategories", tags=["SubCategories"])

# tags は、FastAPIでAPIルーターやエンドポイントにメタデータを追加するために使用されるオプションの引数です。これにより、APIドキュメント（例えば、Swagger UI）においてAPIエンドポイントをカテゴリごとにグループ化することができます。

@router.get("", response_model=list[SubCategoryResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DbDependency):
    return subcategory_cruds.find_all(db)


@router.get("/{id}", response_model=SubCategoryResponse, status_code=status.HTTP_200_OK)
async def find_by_id(
    db: DbDependency, 
    # user: UserDependency, 
    id: int = Path(gt=0)
):
    # found_subcategory = subcategory_cruds.find_by_id(db, id, user.user_id)
    found_subcategory = subcategory_cruds.find_by_id(db, id)
    if not found_subcategory:
        raise HTTPException(status_code=404, detail="SubCategory not found")
    return found_subcategory

@router.get("/category_id/{category_id}", response_model=list[SubCategoryResponse], status_code=status.HTTP_200_OK)
async def find_all_subcategories_in_category(db: DbDependency, category_id: int = Path(gt=0)):
    return subcategory_cruds.find_all_subcategories_in_category(db, category_id)

@router.get("/", response_model=list[SubCategoryResponse], status_code=status.HTTP_200_OK)
async def find_by_name(
    db: DbDependency, name: str = Query(min_length=2, max_length=20)
):
    return subcategory_cruds.find_by_name(db, name)


@router.post("/", response_model=SubCategoryResponse, status_code=status.HTTP_201_CREATED)
# async def create(db: DbDependency, category_id: int, subcategory_create: SubCategoryCreate):
async def create(db: DbDependency, subcategory_create: SubCategoryCreate):
    found_category = category_cruds.find_by_id(db, subcategory_create.category_id)
    if not found_category:
        raise HTTPException(status_code=404, detail="Category not found")
    pass
    return subcategory_cruds.create(db, subcategory_create)


@router.put("/{id}", response_model=SubCategoryResponse, status_code=status.HTTP_200_OK)
async def update(
    db: DbDependency,
    # user: UserDependency,
    subcategory_update: SubCategoryUpdate,
    id: int = Path(gt=0),
):
    updated_item = subcategory_cruds.update(db, id, subcategory_update, user.user_id)
    if not updated_item:
        raise HTTPException(status_code=404, detail="SubCategory not updated")
    return updated_item


@router.delete("/{id}", response_model=SubCategoryResponse, status_code=status.HTTP_200_OK)
async def delete(
    db: DbDependency,
    # user: UserDependency,
    id: int = Path(gt=0)
):
    deleted_item = subcategory_cruds.delete(db, id, user.user_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return deleted_item
