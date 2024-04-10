from app.routes.targets_perMonth import validate, process
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

def testProcess():

    targets = {
        (2022,6): {
            "month": 6,
            "year": 2022,
            "recurringRevenue": 145000.0,
            "churnRate": 0.01,
            "downgradeRate": 0.03,
            "upgradeRate": 0.02,
        }
    }

    assert process(targets, {"year": 2022, "month": 6}) == {
            "month": 6,
            "year": 2022,
            "recurringRevenue": 145000.0,
            "churnRate": 0.01,
            "downgradeRate": 0.03,
            "upgradeRate": 0.02,
        }

    assert process(targets, {"year": 2021, "month": 6}) == {}