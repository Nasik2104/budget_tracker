import sqlite3

with sqlite3.connect("app.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS test (question TEXT UNIQUE, answers TEXT, correct TEXT)")
    conn.commit()

    print("powfpos")

def add_question(question, answers, correct):
    msg = ""
    with sqlite3.connect("app.db") as conn:
        try:
            cr = conn.cursor()
            cr.execute("INSERT INTO test (question, answers, correct) VALUES (?, ?, ?)",
                       (question, answers, correct))
            conn.commit()
            msg = "Record success added"
        except Exception as e:
            conn.rollback()
            print(e)
            msg = "Error in insert operation"
    print(msg)
    return msg


def get_questions():
    res = None
    with sqlite3.connect("app.db") as conn:
        conn.row_factory = sqlite3.Row
        cr = conn.cursor()
        cr.execute("SELECT * FROM test")
        res = cr.fetchall()
        print(res)
    return res

def get_answer(question):
    answer = None
    with sqlite3.connect('app.db') as conn:
        cr = conn.cursor()
        cr.execute("SELECT correct FROM test WHERE question = ?", (question,))
        answer = cr.fetchall()
    return answer
