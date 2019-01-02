

"""
Main file.
"""
from flask import Flask
from app.api.v1.views.queston_views import version1
from instance.config import app_config



def create_app(config_name):
    """
    Create app.
    """
    app = Flask(__name__, instance_relative_config=True)
    #app.url_map.strict_slashes = False
    app.register_blueprint(version1)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app
