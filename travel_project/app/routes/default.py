from flask import Blueprint, render_template
from sqlalchemy import select

from app.database import Session
from app.models import Travel

bp = Blueprint("default", __name__)

@bp.route('/index')
@bp.route('/')
def index():
    with Session() as session:
        query = select(Travel).where(Travel.booked == False)
        travels = session.scalars(query).all()
    return render_template('main.html', travels=travels)

@bp.route('/booked')
def booked():
    with Session() as session:
        query = select(Travel).where(Travel.booked == True)
        travels = session.scalars(query).all()
    return render_template('main.html', travels=travels, booked=1)