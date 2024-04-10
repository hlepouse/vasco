from marshmallow import Schema, fields
import os

class TargetPerMonthInputSchema(Schema):
    year = fields.Int(required=True, validate=lambda x: int(os.getenv('YEAR_MIN')) <= x <= int(os.getenv('YEAR_MAX')))
    month = fields.Int(required=True, validate=lambda x: 1 <= x <= 12)