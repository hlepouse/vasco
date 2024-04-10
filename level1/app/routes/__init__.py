from flask import Blueprint

trpc = Blueprint('trpc', __name__, url_prefix='/trpc')

from . import targets_perMonth