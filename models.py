import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def get_con():
    try:
        con = sql.connect(path.join(ROOT, 'database.db'))
        return con
    except:
        return False


def close_and_commit(con):
    con.commit()
    con.close()

def create_feedback(name, email, subject, message):
    con = get_con()
    cur = con.cursor()

    query = 'Insert into feedback(name, email, subject, message) values(?, ?, ?, ?)'
    cur.execute(query, (name, email, subject, message))

    close_and_commit(con)

def read_feedback():
    con = get_con()
    cur = con.cursor()

    query = 'select * from feedback'
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    con.close()

    return data

def update_feedback(name, email, subject, message):
    create_feedback(name, email, subject, message)

def delete_feedback(id):
    con = get_con()
    cur = con.cursor()

    query = 'delete from feedback where id = ?'

    cur.execute(query, (id,))
    close_and_commit(con)

def get_feedback_by_id(id):
    con = get_con()
    cur = con.cursor()

    query = 'select * from feedback where id = ?'

    cur.execute(query, (id,))
    data = cur.fetchall()
    cur.close()
    con.close()

    return data
