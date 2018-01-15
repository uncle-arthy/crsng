#!/usr/bin/python3
#  -*- coding: utf-8 -*-
__author__ = 'Alexei Evdokimov'


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from crsngDBHandler import DatabaseHandler


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        #  Init database handler
        self.db = DatabaseHandler()
        
        #  Decorate main window
        self.setObjectName("MainWindow")
        self.resize(1280, 900)
        self.setWindowTitle("crsng | Main")
        
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.setFont(font)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/Stripes_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
    #  Service function
    def say(self, txt="WTF?!"):
        try:
            print("I say " + str(txt))
        except:
            print("Something goes wrong...")
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = AppMainWindow()
    
    MainWindow.show()
    
    sys.exit(app.exec_())
