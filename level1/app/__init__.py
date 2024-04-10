from flask import Flask, request
import json

def convert_percent_to_float(rate):

    return rate / 100

def preprocess_targets(json_file):

    targets_list = json.load(json_file)
    targets_dict = {}

    for target in targets_list:

        for rateKey in ["churnRate", "downgradeRate", "upgradeRate"]:
            target[rateKey] = convert_percent_to_float(target[rateKey])

        targets_dict[target["year"], target["month"]] = target

    return targets_dict

def create_app():

    app = Flask(__name__)

    with open("data/targets.json") as json_file:

        app.config['TARGETS'] = preprocess_targets(json_file)

    @app.route('/trpc/targets.perMonth')
    def targets_perMonth():

        input = json.loads(request.args.get('input'))

        return app.config['TARGETS'][input["year"], input["month"]]

    return app