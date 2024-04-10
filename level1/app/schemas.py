from marshmallow import Schema, fields

class TargetPerMonthInputSchema(Schema):
    year = fields.Int(required=True)
    month = fields.Int(required=True)