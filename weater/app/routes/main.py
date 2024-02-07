import os

from flask import render_template, request, redirect
from flask.blueprints import Blueprint

import requests

bp = Blueprint("default", __name__)

wea = "47ac3b0e8423e801dd60854c54b2f58f"
@bp.route('/', methods=["GET"])
def main_page():
    value = request.args.get('q')
    weather = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={value}&appid={wea}&units=metric"
    )
    data = weather.json()
    return render_template("main.html", data=data)