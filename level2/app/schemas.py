# These are the schemas used to validate the json inputs of the routes

from marshmallow import Schema, fields
import os

class TargetPerMonthInputSchema(Schema):
    year = fields.Int(required=True, validate=lambda x: int(os.getenv('YEAR_MIN')) <= x <= int(os.getenv('YEAR_MAX')))
    month = fields.Int(required=True, validate=lambda x: 1 <= x <= 12)

class TargetPerQuarterInputSchema(Schema):
    year = fields.Int(required=True, validate=lambda x: int(os.getenv('YEAR_MIN')) <= x <= int(os.getenv('YEAR_MAX')))
    quarter = fields.Int(required=True, validate=lambda x: 1 <= x <= 4)