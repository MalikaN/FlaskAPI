from flask import Flask
from pihitakapi.resources import mysql
from flask_jwt_extended import JWTManager


def create_app(app_name='API'):  
    app = Flask(app_name)
    app.config.from_object('pihitakapi.config.BaseConfig')
    from pihitakapi.api import api_bp
    app.register_blueprint(api_bp)
    mysql.init_app(app)
    jwt = JWTManager(app)
    return app