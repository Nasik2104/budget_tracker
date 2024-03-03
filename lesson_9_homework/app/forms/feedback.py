from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    rating = RadioField('Rating',
                       choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')],
                       validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('')