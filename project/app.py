from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_view():
    return render_template("index.html")

@app.route("/menu.html")
def show_menu():
    return render_template("menu.html")

if __name__ == "__main__":
    app.run()

