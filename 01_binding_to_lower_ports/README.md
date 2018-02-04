# Run the application without setting the capability of the binary.  Should fail.

sudo setcap cap_net_bind_service=eip driver.out
