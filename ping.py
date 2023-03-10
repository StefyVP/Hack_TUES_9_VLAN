import os
import socket

IPaddress = socket.gethostbyname(socket.gethostname())
ip_list = ["8.8.8.8",str(IPaddress)]

result_list = []

def ping_network():

    for ip in ip_list:
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            # print(f"UP {ip} Ping Successfull")
            result_list.append(f"UP {ip} Ping Successfull" + "\n")
        else:
            print(f"DOWN {ip} Ping Unsuccessful")
            # result_list.append(f"DOWN {ip} Ping Unuccessfull" + "\n")
    return result_list
