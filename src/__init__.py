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

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        return User.get(email)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5328)

    return app
