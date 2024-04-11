from flask import request, current_app
from app.schemas import TargetPerQuarterInputSchema
from . import trpc
from app.computing import computeRangeMetrics, isDataAvailable
from app.utils.YearMonthRange import YearMonthRange
from app.utils.schema import validate

def process(targets, input):

    yearMonthRange = YearMonthRange.fromQuarter(input["year"], input["quarter"])

    if not isDataAvailable(targets, yearMonthRange):
        return {}

    target = computeRangeMetrics(targets, yearMonthRange)
    
    target["year"] = input["year"]
    target["quarter"] = input["quarter"]
    
    return target
    
@trpc.route('/targets.perQuarter')
def targets_perQuarter():

    jsonInput = request.args.get('input')

    input, error = validate(jsonInput, TargetPerQuarterInputSchema)
    if error is not None:
        return input, error
    
    targets = current_app.config['TARGETS']
    
    return process(targets, input)