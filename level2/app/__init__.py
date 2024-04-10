from flask import Flask
import json
from app.preprocessing import preprocessTargets
from app.routes import trpc
import os
from dotenv import load_dotenv

# Factory method to create app
# The snake case is required for Flask
def create_app():

    load_dotenv()

    app = Flask(__name__)

    with open(os.getenv('PATH_TARGETS')) as jsonFile:

        targetsList = json.load(jsonFile)
    
    app.config['TARGETS'] = preprocessTargets(targetsList)

    app.register_blueprint(trpc)

    return app