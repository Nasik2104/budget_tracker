from flask import Flask, g

from app.db import get_db


def create_app():
    app = Flask(__name__)

    with app.app_context():
        get_db(is_server_start=True)

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    from app.categories import bp as categ_bp
    app.register_blueprint(categ_bp, url_prefix='/categories')

    from app.spendings import bp as spendings_bp
    app.register_blueprint(spendings_bp, url_prefix='/spendings')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    @app.route('/test')
    def test_page():
        return "This is a test page"

    return app