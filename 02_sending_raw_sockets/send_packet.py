from scapy.all import *

packet = Ether()/Dot1Q()/IP()
send(packet)

