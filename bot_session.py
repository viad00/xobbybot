# coding=UTF-8
import sqlite3
from settings import *
import datetime

def write_error(text):
    f = open('db_errors.txt','a')
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
        cursor.execute('DELETE FROM Repair WHERE user_id=:user_id', {'user_id': user_id})
        cursor.execute('INSERT INTO Repair VALUES (:user_id, :answer, NULL)', {"user_id": user_id, "answer": answer})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Repair':
            cursor.execute('CREATE TABLE Repair(user_id TEXT, answer TEXT, type TEXT)')
            cursor.execute('INSERT INTO Repair VALUES (:user_id, :answer, NULL)', {"user_id": user_id, "answer": answer})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))


def repair_remove_query(user_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('DELETE FROM Repair WHERE user_id=:user_id', {'user_id': user_id})
    conn.commit()
    conn.close()


def repair_update_type(user_id, type):
    conn = sqlite3.connect(DATABASE)
    conn.execute('UPDATE Repair SET type=:type WHERE user_id=:user_id', {'user_id': user_id, 'type': type})
    conn.commit()
    conn.close()


def parts_write_answer(user_id, answer):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Parts WHERE user_id=:user_id', {'user_id': user_id})
        cursor.execute('INSERT INTO Parts VALUES (:user_id, :answer, NULL)', {"user_id": user_id, "answer": answer})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Parts':
            cursor.execute('CREATE TABLE Parts(user_id TEXT, answer TEXT, type TEXT)')
            cursor.execute('INSERT INTO Parts VALUES (:user_id, :answer, NULL)', {"user_id": user_id, "answer": answer})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))


def parts_update_type(user_id, type):
    conn = sqlite3.connect(DATABASE)
    conn.execute('UPDATE Parts SET type=:type WHERE user_id=:user_id', {'user_id': user_id, 'type': type})
    conn.commit()
    conn.close()


def parts_remove_query(user_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('DELETE FROM Parts WHERE user_id=:user_id', {'user_id': user_id})
    conn.commit()
    conn.close()
