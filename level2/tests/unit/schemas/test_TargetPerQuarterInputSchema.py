from app.schemas import TargetPerQuarterInputSchema
import pytest
from marshmallow import ValidationError

def testInvalidInput():

    schema = TargetPerQuarterInputSchema()

    with pytest.raises(ValidationError):
        schema.load({
            "quarter": 4
        })

    with pytest.raises(ValidationError):
        schema.load({
            "year": "string",
            "quarter": 4
        })

def testValidInput():

    schema = TargetPerQuarterInputSchema()

    schema.load({
        "year": 2000,
        "quarter": 4
    })