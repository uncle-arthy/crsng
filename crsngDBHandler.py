#!/usr/bin/python3
#  -*- coding: utf-8 -*-
__author__ = 'Alexei Evdokimov'


import sqlite3 as sql
from datetime import datetime, date, time
from PyQt5 import QtSql


class DatabaseHandler(object):
    def __init__(self):
        
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName('MainDB.db')
        self.con.open()
        
    def close_db(self):
        print('Commiting changes...')
        self.con.commit()
        print('Closing connection with DB...')
        self.con.close()
        
    def add_dog_to_db(self, dog_dict):
        print(dog_dict)
        
    def get_breeds(self):
        
        qry = QtSql.QSqlQuery('SELECT * from breeds')
        
        breeds_fetch = []
        
        if qry.isSelect():
            qry.first()
            while qry.isValid():
                breeds_fetch.append((qry.value("id"), qry.value('breed')))
                qry.next()
        
        return breeds_fetch
