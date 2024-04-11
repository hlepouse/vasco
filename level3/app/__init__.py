from flask import Flask
from app.routes import trpc
import os
from dotenv import load_dotenv
from app.Computer import Computer
import json

# The app inherits from basic Flask app
# All computations are perfomed by the Computer object, stored as member of the class
class VascoApp(Flask):

    def __init__(self):

        Flask.__init__(self, __name__)

        # The reading of the data file is not performed in Computer, it makes the class easier to test
        with open(os.getenv('PATH_TARGETS')) as jsonFile:
            targetsList = json.load(jsonFile)

        self.computer = Computer(
            targetsList = targetsList,
            rateMetrics = os.getenv('RATE_METRICS').split(","),
            defaultPreviousRecurringRevenue = float(os.getenv('DEFAULT_PREVIOUS_RECURRING_REVENUE'))
        )

# Factory method to create app
# The snake case is required for Flask
def create_app():

    load_dotenv() # This must be called explicitely for pytest

    app = VascoApp()

    app.register_blueprint(trpc)

    return app