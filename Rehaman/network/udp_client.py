# creating the udp socket

import socket
udp_cli = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip =socket.gethostname()
port =5005
udp_cli.bind((ip,port))

data,ser_addr = udp_cli.recvfrom(1024)
print data
print "server ",ser_addr
udp_cli.sendto("hai",(ip,5000))
udp_cli.close()

