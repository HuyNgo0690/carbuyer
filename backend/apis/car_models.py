from datetime import datetime

from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from db.database import get_db
from models.models import CarModel
from schemas import schemas

router = APIRouter()


@router.get('/')
def get_all_car_models(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    car_models = db.query(CarModel).group_by(CarModel.id).filter(CarModel.name.contains(search)).limit(limit).offset(skip).all()
    car_models = CarModel.serialize_list(car_models)
    return {'results': len(car_models), 'car_models': car_models}


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.CarModelResponse)
def create_car_model(car_model: schemas.CreateCarModelSchema, db: Session = Depends(get_db)):
    try:
        new_model = CarModel(**car_model.dict())
        db.add(new_model)
        db.commit()
        db.refresh(new_model)
        return new_model
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=500, detail=error)


@router.put('/{id}', response_model=schemas.CarModelResponse)
def update_car_model(id: str, car_model: schemas.UpdateCarModelSchema, db: Session = Depends(get_db)):
    try:
        car_model_query = db.query(CarModel).filter(CarModel.id == id)
        result = car_model_query.first()

        if not result:
            raise HTTPException(status_code=status.HTTP_200_OK,
                                detail=f'No car model with this id: {id} found')

        car_model.updated_at = datetime.utcnow()
        car_model_query.update(car_model.dict(exclude_none=True), synchronize_session=False)
        db.commit()
        return result
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=500, detail=error)


@router.get('/{id}', response_model=schemas.CarModelResponse)
def get_car_model(id: str, db: Session = Depends(get_db)):
    car_model = db.query(CarModel).filter(CarModel.id == id).first()
    if not car_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No car model with this id: {id} found")
    return car_model


@router.delete('/{id}')
def delete_post(id: str, db: Session = Depends(get_db)):
    try:
        query = db.query(CarModel).filter(CarModel.id == id)
        result = query.first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No car model with this id: {id} found')
        query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=500, detail=error)
