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
        
        qry = QtSql.QSqlQuery()
        qry.prepare('INSERT INTO dogs (name, breed_id, gender, owner, birth, doc, racebook, tattoo)'
                    'VALUES (:name, :breed_id, :gender, :owner, :birth, :doc, :racebook, :tattoo)')
        
        qry.bindValue(':name', dog_dict["name"])
        qry.bindValue(':breed_id', dog_dict["breed_id"])
        qry.bindValue(':gender', dog_dict["gender"])
        qry.bindValue(':owner', dog_dict["owner"])
        qry.bindValue(':birth', dog_dict["birthday"])
        qry.bindValue(':doc', dog_dict["doc"])
        qry.bindValue(':racebook', dog_dict["racebook"])
        qry.bindValue(':tattoo', dog_dict["tattoo"])
        
        if qry.exec_():
            self.con.commit()
        
    def get_breeds(self):
        
        qry = QtSql.QSqlQuery('SELECT * FROM breeds')
        
        breeds_fetch = []
        
        if qry.isSelect():
            qry.first()
            while qry.isValid():
                breeds_fetch.append((qry.value("id"), qry.value('breed')))
                qry.next()
        
        return breeds_fetch

    def get_dogs(self, breed=None, gender=None):
        
        dogs_fetch = []
        
        # qry = QtSql.QSqlQuery('SELECT * FROM dogs, breeds WHERE dogs.breed_id=breeds.breed')
        #
        # if qry.isSelect():
        #     qry.first()
        #     while qry.isValid():
        #         dogs_fetch.append((qry.value("id"), qry.value("name"), qry.value("breed_id")))
        #         qry.next()
        
        return dogs_fetch
