# TCP CLIENT 2
import socket as sock
print "CREATING TCP CLIENT2"
tcp_cli2 =sock.socket(sock.AF_INET,sock.SOCK_STREAM)
print "sending the req from client2"
ip = sock.gethostname()
port = 5000
tcp_cli2.connect((ip,port))
print "waiting for recving : ",
data=tcp_cli2.recv(1024)
print data
data = input("enter sending data : ")
tcp_cli2.send(data)
tcp_cli2.close()
