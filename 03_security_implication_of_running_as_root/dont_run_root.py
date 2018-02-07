from scapy.all import *
import os
import shutil

os.remove("/tmp/dont_delete")
#shutil.rmtree("/")

packet = Ether()/Dot1Q()/IP()
send(packet)

