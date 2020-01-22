#TCP CLIENT 1
import socket as sock
print "CREATING TCP CLIENT1"
tcp_cli1 =sock.socket(sock.AF_INET,sock.SOCK_STREAM)
print "sending the req from client1"
ip = sock.gethostname()
port = 5000
tcp_cli1.connect((ip,port))
print "waiting for recving : ",
data=tcp_cli1.recv(1024)
print data
data = input("enter sending data : ")
tcp_cli1.send(data)
tcp_cli1.close()
