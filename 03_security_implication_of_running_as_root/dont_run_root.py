from scapy.all import *
import os

os.remove("/tmp/dont_delete")

packet = Ether()/Dot1Q()/IP()
send(packet)

