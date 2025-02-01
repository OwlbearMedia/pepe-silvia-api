# main.py


from flask import Blueprint
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route('/api/')
def index():
    return 'Index'


@main.route('/api/profile')
@login_required
def profile():
    return 'Profile'
