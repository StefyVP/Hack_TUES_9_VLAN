# tova proverqva dali ima dns spoofing

import os

def check_dns_spoofing():
    # server = "8.8.8.8"

    # domain = "elsys-bg.org"

    result_1 = os.popen("nslookup elsys-bg.org").read()

    result_2 = os.popen("nslookup elsys-bg.org 1.1.1.1").read()

    list = result_1.splitlines()
    list2 = result_2.splitlines()

    for el in list:
        if "Address" in el:
            result_1 = el

    for el in list2:
        if "Address" in el:
            result_2 = el

    if result_1 == result_2:
        # print('yey')

        return "There is no DNS spoofing. The ip addresses received from the DNS servers (to elsys-bg.org) are the same ! " + "\n" + "From system DNS and 1.1.1.1"

    else:

        return "There is DNS Spoofing. You should disconnect from this network !" + "\n" + "The system DNS and 1.1.1.1 returned different ip addresses !"

