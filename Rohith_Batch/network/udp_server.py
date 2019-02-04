# creating the udp socket

import socket 
udp_ser = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip =socket.gethostname()
port =5000
udp_ser.bind((ip,port))
udp_ser.sendto("hello",(ip,5005))
data,cli_addr = udp_ser.recvfrom(1024)
print data
print "client ",cli_addr
udp_ser.close()
