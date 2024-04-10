from app.utils.schema import validate
from marshmallow import Schema, fields
import json

def test():

    class TestSchema(Schema):
        myField = fields.Int(required=True, validate=lambda x: 1 <= x <= 10)

    input, error = validate(json.dumps({"myField":5}), TestSchema)
    assert error is None
    
    input, error = validate(json.dumps({"myField":0}), TestSchema)
    assert error == 422

    input, error = validate(json.dumps({"myOtherField":5}), TestSchema)
    assert error == 422

    input, error = validate("azez", TestSchema)
    assert error == 422

    input, error = validate(None, TestSchema)
    assert error == 400