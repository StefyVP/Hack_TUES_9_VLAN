import argparse
from pysnmp.hlapi import *
import socket

status = ''

parser = argparse.ArgumentParser(description='SNMP Scanner')

parser.add_argument('--community', help='SNMP community string', default='public')

args = parser.parse_args()

snmp_parameters = CommunityData(args.community)

oid = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

IPaddress = socket.gethostbyname(socket.gethostname())
# print("IP:", IPaddress)

snmp_request = getCmd(SnmpEngine(),
snmp_parameters,
UdpTransportTarget((IPaddress, 161)),
ContextData(),
ObjectType(oid))

def return_status():
    return status

for errorIndication, errorStatus, errorIndex, varBinds in snmp_request:
    if errorIndication:
        print(errorIndication)
        # print("NO problem!")
        status = str(errorIndication) + "   NO Problem !"

        break

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        print("Error status")
        status = '%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?')
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
            print("varbing")
            status += ' = '.join([x.prettyPrint() for x in varBind])


