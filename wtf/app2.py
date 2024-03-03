import flask
import flask_wtf
import wtforms

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = "Kostya"

def is_luggage_weight_valid(form, field):
    if field.data > 30:
        raise wtforms.validators.ValidationError("Weight is too big")


class LuggageForm(flask_wtf.FlaskForm):
    surname = wtforms.StringField("Surname", validators=[wtforms.validators.InputRequired()])
    name = wtforms.StringField("Name", validators=[wtforms.validators.InputRequired()])
    pass_id = wtforms.IntegerField("Password #", validators=[wtforms.validators.InputRequired()])
    luggage_weight = wtforms.IntegerField("Weight luggage", validators=[wtforms.validators.InputRequired(),
                                                                        is_luggage_weight_valid])
    submit = wtforms.SubmitField("Register", validators=[wtforms.validators.InputRequired()])


@app.route("/luggage/", methods = ["GET", "POST"])
def luggage():
    form = LuggageForm()
    if flask.request.method == "GET":
        return flask.render_template("luggage.html", form=form)
    if form.validate_on_submit():
        return 'ok'
    else:
        print(f"[{__name__}] ERROR: {form.errors}")
        return f"{form.errors} - not valid"

app.run(debug=True, port=5000)