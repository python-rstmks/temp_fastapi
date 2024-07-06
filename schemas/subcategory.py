from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class SubCategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["q normalization"])
    category_id: int = Field(gt=0, examples=[1])
    

class SubCategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=20, examples=["q normalization"])

class SubCategoryResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    name: str = Field(min_length=2, max_length=20, examples=["q normalization"])
    category_id: int

    model_config = ConfigDict(from_attributes=True)