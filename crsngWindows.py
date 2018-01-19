#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Alexey Evdokimov'

from PyQt5 import QtCore, QtGui, QtWidgets

class DecoratedWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.setFont(font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/crsng_png_icon_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)


class BreedsManager(DecoratedWindow):
    def __init__(self, database_handler):
        super().__init__()
        self.db = database_handler
        
        #  Decorate window
        self.initUI()
        
        
    def initUI(self):
        
        help_text = 'Breed Manager will be implemented\nin later release\n' \
                    '(Meanwhile edit breed in database directly)\n\n' \
                    'Редактор пород будет реализован\nв последующих релизах\n(Пока породы можно редактировать\n' \
                    'в базе данных напрямую)'
        
        help_label = QtWidgets.QLabel()
        help_label.setText(help_text)
        help_label.setAlignment(QtCore.Qt.AlignCenter)
        
        grid = QtWidgets.QGridLayout(self)
        self.setLayout(grid)
        
        grid.addWidget(help_label, 0, 0)
        
        self.setWindowTitle('Breed manager | CRSNG')
        self.setGeometry(300, 300, 480, 200)
        self.show()


class DogManager(DecoratedWindow):
    def __init__(self, database_handler):
        super().__init__()
        self.db = database_handler
        
        #  Decorate window
        self.initUI()
        
    def initUI(self):
        #top_shelve = QtWidgets.QHBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        
        self.create_dog_table()
        self.update_dog_table()
        
        #vbox.addWidget(top_shelve)
        self.vbox.addWidget(self.dog_table)
        self.setLayout(self.vbox)
        
        self.setGeometry(200, 200, 1024, 768)
        self.setWindowTitle('Dog manager | CRSNG')
        self.show()
        
    def create_dog_table(self):
        self.dog_table = QtWidgets.QTableWidget()
        self.dog_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dog_table.setAlternatingRowColors(True)
        self.dog_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.dog_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.dog_table.setRowCount(10)
        self.dog_table.setColumnCount(6)
        
    def update_dog_table(self):
        pass
