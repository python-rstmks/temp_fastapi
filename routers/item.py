from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import item as item_cruds, auth as auth_cruds
from schemas.item import ItemResponse, ItemCreate, ItemUpdate
from schemas.auth import DecodedToken
from database import get_db


DbDependency = Annotated[Session, Depends(get_db)]

UserDependency = Annotated[DecodedToken, Depends(auth_cruds.get_current_user)]

# 
router = APIRouter(prefix="/items", tags=["Items"])

# tags は、FastAPIでAPIルーターやエンドポイントにメタデータを追加するために使用されるオプションの引数です。これにより、APIドキュメント（例えば、Swagger UI）においてAPIエンドポイントをカテゴリごとにグループ化することができます。

@router.get("", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DbDependency):
    return item_cruds.find_all(db)


@router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def find_by_id(db: DbDependency, user: UserDependency, id: int = Path(gt=0)):
    found_item = item_cruds.find_by_id(db, id, user.user_id)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item


@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_by_name(
    db: DbDependency, name: str = Query(min_length=2, max_length=20)
):
    return item_cruds.find_by_name(db, name)


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DbDependency, user: UserDependency, item_create: ItemCreate):
    print(item_create)
    print("sakamotosora")
    return item_cruds.create(db, item_create, user.user_id)


@router.put("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def update(
    db: DbDependency,
    user: UserDependency,
    item_update: ItemUpdate,
    id: int = Path(gt=0),
):
    updated_item = item_cruds.update(db, id, item_update, user.user_id)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not updated")
    return updated_item


@router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def delete(db: DbDependency, user: UserDependency, id: int = Path(gt=0)):
    deleted_item = item_cruds.delete(db, id, user.user_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return deleted_item
