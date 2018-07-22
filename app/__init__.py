from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown

from config import config

moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    from app.api import api
    api.init_app(app)

    from .main import main as main_blueprints
    app.register_blueprint(main_blueprints)

    from .model import model as model_blueprints
    app.register_blueprint(model_blueprints)

    from .repertory import repertory as repertory_blueprints
    app.register_blueprint(repertory_blueprints)

    return app