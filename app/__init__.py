from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

db = SQLAlchemy()
bootstrap = Bootstrap()
app = Flask(__name__)

def create_app(config_name):
    
    #setting up configurations
    app.config.from_object(config_options[config_name])

    #initializing app extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #setting up blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app