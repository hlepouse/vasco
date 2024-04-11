from flask import request, current_app
from app.schemas import TargetPerMonthInputSchema
from . import trpc
from app.utils.YearMonthRange import YearMonthRange
from app.utils.YearMonth import YearMonth
from app.TargetsRoute import TargetsRoute

class TargetsRoutePerMonth(TargetsRoute):

    def computeYearMonthRange(self, input):
        yearMonth = YearMonth(input["year"], input["month"])
        return YearMonthRange(yearMonth, yearMonth)
    
@trpc.route('/targets.perMonth')
def targets_perMonth():

    jsonInput = request.args.get('input')

    input, error = TargetsRoutePerMonth().validate(jsonInput, TargetPerMonthInputSchema)
    if error is not None:
        return input, error
    
    return TargetsRoutePerMonth().process(current_app.computer, input)