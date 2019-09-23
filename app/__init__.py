from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    db.init_app(app)
    app.config.from_object(DevConfig)
    login_manager.init_app(app)
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
