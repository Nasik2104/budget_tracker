from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_view():
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

if __name__ == "__main__":
    app.run(debug=True)

