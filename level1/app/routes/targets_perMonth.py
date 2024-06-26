from flask import request, current_app
import json
from json import JSONDecodeError
from marshmallow import ValidationError
from app.schemas import TargetPerMonthInputSchema
from . import trpc

def validate(jsonInput):

    if jsonInput is None:
        return {"message": "No input provided"}, 400

    try:
        input = json.loads(jsonInput)
    except JSONDecodeError as e:
        return str(e), 422
    
    schema = TargetPerMonthInputSchema()

    try:
        input = schema.load(input)
    except ValidationError as e:
        return e.messages, 422
    
    return input, None

def process(targets, input):

    target = targets.get((input["year"], input["month"]))

    if target is None:
        return {}
    
    return target
    
@trpc.route('/targets.perMonth')
def targets_perMonth():

    jsonInput = request.args.get('input')

    input, error = validate(jsonInput)
    if error is not None:
        return input, error
    
    targets = current_app.config['TARGETS']
    
    return process(targets, input)