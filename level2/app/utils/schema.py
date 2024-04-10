from json import JSONDecodeError
import json
from marshmallow import ValidationError

def validate(jsonInput, schemaClass):

    if jsonInput is None:
        return {"message": "No input provided"}, 400

    try:
        input = json.loads(jsonInput)
    except JSONDecodeError as e:
        return str(e), 422
    
    schema = schemaClass()

    try:
        input = schema.load(input)
    except ValidationError as e:
        return e.messages, 422
    
    return input, None