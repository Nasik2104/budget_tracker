import logging

from flask import Blueprint, render_template, request, redirect

from app.db import add_question, get_questions, get_answer

bp = Blueprint("tests", __name__)

filename = "data.txt"


@bp.route("/")
def root():
    poll_data = get_questions()
    poll_data = [dict(row) for row in poll_data]
    return render_template("poll.html", data=poll_data, number_of_ques=len(poll_data))


@bp.route("/add_test", methods=["GET", "POST"])
def add_test():
    if request.method == "GET":
        return render_template("add_test.html")
    else:
        number_of_ques = int(request.form.get("numberOfQuestions"))
        for number in range(1, number_of_ques+1):
            question = request.form.get(f"question{number}")
            answers = request.form.get(f"answers{number}")
            correct = request.form.get(f"correct{number}")
            add_question(question, answers, correct)
        return redirect("/")


@bp.route("/poll")
def poll():

    number_of_ques = request.args.get('numberOfQues', "NOTHING")
    correct = 0
    for key, value in request.args.items():
        if "field" in key:
            question_number = key.split('_')[1]
            user_answer = value

            answer = get_answer(question_number)
            print(user_answer, answer)

            if user_answer == answer[0][0]:
                correct += 1
             # переробити thankyou.html під це все діло
    # return render_template("thankyou.html", data=poll_data, votes=vote)
    return render_template("thankyou.html", correct=correct, number_of_ques=number_of_ques)