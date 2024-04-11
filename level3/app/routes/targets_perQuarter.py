from flask import request, current_app
from app.schemas import TargetPerQuarterInputSchema
from . import trpc
from app.utils.YearMonthRange import YearMonthRange
from app.TargetsRoute import TargetsRoute

class TargetsRoutePerQuarter(TargetsRoute):

    def computeYearMonthRange(self, input):
        return YearMonthRange.fromQuarter(input["year"], input["quarter"])
    
@trpc.route('/targets.perQuarter')
def targets_perQuarter():

    jsonInput = request.args.get('input')

    input, error = TargetsRoutePerQuarter().validate(jsonInput, TargetPerQuarterInputSchema)
    if error is not None:
        return input, error
    
    return TargetsRoutePerQuarter().process(current_app.computer, input)