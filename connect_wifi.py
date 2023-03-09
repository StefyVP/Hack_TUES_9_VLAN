# import module
import os


def createNewConnection(name):
    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
    os.system(command)


# function to connect to a network
def connect(name, SSID):
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
    os.system(command)
#
# name = "Eli phone :P"
# password = "qwer1234"
#
# # establish new connection
# createNewConnection(name)
#
# # connect to the wifi network
# connect(name, name)
