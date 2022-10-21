from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, text
from db.database import Base


class CarBase(Base):
    name = Column(String, unique=True, index=True)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class CarModel(CarBase):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("car_brands.id", ondelete='CASCADE'), nullable=False)
    brand = relationship("CarBrand", back_populates="model")


class CarBrand(CarBase):
    __tablename__ = "car_brands"

    id = Column(Integer, primary_key=True, index=True)
    models = relationship("CarModel", back_populates="brand")
