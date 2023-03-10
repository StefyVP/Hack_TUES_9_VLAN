import argparse
from pysnmp.hlapi import *
import socket

parser = argparse.ArgumentParser(description='SNMP Scanner')

parser.add_argument('--community', help='SNMP community string', default='public')

args = parser.parse_args()

snmp_parameters = CommunityData(args.community)

oid = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

IPaddress = socket.gethostbyname(socket.gethostname())
print("IP:", IPaddress)

snmp_request = getCmd(SnmpEngine(),
snmp_parameters,
UdpTransportTarget((IPaddress, 161)),
ContextData(),
ObjectType(oid))

for errorIndication, errorStatus, errorIndex, varBinds in snmp_request:
    if errorIndication:
        print(errorIndication)
        print("NO problem!")
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        print("Error status")
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
            print("varbing")
