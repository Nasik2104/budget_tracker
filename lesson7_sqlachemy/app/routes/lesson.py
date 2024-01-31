from flask import render_template, request
from flask.blueprints import Blueprint
from sqlalchemy import select

from lesson7_sqlachemy.app.database import Session
from lesson7_sqlachemy.app.models import Lesson

bp = Blueprint('lesson', __name__)

@bp.route('/', methods=["POST", "GET"])
def lesson_add():
    with Session() as session:
        if request.method == "POST":
            new_lesson = Lesson(title=request.form.get("name"))
            session.add(new_lesson)
            session.commit()

        lessons = session.query(Lesson).all()
        print(lessons)
    return render_template("/lesson/managment.html", lessons=lessons)

@bp.route('/<int:id>', methods=["GET"])
def lesson_get(id):
    with Session() as session:
        query = select(Lesson).where(Lesson.id == id)
        print(query)
        data = session.scalars(query).first()
    return render_template("/lesson/get_data.html", content=data)