from flask import render_template, request, redirect, abort

from app.spendings import bp
from app.db import get_spending_db, get_category_db


@bp.route('/')
def get_spendings():
    spendings = get_spending_db().get_spendings()
    spendings_dict = []
    for spending in spendings:
        spendings_dict.append({
            "id": spending[0],
            "name": spending[1],
            "category_id": spending[2],
            "spend_date": spending[3],
            "spendings": spending[4],
            "is_spending": spending[5]
        })
    return render_template('spendings/index.html', spendings_dict=spendings_dict)


@bp.route('/create', methods=['GET', 'POST'])
def create_spending():
    categories = get_category_db().get_categories()
    cats_names_dict = {}
    for category in categories:
        cats_names_dict[category[0]] = category[1]
    if request.method == 'GET':
        return render_template('spendings/create.html', categories_names=cats_names_dict)
    else:
        name = request.form.get('name')
        category_id = request.form.get('category_id')
        spend_date = request.form.get('spend_date')
        spending = request.form.get('spendings')
        is_spending = request.form.get('is_spending')
        db = get_spending_db()

        db.create_spending(name=name, category_id=category_id, spend_date=spend_date, spending=spending, is_spending=is_spending)
        return redirect('/spendings', code=302)


@bp.route('/edit/<int:spending_id>', methods=['GET', 'POST'])
def edit_spending(spending_id):
    db = get_spending_db()
    if request.method == 'GET':
        spending = db.get_spending(id=spending_id)
        if spending:
            print(spending)
            return render_template('spendings/edit.html', name=spending[0], description=spending[1], color=spending[2])
        abort(404)
    else:
        name = request.form.get('name')
        category_id = request.form.get('category_id')
        spend_date = request.form.get('spend_date')
        spending = request.form.get('spendings')
        is_spending = request.form.get('is_spending')

        db.edit_spending(id=spending_id, name=name, category_id=category_id, spend_date=spend_date, spending=spending, is_spending=is_spending)
        return redirect('/spendings', code=302)


@bp.route('/delete/<int:spending_id>', methods=['GET', 'POST'])
def delete_spending(spending_id):
    db = get_spending_db()
    if request.method == 'GET':
        spending = db.get_spending(id=spending_id)
        if spending:
            return render_template('spendings/delete.html', name=spending[0], category_id=spending[1], spend_date=spending[2], spending=spending[3], is_spending=spending[4])
        abort(404)
    else:
        db.delete_spending(id=spending_id)
        return redirect('/spendings', code=302)
