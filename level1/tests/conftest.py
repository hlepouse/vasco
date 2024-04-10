# This fixture is required for pytest-flask
# See https://pytest-flask.readthedocs.io/en/latest/tutorial.html#step-1-install

import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app
