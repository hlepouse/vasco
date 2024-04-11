from flask import request, current_app
from app.schemas import TargetPerMonthInputSchema
from . import trpc
from app.utils.schema import validate
from app.utils.YearMonthRange import YearMonthRange
from app.utils.YearMonth import YearMonth

def process(input):

    yearMonth = YearMonth(input["year"], input["month"])
    yearMonthRange = YearMonthRange(yearMonth, yearMonth)

    if not current_app.computer.isDataAvailable(yearMonthRange):
        return {}

    target = current_app.computer.computeRangeMetrics(yearMonthRange)
    
    target["year"] = input["year"]
    target["month"] = input["month"]
    
    return target
    
@trpc.route('/targets.perMonth')
def targets_perMonth():

    jsonInput = request.args.get('input')

    input, error = validate(jsonInput, TargetPerMonthInputSchema)
    if error is not None:
        return input, error
    
    return process(input)