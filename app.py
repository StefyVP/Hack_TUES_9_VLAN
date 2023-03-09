import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import getNetworks
import connect_wifi
import socket

import sqlite3

network_list = getNetworks.getNetworksFunc()

# IPaddress = socket.gethostbyname(socket.gethostname())

class check_network(QDialog):
    def __init__(self):
        global network_list
        super(check_network, self).__init__()
        loadUi("mai.ui", self)

        # print(only_names)

        IPaddress = socket.gethostbyname(socket.gethostname())
        print(IPaddress)
        self.connected_label.setText('Connected to: ' + str(IPaddress))

        self.comboBox.addItems(network_list)

        self.connect_btn.clicked.connect(self.make_connection)
        self.refresh_btn.clicked.connect(self.refresh_networks)

    def make_connection(self):
        global network_list

        chosen_network = self.comboBox.currentText()
        only_names = []

        dic = {}
        for el in network_list:
            only_names.append(el.split(": ", 1)[1])
            dic[el] = el.split(": ", 1)[1]

        print(dic)
        print(f"Network: {dic[chosen_network]}")

        connect_wifi.createNewConnection(dic[chosen_network])
        connect_wifi.connect(dic[chosen_network], dic[chosen_network])
        # print('yey')

        IPaddress = socket.gethostbyname(socket.gethostname())
        self.connected_label.setText('Connected to: ' + str(IPaddress))

    def refresh_networks(self):
        network_list = getNetworks.getNetworksFunc()
        self.comboBox.addItems(network_list)





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