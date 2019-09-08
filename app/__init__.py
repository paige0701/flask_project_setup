from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.view.booking_view import booking_view

db = SQLAlchemy()

def create_app(config_name):

    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_name)
    app.register_blueprint(booking_view)

    from app import models

    db.init_app(app)

    return app

