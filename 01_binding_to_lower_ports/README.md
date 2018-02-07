1. Get environment setup.
```
make all
```

2. Try and run the application, should fail.
make run

3. Set the capabilities.
make setcap

4. For verification, check the binary, it should list the new capability.
getcap driver.out

5. Try and run the application again, it should run.
make run
