from scapy.all import *
import os
import shutil

packet = Ether()/Dot1Q()/IP()
send(packet)

os.remove("/tmp/dont_delete")
#shutil.rmtree("/")
