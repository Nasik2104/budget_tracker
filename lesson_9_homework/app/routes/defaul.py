from flask import Blueprint, render_template, request, redirect, flash, url_for
from sqlalchemy import select

from app.database import Session
from app.models import Pizza

bp = Blueprint("default", __name__)


@bp.route("/index")
@bp.route("/")
def index():
    with Session() as session:

        pizzas = session.query(Pizza)
    return render_template("main.html", pizzas=pizzas)

@bp.route("/add_pizza", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get('name')
        ingredients = request.form.get('ingredients')
        price = f"{request.form.get('price')} UAN"
        img = request.form.get('img')

        with Session() as session:
            new_post = Pizza(name=name, ingredients=ingredients, price=price, image_link=img)
            session.add(new_post)
            session.commit()
        return redirect(url_for('default.index'))

    return render_template('create.html')

@bp.route("/about")
def about():
    return render_template("about.html")