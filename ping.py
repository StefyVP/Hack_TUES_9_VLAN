import os
import socket

IPaddress = socket.gethostbyname(socket.gethostname())
ip_list = ["8.8.8.8",str(IPaddress)]

for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successfull")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")