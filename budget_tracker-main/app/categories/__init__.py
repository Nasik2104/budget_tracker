from flask import Blueprint

bp = Blueprint('categories', __name__, template_folder='templates', static_folder='static')

from app.categories import routes
