from typing import List, Dict
from sqlalchemy import inspect
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, text, Integer
from sqlalchemy.orm import relationship

from db.database import Base


class Serializer:

    def set_data(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def serialize(self) -> Dict:
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(list_items: List) -> List[Dict]:
        return [data.serialize() for data in list_items]


class CarModel(Serializer, Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("brands.id", ondelete='CASCADE'), nullable=False)
    name = Column(String, unique=True, index=True)
    logo = Column(String, unique=True, index=True)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    brand = relationship("CarBrand")


class CarBrand(Serializer, Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    logo = Column(String, unique=True, index=True)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
