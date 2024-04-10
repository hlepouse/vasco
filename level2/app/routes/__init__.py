# New routes have to be added here in order to be registered

from flask import Blueprint

trpc = Blueprint('trpc', __name__, url_prefix='/trpc')

from . import targets_perMonth
from . import targets_perQuarter