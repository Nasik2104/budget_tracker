from flask import Flask
from .database import create_all, Session


def create_app():

    create_all()

    app = Flask(__name__)

    from .routes import main_bp

    app.register_blueprint(main_bp, url_prefix="/")


    return app