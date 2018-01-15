#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Alexey Evdokimov'

from PyQt5 import QtCore, QtGui, QtWidgets


class BreedsManager(QtWidgets.QWidget):
    def __init__(self, database_handler):
        super().__init__()
        self.db = database_handler
        
        #  Decorate window
