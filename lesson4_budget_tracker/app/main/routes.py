from flask import render_template, g,  request, redirect

from app.main import bp
from app.db import get_spending_db, get_category_db


@bp.route('/')
def get_index():
    spendings = get_spending_db().get_spendings()
    spendings_dict = []
    for spend in spendings:
        spendings_dict.append({
            "id": spend[0],
            "name": spend[1],
            "category": spend[2],
            "date": spend[3],
            "spending": spend[4],
            "is_spending": spend[5]
        })

    return render_template("main/index.html", spendings=spendings_dict)

@bp.route('/create', methods=['GET', 'POST'])
def create_spending():
    if request.method == 'GET':
        category_names = get_category_db().get_names()
        return render_template('main/create.html', names=category_names)
    else:
        name = request.form.get('name')
        category = request.form.get('category_id')
        date = request.form.get('date')
        spending = request.form.get('spend')
        is_spending = request.form.get('is_spend')

        db = get_spending_db()

        db.create_spending(name=name, category_id=category, date=date, spending=spending, is_spending=is_spending)
        return redirect('/', code=302)

@bp.route('/edit/<int:spending_id>', methods=['GET', 'POST'])
def edit_spending(spending_id):

    db = get_spending_db()
    if request.method == 'GET':
        spending = db.get_spending(id=spending_id)
        if spending:
            print(spending)
            category_names = get_category_db().get_names()
            return render_template('main/edit.html', name=spending[0][0], category=spending[0][1], date=spending[0][2], spending=spending[0][3], is_spending=spending[0][4], names=category_names)
        abort(404)
    else:
        name = request.form.get('name')
        category = request.form.get('category_id')
        date = request.form.get('date')
        spending = request.form.get('spend')
        is_spending = request.form.get('is_spend')

        db = get_spending_db()

        db.edit_spending(id=spending_id, name=name, category_id=category, date=date, spending=spending, is_spending=is_spending)
        return redirect('/', code=302)

@bp.route('/delete/<int:spending_id>', methods=['GET', 'POST'])
def delete_spending(spending_id):
    db = get_spending_db()
    if request.method == 'GET':
        spending = db.get_spending(id=spending_id)
        print(spending)
        if spending:
            return render_template('main/delete.html', name=spending[0][1], date=spending[0][3], spending=spending[0][4])
        abort(404)
    else:
        db.delete_spending(id=spending_id)
        return redirect('/', code=302)

@bp.route("/report")
def report():
    spendings = get_spending_db().get_spendings()
    spendings_dict = []
    for spend in spendings:
        spendings_dict.append({
            "id": spend[0],
            "name": spend[1],
            "category": spend[2],
            "date": spend[3],
            "spending": spend[4],
            "is_spending": spend[5]
        })

    return render_template("main/report.html",spendings=spendings_dict)

