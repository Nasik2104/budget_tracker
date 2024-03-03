from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import select, update

from app.database import Session
from app.models import Travel
from app.forms import AddForm

bp = Blueprint("travel", __name__)

@bp.route('/<int:travel_id>', methods=["GET", "POST"])
def get_travel(travel_id):
    if request.method == "POST":
        with Session() as session:
            query = select(Travel).where(Travel.id == travel_id)
            travel = session.scalars(query).one()
            travel.booked = True
            session.commit()
        return redirect(url_for('default.index'))

    with Session() as session:
        query = select(Travel).where(Travel.id == travel_id)
        travel = session.scalars(query).one()
    print(travel)
    return render_template('travel.html', travel=travel)

@bp.route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        transport = form.transport.data
        destination = form.destination.data
        departure = form.departure.data
        start = form.start.data
        end = form.end.data
        price = form.price.data
        img_link = form.img_link.data
        description = form.description.data

        with Session() as session:
            new_tour = Travel(name=name, transport=transport, destination=destination, departure=departure, start=start, end=end, price=price, img_link=img_link, description=description)
            session.add(new_tour)
            session.commit()
        return redirect(url_for('default.index'))


    return render_template('add.html', form=form)

@bp.route('/edit/<int:travel_id>', methods=["GET", "POST"])
def edit(travel_id):
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        transport = form.transport.data
        destination = form.destination.data
        departure = form.departure.data
        start = form.start.data
        end = form.end.data
        price = form.price.data
        img_link = form.img_link.data
        description = form.description.data

        query = select(Travel).where(Travel.id == travel_id)

        with Session() as session:
            tour = session.scalars(query).one_or_none()

            session.execute(update(Travel).where(Travel.id == travel_id).values(name=name, transport=transport,
                              destination=destination, departure=departure, start=start,end=end, price=price,
                              img_link=img_link, description=description))
            session.commit()
        return redirect(url_for('default.index'))
    return render_template("edit.html", form=form)

@bp.route('/delete/<int:travel_id>', methods=["GET", "POST"])
def delete(travel_id):
    query = select(Travel).where(Travel.id == travel_id)
    if request.method == "POST":
        with Session() as session:
            tour = session.scalars(query).one()
            session.delete(tour)
            session.commit()

        return redirect(    url_for('default.index'))

    with Session() as session:
        tour = session.scalars(query).one()
    return render_template('delete.html', tour=tour)

