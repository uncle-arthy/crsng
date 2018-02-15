#!/usr/bin/python3
#  -*- coding: utf-8 -*-
__author__ = 'Alexei Evdokimov'


import sqlite3 as sql
from datetime import datetime, date, time


class DatabaseHandler(object):
    def __init__(self):
        self.con = sql.connect('MainDB.db', detect_types=sql.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.cur.execute('PRAGMA encoding="UTF-8";')
        
        print('Connection seems to be established...')
        
    def close_db(self):
        print('Commiting changes...')
        self.con.commit()
        print('Closing connection with DB...')
        self.con.close()
        
    def add_dog_to_db(self, dog_dict):
        print(dog_dict)
        
    def test_list(self):
        sample_breeds = ["Whippet", "Borzoi", "Italian greyhound",
                         "Basenji", "Saluki", "Greyhound",
                         "Thai ridgeback", "Rodesian ridgeback",
                         "Beagle", "Irish wolfhound"]
        
        sample_fetched_result = enumerate(sample_breeds, start=1)
        
        return sample_fetched_result
