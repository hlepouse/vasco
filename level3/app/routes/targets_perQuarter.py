from flask import request, current_app
from app.schemas import TargetPerQuarterInputSchema
from . import trpc
from app.utils.YearMonthRange import YearMonthRange
from app.utils.schema import validate

def process(input):

    yearMonthRange = YearMonthRange.fromQuarter(input["year"], input["quarter"])

    if not current_app.computer.isDataAvailable(yearMonthRange):
        return {}

    target = current_app.computer.computeRangeMetrics(yearMonthRange)
    
    target["year"] = input["year"]
    target["quarter"] = input["quarter"]
    
    return target
    
@trpc.route('/targets.perQuarter')
def targets_perQuarter():

    jsonInput = request.args.get('input')

    input, error = validate(jsonInput, TargetPerQuarterInputSchema)
    if error is not None:
        return input, error
    
    return process(input)