
from typing import Dict
from flask import Flask
from flask_restful import Resource, Api
from flask_restful.utils import cors
from flask_migrate import upgrade, downgrade
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource


from src import v1
from src.common.db import db, ma, migrate
from src.docs import docs
from src.common.types import SecondResponseSchema, SimpleResponseSchema, SimpleRequestSchema
from src .v1 import ApiMainHandler
from src.v1.friends import FriendsHandler
from src.v1.media import MediaHandler


def alembic_upgrade(app: Flask):
    """Upgrades the database to the latest revision"""
    with app.app_context():
        upgrade()


def alembic_downgrade(app: Flask):
    """Downgrades the database to the previous revision"""
    with app.app_context():
        downgrade()


def create_app(context_config="DevelopmentConfig"):
    app: Flask = Flask(__name__)
    api: Api = Api(app, catch_all_404s=True)
    app.config.from_object(f"src.config.{context_config}")
    app.config["SQLALCHEMY_DATABASE_URI"] = "amazondynamodb:///?Access Key=xxx&Secret Key=xxx&Domain=amazonaws.com&Region=OREGON"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config.update({
        "APISPEC_SPEC": APISpec(
            title="Awesome Project",
            version="v1",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0"
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
        "APISPEC_SWAGGER_UI_URL": "/swagger-ui/"  # URI to access UI of API Doc
    })

    # SWAGGER_URL: str = "/docs"
    # API_URL: str = "/static/openapi.json"
    # SWAGGERUI_BLUEPRINT: Dict = get_swaggerui_blueprint(
    #     SWAGGER_URL,
    #     API_URL,
    #     config={
    #         "app_name": "VizioGramAPI"
    #     }
    # )
    # app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    docs.init_app(app)

    app.register_blueprint(v1.bp)

    class MainHandler(MethodResource, Resource):

        @doc(description="My First GET Awesome API.", tags=["Awesome"])
        @marshal_with(SimpleResponseSchema)
        @cors.crossdomain(origin="*")
        def get(self) -> SimpleResponseSchema:
            return {"data": "Hello World!"}

        @doc(description="My First GET Awesome API.", tags=["Awesome"])
        @use_kwargs(SimpleRequestSchema, location=("json"))
        @marshal_with(SimpleResponseSchema)  # marshalling
        def post(self) -> SimpleResponseSchema:
            """
            Get method represents a GET API method
            """
            return {"message": "My First Awesome API"}

    api.add_resource(MainHandler, "/")
    api.add_resource(ApiMainHandler, "/api/")
    api.add_resource(FriendsHandler, "/api/friends/")
    api.add_resource(MediaHandler, "/api/media/")

    docs.register(MainHandler)
    docs.register(ApiMainHandler)
    docs.register(FriendsHandler)
    docs.register(MediaHandler)

    return app
