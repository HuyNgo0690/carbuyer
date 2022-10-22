from datetime import datetime

from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from db.database import get_db
from models.models import CarBrand
from schemas import schemas

router = APIRouter()


@router.get('/')
def get_all_car_brands(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    car_brands = db.query(CarBrand).group_by(CarBrand.id).filter(CarBrand.name.contains(search)).limit(limit).offset(skip).all()
    car_brands = CarBrand.serialize_list(car_brands)
    return {'results': len(car_brands), 'car_models': car_brands}


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.CarBrandResponse)
def create_car_brand(car_brand: schemas.CreateCarBrandSchema, db: Session = Depends(get_db)):
    try:
        new_brand = CarBrand(**car_brand.dict())
        db.add(new_brand)
        db.commit()
        db.refresh(new_brand)
        return new_brand
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=500, detail=error)


@router.put('/{id}', response_model=schemas.CarBrandResponse)
def update_car_brand(id: str, car_brand: schemas.UpdateCarBrandSchema, db: Session = Depends(get_db)):
    try:
        query = db.query(CarBrand).filter(CarBrand.id == id)
        result = query.first()

        if not result:
            raise HTTPException(status_code=status.HTTP_200_OK,
                                detail=f'No car brand with this id: {id} found')
        car_brand = car_brand.dict(exclude_unset=True)
        car_brand.update(dict(updated_at=datetime.utcnow()))
        result.set_data(car_brand)
        db.commit()
        return result
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=500, detail=error)


@router.get('/{id}', response_model=schemas.CarBrandResponse)
def get_car_brand(id: str, db: Session = Depends(get_db)):
    query = db.query(CarBrand).filter(CarBrand.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No car brand with this id: {id} found")
    return query


@router.delete('/{id}')
def delete_car_brand(id: str, db: Session = Depends(get_db)):
    try:
        query = db.query(CarBrand).filter(CarBrand.id == id)
        result = query.first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No car brand with this id: {id} found')
        query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=500, detail=error)
