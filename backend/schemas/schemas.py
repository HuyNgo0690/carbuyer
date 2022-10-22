from typing import Union, List, Optional
from datetime import datetime
from pydantic import BaseModel


class CarBrandBase(BaseModel):
    name: str
    logo: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class CreateCarBrandSchema(CarBrandBase):
    pass


class UpdateCarBrandSchema(BaseModel):
    name: Optional[str] = None
    logo: Optional[str] = None
    description: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True


class CarBrandResponse(CarBrandBase):
    id: int
    name: str
    logo: str
    description: str
    created_at: datetime
    updated_at: datetime


class FilteredCarBrandResponse(CarBrandBase):
    name: str


class CarModelBase(BaseModel):
    brand_id: int
    name: str
    logo: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class CreateCarModelSchema(CarModelBase):
    pass


class CarModelResponse(CarModelBase):
    id: int
    name: str
    logo: str
    brand: FilteredCarBrandResponse
    created_at: datetime
    updated_at: datetime


class UpdateCarModelSchema(BaseModel):
    name: Optional[str] = None
    logo: Optional[str] = None
    description: Optional[str] = None
    brand_id: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True
