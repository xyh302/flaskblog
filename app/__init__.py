from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

bootstrap = Bootstrap()
db = MongoEngine()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    db.init_app(app)
    login.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
