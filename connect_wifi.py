# importing the os module
import os
# defining the function to establish a new connection

def create_new_connection(name, SSID, password):

    print('hm')

    config = """<?xml version="1.0"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>""" + name + """</name>
        <SSIDConfig>
            <SSID>
                <name>""" + SSID + """</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>""" + password + """</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
        <MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
            <enableRandomization>false</enableRandomization>
            <randomizationSeed>3980062735</randomizationSeed>
        </MacRandomization>
    </WLANProfile>
"""
    with open("C:\\wifis\\" + name + ".xml", 'w') as file:
        file.write(config)

    print('pliok')

    wlan_command = 'netsh wlan add profile filename ="C:\\wifis\\' + name + ".xml\"" + ' interface = "Wi-Fi"'
    os.system(wlan_command)

def wlan_connect(name):
    wlan_command = "netsh wlan connect name =\"" + name
    os.system(wlan_command)


#
# name = "Eli"
# password = "qwer1234"
#
# create_new_connection(name, name, password)
#
# wlan_connect(name)
