from typing import Dict
from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_restful.utils import cors
from flask_apispec import marshal_with, doc
from flask_apispec.views import MethodResource

from src.common.types import FriendsResponseSchema
from src.docs import docs


bp: Blueprint = Blueprint("api", __name__, url_prefix="/api")
api: Api = Api(bp, catch_all_404s=True)


class FriendsHandler(MethodResource, Resource):

    @doc(description="My First GET Awesome API.", tags=["friends"])
    @marshal_with(FriendsResponseSchema)
    @cors.crossdomain(origin="*")
    def get(self) -> FriendsResponseSchema:
        scheme = FriendsResponseSchema()
        response = {
            "id": "1",
            "status": "active",
            "name": "John Doe", }

        error = scheme.validate(response)
        print(error)

        return response
