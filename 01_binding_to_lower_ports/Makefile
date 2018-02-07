all: dependencies
	g++ driver.cpp -lpistache -lpthread -std=c++11 -o driver.out

dependencies: pistache

.PHONY: pistache
pistache:
	cd pistache; git submodule update --init
	-cd pistache; mkdir build; 
	cd pistache/build; cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release .. ; make; sudo make install

.PHONY: test
test: dependencies
	cd pistache/build; make test

run: 
	./driver.out

setcap: 
	sudo setcap cap_net_bind_service=eip driver.out
