import subprocess

networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

# decode_network = networks.encode('utf-8').strip()
decode_network2 = networks.decode('ascii').strip()

print(decode_network2)