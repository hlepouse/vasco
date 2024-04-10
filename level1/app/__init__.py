from flask import Flask

def create_app():

    app = Flask(__name__)

    @app.route('/trpc/targets.perMonth')
    def targets_perMonth():

        return {}

    return app