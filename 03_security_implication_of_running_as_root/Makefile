all: dependencies

dependencies:
	rm -rf env
	virtualenv env
	. env/bin/activate; pip install scapy
	sudo touch /tmp/dont_delete
	sudo pip install scapy

run:
	. env/bin/activate; python dont_run_root.py

root_run:
	. env/bin/activate; sudo python dont_run_root.py

setcap:
	sudo setcap cap_net_raw=eip env/bin/python2
