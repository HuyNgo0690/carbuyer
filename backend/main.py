from apis import app
from fastapi_restful import Api
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def create_app():
    api = Api(app)
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
    # engine = create_engine(
    #     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    # )
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    #
    # Base = declarative_base()
    from apis.car_models import CarModelApi
    car_model = CarModelApi()
    api.add_resource(car_model, "/model")
    return app


if __name__ == '__main__':
    main = create_app()
    import uvicorn

    uvicorn.run(main, host="0.0.0.0", port=8000, log_level="debug")
    # from waitress import serve
    #
    # serve(main, host='0.0.0.0')
