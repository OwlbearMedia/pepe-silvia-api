import os
from flask import Flask
import boto3
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_login import LoginManager
from .models import User

dynamodb = boto3.resource('dynamodb')


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        table = dynamodb.Table('users')
        response = table.get_item(
            Key={
                'email': user_id,
            }
        )

        if response['Item']:
            return User(response['Item'])
        else:
            return None

    # blueprint for the user api
    from .user import auth as user_blueprint
    app.register_blueprint(user_blueprint)

    # blueprint for (conspiracy) boards api
    from .board import board as board_blueprint
    app.register_blueprint(board_blueprint)

    return app
