from flask import request, current_app
import json
from json import JSONDecodeError
from marshmallow import ValidationError
from app.schemas import TargetPerQuarterInputSchema
from . import trpc
from app.computing import computeMetrics, isDataAvailable
from app.utils import computeStartEndMonths

def validate(jsonInput):

    if jsonInput is None:
        return {"message": "No input provided"}, 400

    try:
        input = json.loads(jsonInput)
    except JSONDecodeError as e:
        return str(e), 422
    
    schema = TargetPerQuarterInputSchema()

    try:
        input = schema.load(input)
    except ValidationError as e:
        return e.messages, 422
    
    return input, None

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

    input, error = validate(jsonInput)
    if error is not None:
        return input, error
    
    targets = current_app.config['TARGETS']
    
    return process(targets, input)