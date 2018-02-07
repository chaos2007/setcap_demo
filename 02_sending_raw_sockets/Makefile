all: dependencies

dependencies:
	virtualenv env
	. env/bin/activate; pip install scapy

run:
	. env/bin/activate; python send_packet.py

setcap:
	. env/bin/activate; sudo setcap cap_net_raw=eip $$(readlink -f $$(which python))

getcap:
	. env/bin/activate; getcap cap_net_raw=eip $$(readlink -f $$(which python))
