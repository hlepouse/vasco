from marshmallow import Schema, fields

class TargetPerMonthInputSchema(Schema):
    year = fields.Int(required=True, validate=lambda x: 1900 <= x <= 3000)
    month = fields.Int(required=True, validate=lambda x: 1 <= x <= 12)