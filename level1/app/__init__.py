from flask import Flask, request
import json
from json import JSONDecodeError
from marshmallow import Schema, fields, ValidationError

def convertPercentToFloat(rate):

    return rate / 100

def isRateKey(key):

    return key.endswith("Rate")

def preprocessTargets(targetsList):

    targetsDict = {}

    for target in targetsList:

        for targetKey in target.keys():

            if isRateKey(targetKey):
                target[targetKey] = convertPercentToFloat(target[targetKey])

        targetsDict[target["year"], target["month"]] = target

    return targetsDict

class TargetPerMonthInputSchema(Schema):
    year = fields.Int(required=True)
    month = fields.Int(required=True)

# Factory method to create app
# The snake case is required for Flask
def create_app():

    app = Flask(__name__)

    with open("data/targets.json") as jsonFile:

        targetsList = json.load(jsonFile)
    
    app.config['TARGETS'] = preprocessTargets(targetsList)

    @app.route('/trpc/targets.perMonth')
    def targetsPerMonth():

        jsonInput = request.args.get('input')

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

        return app.config['TARGETS'][input["year"], input["month"]]

    return app