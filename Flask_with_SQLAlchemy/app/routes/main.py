from flask import render_template
from flask.blueprints import Blueprint

from Flask_with_SQLAlchemy.app.database import Session
from Flask_with_SQLAlchemy.app.models import Product, Suplier, ProductType

from sqlalchemy import select

bp = Blueprint("default", __name__)


@bp.route('/')
def main():
    with Session() as session:
        products = session.query(Product)
        print(products)
    return render_template("main.html", products=products)

@bp.route('/types')
def types():
    with Session() as session:
        types = session.query(ProductType)

    return render_template("types.html", types=types)

@bp.route('/supliers')
def supliers():
    with Session() as session:
        suppliers = session.query(Suplier)

    return render_template("suppliers.html", suppliers=suppliers)
