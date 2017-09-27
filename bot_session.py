# coding=UTF-8
# import sqlite3
import pyodbc
from settings import *
import datetime

database_connector = pyodbc.connect # sqlite3.connect

def write_error(text):
    f = open('db_errors.txt', 'a')
    f.write(str(datetime.datetime.now()) + ': ' + text + '\n')
    f.close()


def check_session(user_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT route FROM Users WHERE user_id=?', user_id)
    except Exception as e:
        write_error(str(e))
        cursor.execute('CREATE TABLE Users(user_id VARCHAR(50), route VARCHAR(100))')
        conn.commit()
        conn.close()
        return False
    if len(cursor.fetchall()) > 0:
        conn.close()
        return True
    conn.close()
    return False


def block_user(user_id, route):
    conn = database_connector(DATABASE)
    conn.execute('INSERT INTO Users(user_id, route) VALUES (?, ?)', user_id, route)
    conn.commit()
    conn.close()


def getRoute(user_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT route FROM Users WHERE user_id=?', user_id)
    result = cursor.fetchone()
    return str(result[0])


def unblock_user(user_id):
    conn = database_connector(DATABASE)
    conn.execute('DELETE FROM Users WHERE user_id=?', user_id)
    conn.commit()
    conn.close()


def test_start(user_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Running_Tests(user_id, test_id, score) VALUES (?, 0, 0)', user_id)
    except Exception as e:
        write_error(str(e))
        cursor.execute('CREATE TABLE Running_Tests(user_id VARCHAR(50), test_id INTEGER, score INTEGER)')
    conn.commit()
    conn.close()


def test_get_question(quest_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    ret = [u'', b'']
    try:
        cursor.execute('SELECT text, attach FROM Questions WHERE quest_id=?', quest_id)
        ret = cursor.fetchone()
        if len(ret) < 1:
            ret = ret = [u'NOMORE', b'']
    except Exception as e:
        write_error(str(e))
        try:
            cursor.execute('CREATE TABLE Questions(quest_id INTEGER, text NVARCHAR(2000), attach VARBINARY(MAX), answer INTEGER, value INTEGER)')
        except Exception:
            pass
        ret = [u'NOMORE', b'']
        conn.commit()
    conn.close()
    return ret


def test_get_answer_value(quest_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT answer, value FROM Questions WHERE quest_id=?', quest_id)
    ret = cursor.fetchone()
    conn.close()
    return ret


def test_get_current_test_score(user_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT test_id, score FROM Running_Tests WHERE user_id=?', user_id)
    ret = cursor.fetchone()
    conn.close()
    return ret


def test_set_question_score(user_id, test_id, score):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('UPDATE Running_Tests SET test_id=?, score=? WHERE user_id=?', test_id, score, user_id)
    conn.commit()
    conn.close()


def test_del(user_id):
    conn = database_connector(DATABASE)
    conn.execute('DELETE FROM Running_Tests WHERE user_id=?', user_id)
    conn.commit()
    conn.close()


def test_get_max_score():
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(value) FROM Questions WHERE text IS NOT NULL')
    ret = cursor.fetchone()
    conn.close()
    return ret[0]


# TODO: Needs revise
def check_admin(user_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT user_id FROM Admins WHERE user_id=:user_id', {'user_id': user_id})
    except Exception as e:
        if str(e.message) == 'no such table: Admins':
            cursor.execute('CREATE TABLE Admins(user_id TEXT)')
            cursor.execute('INSERT INTO Admins VALUES (:user_id)', {'user_id': user_id})
        else:
            write_error(str(e))
        conn.commit()
        conn.close()
        return False
    if len(cursor.fetchall()) > 0:
        conn.close()
        return True
    conn.close()
    return False


def admins_get_all():
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT ROWID, user_id FROM Admins')
    except Exception as e:
        write_error(str(e))
        return [(1, u'Нет администраторов')]
    sales = cursor.fetchall()
    if len(sales) > 0:
        return sales
    else:
        return [(1, u'Нет администраторов')]


def admin_del_by_id(row_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Admins WHERE ROWID=:row_id', {'row_id': row_id})
        conn.commit()
        conn.close()
    except Exception as e:
        write_error(str(e))


def add_admin(user_id):
    conn = database_connector(DATABASE)
    conn.execute('INSERT INTO Admins VALUES (:user_id)', {'user_id': user_id})
    conn.commit()
    conn.close()
