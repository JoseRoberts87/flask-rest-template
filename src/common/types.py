

from typing import Dict, TypedDict
from marshmallow import Schema, fields


class OutputHeaders(TypedDict):
    ContentType: str
    AccessControlAllowOrigin: str
    AccessControlAllowHeaders: str
    AccessControlMaxAge: str


class OutputJson(TypedDict):
    msg: Dict
    status: int
    headers: OutputHeaders


class SimpleResponseSchema(Schema):
    message = fields.Str(dump_default="Success")


class SecondResponseSchema(Schema):
    message = fields.Str(dump_default="Success")
    active = fields.Bool(dump_default=True)


class FriendsResponseSchema(Schema):
    id = fields.Str(dump_default="Success")
    status = fields.Str(dump_default="Success")
    name = fields.Str(dump_default="Success")


class SimpleRequestSchema(Schema):
    api_type = fields.String(
        required=True)
