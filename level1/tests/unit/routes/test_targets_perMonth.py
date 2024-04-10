from app.routes.targets_perMonth import validate
import json

def testValidate():

    input, error = validate(None)
    assert error == 400

    input, error = validate("qffsd")
    assert error == 422

    input, error = validate(json.dumps({
        "month": "aaa",
        "year": 2022
    }))
    assert error == 422

    input, error = validate(json.dumps({
        "month": 4,
        "year": 2022
    }))
    assert error is None

def testValidateRanges():

    input, error = validate(json.dumps({
        "month": 0,
        "year": 2022
    }))
    assert error == 422

    input, error = validate(json.dumps({
        "month": 4,
        "year": 100000
    }))
    assert error == 422