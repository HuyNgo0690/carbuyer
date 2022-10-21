from typing import Union

from pydantic import BaseModel


class CarModelBase(BaseModel):
    brand_id: int
    name: str
    model_logo: str
    description: Union[str, None] = None


class CarModelCreate(CarModelBase):
    pass


class CarModel(CarModelBase):
    id: int
    brand_id: int

    class Config:
        orm_mode = True


class CarBrandBase(BaseModel):
    name: str
    model_logo: str
    description: Union[str, None] = None


class CardBrandCreate(CarBrandBase):
    pass


class CarBrand(CarBrandBase):
    id: int

    class Config:
        orm_mode = True
