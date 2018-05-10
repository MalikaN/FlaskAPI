from flask import Flask
from surveyapi.resources import mysql

def create_app(app_name='SURVEY_API'):  
    app = Flask(app_name)
    app.config.from_object('surveyapi.config.BaseConfig')

    from surveyapi.api import api_bp
    app.register_blueprint(api_bp)
    mysql.init_app(app)
    return app