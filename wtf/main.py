from flask import Flask, template_rendered, request

app = Flask(__name__)

@app.route('/search/')
def flask_search():
    return template_rendered('search.html')

@app.route('/dosearch/')
def flask_dosearch():
    s=request.args.get("s")
    return f'Пошук по {s}'

app.run(debug=True)