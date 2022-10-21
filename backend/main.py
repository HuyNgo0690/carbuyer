from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis import car_models, car_brands
from config.config import settings
from db.database import Base, engine

origins = [
    settings.CLIENT_ORIGIN,
]


def add_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def include_app(app):
    app.include_router(car_models.router, tags=['Car Model'], prefix='/api/model')
    app.include_router(car_brands.router, tags=['Car Brand'], prefix='/api/brand')


def create_tables():  # new
    Base.metadata.create_all(bind=engine)


def start_app():
    app = FastAPI(title="Cars")
    add_middleware(app)
    include_app(app)
    create_tables()  # new
    return app


if __name__ == '__main__':
    app = start_app()
    import uvicorn

    # uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
    uvicorn.run(app, host="0.0.0.0", port=settings.DEBUG_PORT)
