from datetime import datetime

from schemas import schemas
from models.models import CarBrand
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from db.database import get_db

router = APIRouter()


@router.get('/', response_model=schemas.ListCarBrandResponse)
def get_all_car_brands(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    car_models = db.query(CarBrand).group_by(CarBrand.id).filter(CarBrand.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(car_models), 'car_models': car_models}


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.CarBrandResponse)
def create_car_brand(car_brand: schemas.CreateCarBrandSchema, db: Session = Depends(get_db)):
    new_brand = CarBrand(**car_brand.dict())
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand


@router.put('/{id}', response_model=schemas.CarBrandResponse)
def update_car_brand(id: str, car_brand: schemas.UpdateCarBrandSchema, db: Session = Depends(get_db)):
    query = db.query(CarBrand).filter(CarBrand.id == id)
    result = query.first()

    if not result:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No car brand with this id: {id} found')

    car_brand.created_at = result.created_at
    car_brand.updated_at = datetime.utcnow()
    query.update(car_brand.dict(exclude_none=True), synchronize_session=False)
    db.commit()
    return result


@router.get('/{id}', response_model=schemas.CarBrandResponse)
def get_car_brand(id: str, db: Session = Depends(get_db)):
    query = db.query(CarBrand).filter(CarBrand.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No car brand with this id: {id} found")
    return query


@router.delete('/{id}')
def delete_car_brand(id: str, db: Session = Depends(get_db)):
    query = db.query(CarBrand).filter(CarBrand.id == id)
    result = query.first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No car brand with this id: {id} found')
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
