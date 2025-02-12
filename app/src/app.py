# init.py

import uuid
from flask import Flask, Blueprint
import boto3
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_login import LoginManager
from models import User

dynamodb = boto3.resource('dynamodb')


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
        return User(response['Item'])
    else:
        return None


# blueprint for the user api
user_blueprint = Blueprint('user', __name__)
app.register_blueprint(user_blueprint)

# blueprint for (conspiracy) boards api
board_blueprint = Blueprint('board', __name__)
app.register_blueprint(board_blueprint)
