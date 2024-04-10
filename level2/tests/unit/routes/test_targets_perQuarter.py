from app.routes.targets_perQuarter import validate, process
import json

def testValidate():

    input, error = validate(None)
    assert error == 400

    input, error = validate("qffsd")
    assert error == 422

    input, error = validate(json.dumps({
        "quarter": "aaa",
        "year": 2022
    }))
    assert error == 422

    input, error = validate(json.dumps({
        "quarter": 4,
        "year": 2022
    }))
    assert error is None

def testValidateRanges():

    input, error = validate(json.dumps({
        "quarter": 0,
        "year": 2022
    }))
    assert error == 422

    input, error = validate(json.dumps({
        "quarter": 4,
        "year": 100000
    }))
    assert error == 422

def testProcess():

    targets = {
        (2022,1): {
            "recurringRevenue": 100000,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01,
        },
        (2022,2): {
            "recurringRevenue": 100000,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01,
        },
        (2022,3): {
            "recurringRevenue": 100000,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01,
        }
    }

    assert process(targets, {"year": 2022, "quarter": 1}) == {
            "quarter": 1,
            "year": 2022,
            "recurringRevenue": 100000,
            "churnRate": 0.03,
            "downgradeRate": 0.03,
            "upgradeRate": 0.03,
        }

    assert process(targets, {"year": 2021, "quarter": 2}) == {}