import subprocess
import sys

PYTHONIOENCODING = 'utf-8'

# sys.stdout.encoding()

networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

networks = networks.decode('cp437')

print(networks)

