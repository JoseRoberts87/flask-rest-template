from typing import Dict
from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_restful.utils import cors
from flask_apispec import marshal_with, doc
from flask_apispec.views import MethodResource

from src.common.types import SecondResponseSchema
from src.docs import docs


bp: Blueprint = Blueprint("api", __name__, url_prefix="/api")
api: Api = Api(bp, catch_all_404s=True)


class MediaHandler(MethodResource, Resource):

    @doc(description="My First GET Awesome API.", tags=["media"])
    @marshal_with(SecondResponseSchema)
    @cors.crossdomain(origin="*")
    def get(self) -> SecondResponseSchema:
        scheme = SecondResponseSchema()
        response = {
            "message": "this is a sample response from the '/api' endpoint in flask Container",
            "active": False,
        }

        error = scheme.validate(response)
        print(error)

        return response
