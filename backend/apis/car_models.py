from fastapi_restful import Resource, set_responses

from schemas.reponse_schema import ResponseModel


class CarModelApi(Resource):
    # @set_responses(ResponseModel)
    def get(self):
        return "done"
