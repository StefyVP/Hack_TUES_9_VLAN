import subprocess
import sys

# PYTHONIOENCODING = 'utf-8'

# sys.stdout.encoding()

def getNetworksFunc():

    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

    networks = networks.decode('cp437')

    x = networks.splitlines()

    name_net = []

    info_for_net = {}

    word = 'SSID'

    for el in x:
        str = el
        # print(el)

        if word in str:
            # print(str)
            name_net.append(el)

        # else:
            # info_for_net[name_net[el]] = el

    print(networks)

    # print(name_net)

    return name_net

# getNetworksFunc()

# def
