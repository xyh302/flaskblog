from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_moment import Moment


bootstrap = Bootstrap()
db = MongoEngine()
login = LoginManager()
login.login_view = 'auth.login'
moment = Moment()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    db.init_app(app)
    login.init_app(app)
    moment.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.error import bp as error_bp
    app.register_blueprint(error_bp)

    from app.article import bp as article_bp
    app.register_blueprint(article_bp)

    from app.post import bp as post_bp
    app.register_blueprint(post_bp)

    return app


#from app import models
