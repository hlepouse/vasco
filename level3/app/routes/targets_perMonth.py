from flask import request, current_app
from app.schemas import TargetPerMonthInputSchema
from . import trpc
from app.computing import isDataAvailable, computeRangeMetrics
from app.utils.schema import validate
from app.utils.YearMonthRange import YearMonthRange
from app.utils.YearMonth import YearMonth

def process(targets, input):

    yearMonth = YearMonth(input["year"], input["month"])
    yearMonthRange = YearMonthRange(yearMonth, yearMonth)

    if not isDataAvailable(targets, yearMonthRange):
        return {}

    target = computeRangeMetrics(targets, yearMonthRange)
    
    target["year"] = input["year"]
    target["month"] = input["month"]
    
    return target
    
@trpc.route('/targets.perMonth')
def targets_perMonth():

    jsonInput = request.args.get('input')

    input, error = validate(jsonInput, TargetPerMonthInputSchema)
    if error is not None:
        return input, error
    
    targets = current_app.config['TARGETS']
    
    return process(targets, input)