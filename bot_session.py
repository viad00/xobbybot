# coding=UTF-8
import sqlite3
from settings import *
import datetime

database_connector = sqlite3.connect

def write_error(text):
    f = open('db_errors.txt', 'a')
    f.write(str(datetime.datetime.now()) + ': ' + text + '\n')
    f.close()


def check_session(user_id):
    conn = database_connector(DATABASE)
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
    conn = database_connector(DATABASE)
    conn.execute('INSERT INTO Users VALUES (:user_id, :route)', {"user_id": user_id, "route": route})
    conn.commit()
    conn.close()


def getRoute(user_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT route FROM Users WHERE user_id=:userid', {"userid": user_id})
    result = cursor.fetchone()
    return str(result[0])


def unblock_user(user_id):
    conn = database_connector(DATABASE)
    conn.execute('DELETE FROM Users WHERE user_id=:userid', {"userid": user_id})
    conn.commit()
    conn.close()


def repair_write_answer(user_id, answer):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Repair WHERE user_id=:user_id', {'user_id': user_id})
        cursor.execute('INSERT INTO Repair VALUES (:user_id, :answer, NULL)', {"user_id": user_id, "answer": answer})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Repair':
            cursor.execute('CREATE TABLE Repair(user_id TEXT, answer TEXT, type TEXT)')
            cursor.execute('INSERT INTO Repair VALUES (:user_id, :answer, NULL)',
                           {"user_id": user_id, "answer": answer})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))


def repair_remove_query(user_id):
    conn = database_connector(DATABASE)
    conn.execute('DELETE FROM Repair WHERE user_id=:user_id', {'user_id': user_id})
    conn.commit()
    conn.close()


def repair_update_type(user_id, type):
    conn = database_connector(DATABASE)
    conn.execute('UPDATE Repair SET type=:type WHERE user_id=:user_id', {'user_id': user_id, 'type': type})
    conn.commit()
    conn.close()


def parts_write_answer(user_id, answer):
    conn = database_connector(DATABASE)
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
    conn = database_connector(DATABASE)
    conn.execute('UPDATE Parts SET type=:type WHERE user_id=:user_id', {'user_id': user_id, 'type': type})
    conn.commit()
    conn.close()


def parts_remove_query(user_id):
    conn = database_connector(DATABASE)
    conn.execute('DELETE FROM Parts WHERE user_id=:user_id', {'user_id': user_id})
    conn.commit()
    conn.close()


def get_all_sales():
    conn = database_connector(DATABASE)
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
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT text, image_src FROM Sales WHERE ROWID=:sale_id', {'sale_id': sale_id})
    return cursor.fetchone()


def sale_del_by_id(sale_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Sales WHERE ROWID=:sale_id', {'sale_id': sale_id})
    conn.commit()
    conn.close()


def sale_add(desc):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Sales WHERE text ISNULL AND image_src ISNULL')
        cursor.execute('INSERT INTO Sales VALUES (:desc, NULL, NULL)', {'desc': desc})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Sales':
            cursor.execute('CREATE TABLE Sales(description TEXT, text TEXT, image_src TEXT)')
            cursor.execute('INSERT INTO Sales VALUES (:desc, NULL, NULL)', {'desc': desc})
            conn.commit()
            conn.close()
        write_error(str(e))


def sale_add_p1(text, attach):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    cursor.execute('UPDATE Sales SET text=:text, image_src=:attach WHERE text ISNULL AND image_src ISNULL',
                   {'text': text, 'attach': attach})
    conn.commit()
    conn.close()



def tools_write_db(user_id, answer):
    conn = database_connector(DATABASE)
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
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Tyres_Query WHERE user_id=:user_id', {'user_id': user_id})
        cursor.execute('INSERT INTO Tyres_Query VALUES (:user_id, :size)', {'user_id': user_id, 'size': size})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Tyres_Query':
            cursor.execute('CREATE TABLE Tyres_Query(user_id TEXT, size TEXT)')
            cursor.execute('INSERT INTO Tyres_Query VALUES (:user_id, :size)', {'user_id': user_id, 'size': size})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))


def tyres_get_size(user_id):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT size FROM Tyres_Query WHERE user_id=:user_id', {'user_id': user_id})
        answer = cursor.fetchone()[0]
        cursor.execute('DELETE FROM Tyres_Query WHERE user_id=:user_id', {'user_id': user_id})
        conn.commit()
        conn.close()
        return answer
    except Exception as e:
        write_error(str(e))
        return '0/0/0'


def tyres_find(size, season):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT name, season, price FROM Tyres_Catalog WHERE size=:size AND season=:season',
                       {'size': size, 'season': season})
        return cursor.fetchall()
    except Exception as e:
        write_error(str(e))
        return [('Name', 'Season', '0')]


def tyres_get_install_price():
    service = u'install'
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT price FROM Tyres_Service WHERE service=:service', {'service': service})
        answer = cursor.fetchone()[0]
    except Exception as e:
        write_error(str(e))
        answer = u'Попробуйте позже.'
    return answer


def tyres_get_fix_price():
    service = u'fix'
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT price FROM Tyres_Service WHERE service=:service', {'service': service})
        answer = cursor.fetchone()[0]
    except Exception as e:
        write_error(str(e))
        answer = u'Попробуйте позже.'
    return answer


def tyres_get_store_price():
    service = u'store'
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT price FROM Tyres_Service WHERE service=:service', {'service': service})
        answer = cursor.fetchone()[0]
    except Exception as e:
        write_error(str(e))
        answer = u'Попробуйте позже.'
    return answer


def tyres_set_service_price(service, price):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Tyres_Service WHERE service=:service', {'service': service})
        cursor.execute('INSERT INTO Tyres_Service VALUES (:service, :price)', {'service': service, 'price': price})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Tyres_Service':
            cursor.execute('CREATE TABLE Tyres_Service(service TEXT, price TEXT)')
            cursor.execute('INSERT INTO Tyres_Service VALUES (:service, :price)', {'service': service, 'price': price})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))


def tyres_write_order(user_id, answer):
    conn = database_connector(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Tyres WHERE user_id=:user_id', {'user_id': user_id})
        cursor.execute('INSERT INTO Tyres VALUES (:user_id, :answer)', {"user_id": user_id, "answer": answer})
        conn.commit()
        conn.close()
    except Exception as e:
        if str(e.message) == 'no such table: Tyres':
            cursor.execute('CREATE TABLE Tyres(user_id TEXT, answer TEXT)')
            cursor.execute('INSERT INTO Tyres VALUES (:user_id, :answer)', {"user_id": user_id, "answer": answer})
            conn.commit()
            conn.close()
            write_error(str(e))
        else:
            write_error(str(e))


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
