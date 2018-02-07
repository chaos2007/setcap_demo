all: dependencies

dependencies:
	virtualenv env
	. env/bin/activate; pip install scapy

run:
	. env/bin/activate; python send_packet.py

setcap:
	sudo setcap cap_net_raw=eip env/bin/python2
