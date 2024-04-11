# This is the base abstract class for targets perMonth and perQuarter

from json import JSONDecodeError
import json
from marshmallow import ValidationError
from app.utils.YearMonthRange import YearMonthRange
from app.utils.YearMonth import YearMonth

class TargetsRoute:

    def validate(self, jsonInput, schemaClass):

        if jsonInput is None:
            return {"message": "No input provided"}, 400

        try:
            input = json.loads(jsonInput)
        except JSONDecodeError as e:
            return str(e), 422
        
        schema = schemaClass()

        try:
            input = schema.load(input)
        except ValidationError as e:
            return e.messages, 422
        
        return input, None
    
    # This is an abstract method that must be implemented in children classes
    def computeYearMonthRange(self, input):
        return None

    def process(self, computer, input):

        yearMonthRange = self.computeYearMonthRange(input)

        if not computer.isDataAvailable(yearMonthRange):
            return {}

        target = computer.computeRangeMetrics(yearMonthRange)
        
        # The | operator merges two dictionaries
        return target | input