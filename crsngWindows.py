#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Alexey Evdokimov'

import time
from PyQt5 import QtCore, QtGui, QtWidgets

class DecoratedWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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
        self.top_shelve_layout = QtWidgets.QHBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.top_shelve = QtWidgets.QFrame(self)
        self.top_shelve.setLayout(self.top_shelve_layout)

        
        self.create_dog_table()
        self.update_dog_table()
        
        self.add_dog_btn = QtWidgets.QPushButton()
        self.add_dog_btn.setText('Add dog')
        self.add_dog_btn.clicked.connect(self.add_dog_form)
        self.top_shelve_layout.addWidget(self.add_dog_btn)
        self.top_shelve_layout.addStretch()
        
        self.vbox.addWidget(self.top_shelve)
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
        self.dog_table.setDragEnabled(False)
        self.dog_table.verticalHeader().hide()
        self.dog_table.setSortingEnabled(True)
        self.dog_table.setColumnCount(9)
        self.dog_table.setColumnWidth(0, 50)
        self.dog_table.setColumnWidth(1, 370)
        self.dog_table.setColumnWidth(2, 120)
        self.dog_table.setColumnWidth(3, 75)
        self.dog_table.setColumnWidth(4, 200)
        self.dog_table.setColumnWidth(5, 100)
        self.dog_table.setColumnWidth(6, 100)
        self.dog_table.setColumnWidth(7, 100)
        self.dog_table.setColumnWidth(8, 100)
        
        # Table headers
        headers = ['DB ID', 'Dog name', 'Breed', 'Gender', 'Owner',
                   'Birthday', 'Doc number', 'Racebook', 'Tattoo/Chip']
        self.dog_table.setHorizontalHeaderLabels(headers)
        
    def update_dog_table(self):
        
        dogs_list = self.db.get_dogs()
        
        self.dog_table.setRowCount(len(dogs_list))
        
        for row_num, entry in enumerate(dogs_list):
            print(row_num, entry)
            self.dog_table.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(entry[0])))
            self.dog_table.setItem(row_num, 1, QtWidgets.QTableWidgetItem(entry[1]))
            self.dog_table.setItem(row_num, 2, QtWidgets.QTableWidgetItem(entry[2]))
            self.dog_table.setItem(row_num, 3, QtWidgets.QTableWidgetItem(entry[3]))
            self.dog_table.setItem(row_num, 4, QtWidgets.QTableWidgetItem(entry[4]))
            self.dog_table.setItem(row_num, 5, QtWidgets.QTableWidgetItem(entry[5]))
            self.dog_table.setItem(row_num, 6, QtWidgets.QTableWidgetItem(entry[6]))
            self.dog_table.setItem(row_num, 7, QtWidgets.QTableWidgetItem(entry[7]))
            self.dog_table.setItem(row_num, 8, QtWidgets.QTableWidgetItem(entry[8]))
            
    def add_dog_form(self):
        self.add_dog_form = AddDogWindow(self.db)


class AddDogWindow(DecoratedWindow):
    def __init__(self, database_handler):
        super().__init__()
        self.db = database_handler
        
        #  Decorate window
        self.initUI()
        
    def initUI(self):
        # Geometry
        self.setWindowTitle("Add Dog | CRSNG")
        self.setGeometry(200, 200, 640, 500)
        
        # Service text
        self.service_label = QtWidgets.QLabel("\nThis is service label\n\n")
        self.service_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # Buttons
        self.add_dog_to_db_btn = QtWidgets.QPushButton("Add to DB")
        self.add_dog_to_db_btn.clicked.connect(self.add_dog_handler)
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.close)
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.add_dog_to_db_btn, 0, QtCore.Qt.AlignRight)
        self.hbox.addWidget(self.cancel_btn, 0, QtCore.Qt.AlignRight)
        
        # Entry fields
        self.dog_name_entry = QtWidgets.QLineEdit()
        self.dog_breed_entry = QtWidgets.QComboBox()
        self.dog_gender_entry = QtWidgets.QComboBox()
        self.dog_owner_entry = QtWidgets.QLineEdit()
        self.dog_birth_entry = QtWidgets.QDateEdit()
        self.dog_birth_entry.setDisplayFormat("dd.MM.yyyy")
        self.dog_doc_entry = QtWidgets.QLineEdit()
        self.dog_racebook_entry = QtWidgets.QLineEdit()
        self.dog_tattoo_entry = QtWidgets.QLineEdit()
        
        # Layout
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.addRow(self.service_label)
        self.form_layout.addRow("Dog name:", self.dog_name_entry)
        self.form_layout.addRow("Breed:", self.dog_breed_entry)
        self.form_layout.addRow("Gender", self.dog_gender_entry)
        self.form_layout.addRow("Owner:", self.dog_owner_entry)
        self.form_layout.addRow("Birth date:", self.dog_birth_entry)
        self.form_layout.addRow("№ doc:", self.dog_doc_entry)
        self.form_layout.addRow("№ racebook:", self.dog_racebook_entry)
        self.form_layout.addRow("Tattoo:", self.dog_tattoo_entry)
        
        self.form_layout.addRow(self.hbox)
        
        self.setLayout(self.form_layout)
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)  # Make window modal
        
        # Set data for Breeds etc.
        for i, breed in self.db.get_breeds():
            self.dog_breed_entry.addItem(breed, i)
            
        self.dog_gender_entry.addItems(["Male", "Female"])
        
        self.show()
        
    def add_dog_handler(self):
        print("Adding Dog...")
        
        dog_dict = {}
        dog_dict["name"] = self.dog_name_entry.text()
        dog_dict["breed_id"] = self.dog_breed_entry.currentData()
        dog_dict["breed_name"] = self.dog_breed_entry.currentText()
        dog_dict["gender"] = self.dog_gender_entry.currentText()
        dog_dict["owner"] = self.dog_owner_entry.text()
        dog_dict["birthday"] = self.dog_birth_entry.date().toPyDate().strftime("%d.%m.%Y")
        dog_dict["doc"] = self.dog_doc_entry.text()
        dog_dict["racebook"] = self.dog_racebook_entry.text()
        dog_dict["tattoo"] = self.dog_tattoo_entry.text()

        self.db.add_dog_to_db(dog_dict)
        
        self.close()
