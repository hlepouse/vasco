from flask import Flask
import json
from app.preprocessing import preprocessTargets
from app.routes import trpc

# Factory method to create app
# The snake case is required for Flask
def create_app():

    app = Flask(__name__)

    with open("data/targets.json") as jsonFile:

        targetsList = json.load(jsonFile)
    
    app.config['TARGETS'] = preprocessTargets(targetsList)

    app.register_blueprint(trpc)

    return app