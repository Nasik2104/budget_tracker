from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, IntegerField, URLField, DateField

class AddForm(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired()])
    description = StringField("Description", validators=[validators.DataRequired()])
    transport = SelectField("Transport", choices=['Train', 'Plane', 'Bus'], validators=[validators.DataRequired()])
    destination = StringField("Destination", validators=[validators.DataRequired()])
    departure = StringField("Departure", validators=[validators.DataRequired()])
    start = DateField("Start Date", validators=[validators.DataRequired()])
    end = DateField("End Date", validators=[validators.DataRequired()])
    price = IntegerField("Price", validators=[validators.DataRequired()])
    img_link = URLField("Image Link", validators=[validators.DataRequired()])
