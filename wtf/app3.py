import flask
import flask_wtf
import wtforms
import json

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = "Nasik"


@app.route("/test")
def test():
    with open('users.json') as file:
        users = json.load(file)
        for user in users:
            print(user)
        return flask.jsonify(users)

app.run(debug=True, port=8000)