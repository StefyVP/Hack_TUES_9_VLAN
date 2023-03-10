import socket

ip_address = socket.gethostbyname(socket.gethostname()) # returns the host name of the current system under which the Python interpreter is executed.

def check():
    if ip_address:
        print(f"DNS Status: {socket.gethostname()} is UP! IP address: {ip_address}")
        return f"DNS Status: {socket.gethostname()} is UP! IP address: {ip_address}"
    else:
        # print(f"DNS Status: {socket.gethostname()} is DOWN!")
        return f"DNS Status: {socket.gethostname()} is DOWN!"


