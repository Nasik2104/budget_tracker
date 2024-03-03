import flask
import flask_wtf
import wtforms


class SubcriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name")
    email = wtforms.StringField("Email")
    color = wtforms.ColorField("Color")
    submit = wtforms.SubmitField("Send")


class IcecreamForm(flask_wtf.FlaskForm):
    tastes = wtforms.SelectField("Tastes")
    topping = wtforms.SelectMultipleField("Topping")
    cup_size = wtforms.RadioField("Cup size")
    submit = wtforms.SubmitField("Send")

class RegistrationForm(flask_wtf.FlaskForm):
    email = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")
    submit = wtforms.SubmitField("Send")
    remember = wtforms.BooleanField("Rememeber me")

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = "NASIK"

@app.route("/subscribe/", methods=["GET", "POST"])
def subscribe():
    form = SubcriptionForm()
    if flask.request.method == "GET":
        return flask.render_template("subscribe.html", form=form)
    return form.name.data

@app.route("/ice/", methods=["GET", "POST"])
def ice():
    form = IcecreamForm()
    form.tastes.choices = [("vanila", "vanila"), ("choko", "choko"),("mango", "mango"),("lemon","banan")]
    form.topping.choices = [("cofee", "cofee"), ("strawbery", "strawbery")]
    form.cup_size.choices = [("little", "little"), ("medium", "medium"), ("big", "big")]

    if flask.request.method == "GET":
        return flask.render_template("ice.html", form=form)
    return form.tastes.data


@app.route("/ice_bonus/", methods=["GET", "POST"])
def ice_bonus():
    form = IcecreamForm()
    form.tastes.choices = [("vanila", "vanila"), ("gold", "gold"),("kiwi", "kiwi"),("lemon","banan")]
    form.topping.choices = [("kiwi", "kiwi"), ("strawbery", "strawbery")]
    form.cup_size.choices = [("little", "little"), ("medium", "medium"), ("big", "big"), ("XXL", "XXL")]

    if flask.request.method == "GET":
        return flask.render_template("ice.html", form=form)
    return form.tastes.data

@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if flask.request.method == "GET":
        return flask.render_template("registration.html", form=form)
    return form.email.data

app.run(debug=True, port=3000)