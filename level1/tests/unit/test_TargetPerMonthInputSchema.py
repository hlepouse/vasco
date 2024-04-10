from app import TargetPerMonthInputSchema
import pytest
from marshmallow import ValidationError

def testInvalidInput():

    schema = TargetPerMonthInputSchema()

    with pytest.raises(ValidationError):
        schema.load({
            "month": 4
        })

    with pytest.raises(ValidationError):
        schema.load({
            "year": "string",
            "month": 4
        })

def testValidInput():

    schema = TargetPerMonthInputSchema()

    schema.load({
        "year": 2000,
        "month": 4
    })