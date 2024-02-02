from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.main import bp

    app.register_blueprint(bp, url_prefix='/')

    return app