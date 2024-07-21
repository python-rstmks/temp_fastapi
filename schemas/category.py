from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    # user_id: int = Field(gt=0, examples=[1])

class CategoryResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    user_id: int

    model_config = ConfigDict(from_attributes=True)