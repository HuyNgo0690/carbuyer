from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from apis import Base


class CarModel(Base):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("car_brands.id"))
    name = Column(String, unique=True, index=True)
    model_logo = Column(String, unique=True, nullable=False)
    description = Column(String)
    brand = relationship("CarBrand", back_populates="model")


class CarBrand(Base):
    __tablename__ = "car_brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand_logo = Column(String, unique=True)
    description = Column(String)
    models = relationship("CarModel", back_populates="brand")
