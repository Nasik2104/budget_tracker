import os

from flask import Flask, render_template

from app.database import create_db, drop_db, Session

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config["SECRET_KEY"] = os.urandom(12).hex()
    from app.routes import default_bp, travel_bp

    app.register_blueprint(default_bp, url_prefix="/")
    app.register_blueprint(travel_bp, url_prefix="/travel")


    from app import models
    create_db()

    return app