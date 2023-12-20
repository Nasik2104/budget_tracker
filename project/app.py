from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

DATABASE = "test.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def create_db():
    cr = sqlite3.connect(DATABASE)
    cr.execute("""
        CREATE TABLE IF NOT EXISTS orders
            (name VARCHAR(128), email VARCHAR(128), adress TEXT, pizza_name VARCHAR(32), phone VARCHAR(32), quantity INT) 
    """)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
@app.route("/index")
def index_view():
    create_db()
    return render_template("index.html", title = "Home")

data = [
            {"name": "Маргарита", "ingredients": "Сир Моцарелла, Базилік(зелень), Помідор, Кетчуп, Орегано", "price":"140 грн", "img":"https://images.ntile.app/81ffbc387a5466c10d8cb8f66dba491a446ca15d103d8595f2c50b26db4fb8faed63bf22174cc64d1885189388f98da4?width=380&quality=100"},
            {"name": "Пепероні", "ingredients": "Сир Моцарелла, Пепероні, Пармезан", "price": "130 грн"},
            {"name": "3 Сири", "ingredients": "Томатна паста, Dor Blue, Пармезан, Сир Філадельфії", "price": "125 грн"},
            {"name": "Гавайська", "ingredients": "Сир Моцарелла, Шинка, Томатна паста, Ананас консервований, Помідор", "price": "135 грн"},
            {"name": "4 сезони", "ingredients": "Сир Моцарелла, Салямі, Томатна паста, Помідор, Шинка, Гриби", "price": "150 грн"},
]

@app.route("/menu")
def show_menu():
    context = {
        "data_menu": data,
    }
    return render_template("menu.html", title="menu", **context)

@app.route("/pizza_info/", methods = ["GET"])
def show_pizza_info():

    pizzaname = request.args.get('pizzaname')
    print(pizzaname)
    return render_template("pizza_info.html", pizza_name=pizzaname, title = pizzaname, data_menu = data)

@app.route("/order", methods = ["GET", "POST"])
def order():
    pizzaname = request.args.get('pizzaname')

    if request.method == "POST":
        quantity = request.form.get("quantity")
        name = request.form.get("name")
        email = request.form.get("email")
        adress = request.form.get("adress")
        phone = request.form.get("phone")
        print(name, adress, phone, email)
        cr = get_db()
        cr.execute("""
               INSERT INTO orders (name, email, adress, pizza_name, phone, quantity) VALUES (?,?,?,?,?,?)
           """, (name, email, adress, pizzaname, phone, quantity))
        cr.commit()
        return render_template("index.html")

    else:
        return render_template("order_page.html", pizza_name=pizzaname)

@app.route("/view")
def view():
    cr = get_db().cursor()
    cr.execute("SELECT * FROM orders")
    data = cr.fetchall()

    return render_template("view.html", orders = data)

if __name__ == "__main__":
    app.run(debug=True)

