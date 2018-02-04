all: dependancies
	g++ driver.cpp -lpistache -lpthread -std=c++11 -o driver.out

dependancies: pistache

.PHONY: pistache
pistache:
	-git clone https://github.com/oktal/pistache.git
	cd pistache; git submodule update --init
	-cd pistache; mkdir build; 
	cd pistache/build; cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release .. ; make; sudo make install

.PHONY: test
test: dependancies
	cd pistache/build; make test
