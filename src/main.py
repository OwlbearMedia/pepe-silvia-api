from flask import Blueprint
# from . import dynamodb


main = Blueprint('main', __name__)


@main.route('/api/')
def index():
    return 'Index'


@main.route('/api/profile')
def profile():
    return 'Profile'
