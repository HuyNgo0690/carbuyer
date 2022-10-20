from pydantic import BaseModel

from fastapi_restful import Resource, set_responses


# Setup
class ResponseModel(BaseModel):
    answer: str


class ResourceAlreadyExistsModel(BaseModel):
    is_found: bool


class ResourceModel(BaseModel):
    ID: str
    name: str
