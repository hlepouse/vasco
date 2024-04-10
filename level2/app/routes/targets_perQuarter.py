from flask import request, current_app
from app.schemas import TargetPerQuarterInputSchema
from . import trpc
from app.computing import computeMetrics, isDataAvailable
from app.utils.yearMonth import computeStartEndMonths
from app.utils.schema import validate

def process(targets, input):

    startMonth, endMonth = computeStartEndMonths(input["quarter"])

    if not isDataAvailable(targets, input["year"], startMonth, input["year"], endMonth):
        return {}

    target = computeMetrics(targets, input["year"], startMonth, input["year"], endMonth)
    
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