#!/usr/bin/python3
#  -*- coding: utf-8 -*-
__author__ = 'Alexei Evdokimov'


import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

from crsngDBHandler import DatabaseHandler
from crsngWindows import BreedsManager, DogManager, DecoratedWindow


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        #  Init database handler
        self.db = DatabaseHandler()
        
        self.initUI()
        
    def initUI(self):
        
        #  Decorate main window
        self.setObjectName("MainWindow")
        self.resize(1280, 900)
        self.setWindowTitle("CRSNG 2018.0.1")
        
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.setFont(font)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/crsng_png_icon_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        #  Organize central widget where all stuff will be
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName('centralWidget')
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName('gridLayout')
        self.setCentralWidget(self.centralWidget)
        
        # Organize topmenu, menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName('menubar')
        
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName('menufile')
        self.menufile.setTitle('File')
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName('menuhelp')
        self.menuhelp.setTitle('Help')
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName('menusettings')
        self.menusettings.setTitle('Settings')
        self.setMenuBar(self.menubar)
        
        #  Organize statusbar for future needs
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName('statusbar')
        self.setStatusBar(self.statusbar)
        
        #  Organize menu items (as Actions)
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName('actionExit')
        self.actionExit.setText('Exit')
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setText("About")
        self.actionSaveAll = QtWidgets.QAction(self)
        self.actionSaveAll.setObjectName("actionSaveAll")
        self.actionSaveAll.setText("Save")
        self.actionSaveAll.setToolTip("Save current state in database")
        self.actionSaveAll.setShortcut("Ctrl+S")
        self.actionEditChamp = QtWidgets.QAction(self)
        self.actionEditChamp.setObjectName("actionEditChamp")
        self.actionEditChamp.setText("Competition settings...")
        self.actionDogsDB = QtWidgets.QAction(self)
        self.actionDogsDB.setObjectName("actionDogsDB")
        self.actionDogsDB.setText("Manage dogs...")
        self.actionBreeds = QtWidgets.QAction(self)
        self.actionBreeds.setObjectName("actionBreeds")
        self.actionBreeds.setText("Manage breeds...")
        
        self.menufile.addAction(self.actionSaveAll)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionExit)
        self.menusettings.addAction(self.actionEditChamp)
        self.menusettings.addAction(self.actionDogsDB)
        self.menusettings.addAction(self.actionBreeds)
        self.menuhelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menusettings.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.actionDogsDB.triggered.connect(self.show_dog_manager)
        self.actionBreeds.triggered.connect(self.show_breeds)
        self.actionEditChamp.triggered.connect(self.say)
        self.actionExit.triggered.connect(app.quit)
        
    #  Service function
    def say(self, txt="WTF?!"):
        try:
            print("I say " + str(txt))
        except:
            print("Something goes wrong...")
            
    #  Breed manager
    def show_breeds(self):
        self.breeds_window = BreedsManager(self.db)
        
    #  Dog manager
    def show_dog_manager(self):
        self.dog_manager = DogManager(self.db)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = AppMainWindow()
    
    MainWindow.show()
    
    sys.exit(app.exec_())
