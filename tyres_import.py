#!/bin/python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os
sys.path.append(os.path.realpath(__file__))
import xlrd
import re
import sqlite3
from settings import *


def process_import(path):
    rb = xlrd.open_workbook(path, formatting_info=True)
    sheet = rb.sheet_by_index(0)

    database_connector = sqlite3.connect(DATABASE)

    cursor = database_connector.cursor()
    cursor.execute('DROP TABLE IF EXISTS Tyres_Catalog')
    cursor.execute('CREATE TABLE Tyres_Catalog(name TEXT, size TEXT, season TEXT, price TEXT)')

    trigger = u''

    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        regu = re.findall(ur'\d+.\d?/\d+.\d? R\d+', row[0])
        if regu and trigger != u'':
            cursor.execute('INSERT INTO Tyres_Catalog VALUES (:name, :size, :season, :price)', {'name': row[0],
                                                                                                'size': regu[0].replace(
                                                                                                    ' R', '/'),
                                                                                                'season': trigger,
                                                                                                'price': int(row[4])})
        elif re.findall(ur'зим', row[0]):
            trigger = u'зима'
        elif re.findall(ur'лет', row[0]):
            trigger = u'лето'

    database_connector.commit()
    database_connector.close()


if __name__ == '__main__':
    process_import()
    print('YEP')
