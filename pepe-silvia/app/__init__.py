import uuid
from flask import Flask
import boto3
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_login import LoginManager
from .models import UserModel

dynamodb = boto3.resource('dynamodb')


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    app.config['SECRET_KEY'] = uuid.uuid4().hex

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        table = dynamodb.Table('users')
        response = table.get_item(
            Key={'email': user_id}
        )

        if 'Item' in response:
            return UserModel(response['Item'])
        else:
            return None

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
