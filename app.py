import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3

questionCount = 0
maxPoints = 0

class check_network(QDialog):
    def __init__(self):
        super(check_network, self).__init__()
        loadUi("mai.ui", self)


# main

app = QApplication(sys.argv)
first_screen = check_network()
widget = QtWidgets.QStackedWidget()
widget.addWidget(first_screen)
widget.setFixedHeight(552)
widget.setFixedWidth(785)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")