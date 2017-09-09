# coding=UTF-8
import sqlite3
from settings import *
import datetime

def write_error(text):
    f = open('db_errors.txt','w')
    f.write(str(datetime.datetime.now()) + ': ' + text + '\n')
    f.close()


def check_session(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT route FROM Users WHERE user_id=:userid', {"userid": user_id})
    except Exception as e:
        if str(e.message) == 'no such table: Users':
            cursor.execute('CREATE TABLE Users(user_id TEXT, route TEXT)')
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


def block_user(user_id, route):
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO Users VALUES (:user_id, :route)', {"user_id": user_id, "route": route})
    conn.commit()
    conn.close()


def getRoute(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT route FROM Users WHERE user_id=:userid', {"userid": user_id})
    result = cursor.fetchone()
    return str(result[0])


def unblock_user(user_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('DELETE FROM Users WHERE user_id=:userid', {"userid": user_id})
    conn.commit()
    conn.close()


def repair_write_answer(user_id, answer):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Repair VALUES (:user_id, :answer, NULL)', {"userid": user_id, "answer": answer})
    except Exception as e:
        if str(e.message) == 'no such table: Repair':
            cursor.execute('CREATE TABLE Repair(user_id TEXT, answer TEXT, type TEXT)')
            cursor.execute('INSERT INTO Repair VALUES (:user_id, :answer, NULL)', {"userid": user_id, "answer": answer})
        else:
            write_error(str(e))
            return ''
