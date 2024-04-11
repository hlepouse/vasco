from app.TargetsRoute import TargetsRoute
from marshmallow import Schema, fields
import json

def test():

    class TestSchema(Schema):
        myField = fields.Int(required=True, validate=lambda x: 1 <= x <= 10)

    input, error = TargetsRoute().validate(json.dumps({"myField":5}), TestSchema)
    assert error is None
    
    input, error = TargetsRoute().validate(json.dumps({"myField":0}), TestSchema)
    assert error == 422

    input, error = TargetsRoute().validate(json.dumps({"myOtherField":5}), TestSchema)
    assert error == 422

    input, error = TargetsRoute().validate("azez", TestSchema)
    assert error == 422

    input, error = TargetsRoute().validate(None, TestSchema)
    assert error == 400