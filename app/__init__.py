from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from flask_moment import Moment
from config import Config


db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    CsrfProtect(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) #,url_prefix='/blog'

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .news import news as news_blueprint
    app.register_blueprint(news_blueprint, url_prefix='/news')

    from .data import data as news_blueprint
    app.register_blueprint(news_blueprint, url_prefix='/data')

    return app

app = create_app()
