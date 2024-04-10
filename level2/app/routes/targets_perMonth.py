from flask import request, current_app
from app.schemas import TargetPerMonthInputSchema
from . import trpc
from app.computing import isDataAvailable
from app.utils.schema import validate

def process(targets, input):

    if not isDataAvailable(targets, input["year"], input["month"], input["year"], input["month"]):
        return {}

    target = targets[input["year"], input["month"]]
    
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