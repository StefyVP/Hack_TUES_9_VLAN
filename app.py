import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import getNetworks
from connect_wifi import *
import socket
# import require
import location
import ping
import dns_checker
import datetime

network_list = getNetworks.getNetworksFunc()

# IPaddress = socket.gethostbyname(socket.gethostname())

msgs_string = ''

monitor_start_time = datetime.datetime.now()

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
        self.location_btn.clicked.connect(self.location_show)
        self.time_btn.clicked.connect(self.connection_time_show)
        self.ping_btn.clicked.connect(self.ping_show)
        self.dns_btn.clicked.connect(self.dns_show)

    def make_connection(self):
        global network_list


        chosen_network = self.comboBox.currentText()
        only_names = []

        dic = {}
        for el in network_list:
            only_names.append(el.split(": ", 1)[1])
            dic[el] = el.split(": ", 1)[1]

        # print(dic)
        print(f"Network: {dic[chosen_network]}")

        password = str(self.password_field.text())
        print(password)

        print(dic[chosen_network])
        print(password)
        create_new_connection(dic[chosen_network], dic[chosen_network], password)
        wlan_connect(dic[chosen_network])

        # print('yey')

        IPaddress = socket.gethostbyname(socket.gethostname())
        self.connected_label.setText('Connected to: ' + str(IPaddress))

        global monitor_start_time
        if IPaddress != '127.0.0.1':
            monitor_start_time = datetime.datetime.now()

    def refresh_networks(self):

        network_list = getNetworks.getNetworksFunc()
        self.comboBox.clear()
        self.comboBox.addItems(network_list)

        IPaddress = socket.gethostbyname(socket.gethostname())
        self.connected_label.setText('Connected to: ' + str(IPaddress))

    def location_show(self): ############################
        global msgs_string

        print('of')

        oof = location.get_location()
        print(oof)

        msgs_string += oof + "\n"

        self.msg_area.setText(msgs_string)

    def connection_time_show(self): ######################
        # monitor_end_time = datetime.datetime.now()

        duration = datetime.datetime.now() - monitor_start_time

        self.msg_area.setText(str(duration))

    def dns_show(self):
        status = ''
        status += dns_checker.check_dns_spoofing()

        self.msg_area.setText(status)

    def ping_show(self):

        results = ping.ping_network()
        str_results = ''

        for el in results:
            str_results += el

        self.msg_area.setText(str_results)





# main

app = QApplication(sys.argv)
first_screen = check_network()
widget = QtWidgets.QStackedWidget()
widget.addWidget(first_screen)
widget.setFixedHeight(661)
widget.setFixedWidth(891)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")


# TO DO
# - eentualno da izliza novo prozorche pokazvashto minali vryzki sys zapameteni paroli