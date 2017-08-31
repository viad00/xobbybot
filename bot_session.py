# coding=UTF-8
import sqlite3
from settings import *


def check_session(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT route FROM Users WHERE user_id=:userid', {"userid": user_id})
    except Exception as e:
        if str(e.message) == 'no such table: Users':
            cursor.execute('CREATE TABLE Users(user_id TEXT, route TEXT)')
        else:
            print str(e)
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
