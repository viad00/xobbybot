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


def get_all_sales():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT ROWID, description FROM Sales')
    except Exception as e:
        if str(e.message) == 'no such table: Sales':
            cursor.execute('CREATE TABLE Sales(description TEXT, text TEXT, image_src TEXT)')
            conn.commit()
            conn.close()
            return [(1, u'В данный момент у нас нет акций(')]
        else:
            write_error(str(e))
            return [(1, u'В данный момент у нас нет акций(')]
    sales = cursor.fetchall()
    if len(sales) > 0:
        return sales
    else:
        return [(1, u'В данный момент у нас нет акций(')]


def get_sale_by_id(sale_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT text, image_src FROM Sales WHERE ROWID=:sale_id', {'sale_id': sale_id})
    return cursor.fetchone()


def tools_write_db(user_id, answer):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Tools WHERE user_id=:user_id', {'user_id': user_id})
        cursor.execute('INSERT INTO Tools VALUES (:user_id, :answer)', {"user_id": user_id, "answer": answer})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Tools':
            cursor.execute('CREATE TABLE Tools(user_id TEXT, answer TEXT)')
            cursor.execute('INSERT INTO Tools VALUES (:user_id, :answer)', {"user_id": user_id, "answer": answer})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))


def tyres_write_size(user_id, size):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Tyres_Query WHERE user_id=:user_id', {'user_id': user_id})
        cursor.execute('INSERT INTO Tyres_Query VALUES (:user_id, :size)', {'user_id': user_id, 'size': size})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Tools':
            cursor.execute('CREATE TABLE Tyres_Query(user_id TEXT, size TEXT)')
            cursor.execute('INSERT INTO Tyres_Query VALUES (:user_id, :size)', {'user_id': user_id, 'size': size})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))
