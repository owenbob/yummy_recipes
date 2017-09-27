# initial.py

#third party import
from flask import Blueprint, Flask


# Local import
from recipeCrud import RecipeCrud


# Initialization
main = Blueprint('main', __name__)

import views
from config import config


# Application factory
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.recipeCrud = RecipeCrud()

    return app