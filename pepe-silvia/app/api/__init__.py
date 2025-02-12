from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import user, board  # noqa: F401,F402,E402
