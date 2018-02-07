1. Get environment setup.
make all

2. Try and run the application, should fail.
make run

3. Set the capabilities.
make setcap

4. For verification, check the binary, it should list the new capability.
getcap env/bin/python2

5. Try and run the application again, it should run.
make run
