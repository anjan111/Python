#udp server
import socket
udp_ser = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print"UDP SERVER CREATED"
ip = socket.gethostname()
port = 5000
print "fixing the ip and port number "
udp_ser.bind((ip,port))
data = input("enter some data to sending : ")
udp_ser.sendto(data,(ip,5005))
print "receiving the daata from server : "
data =udp_ser.recvfrom(1024)
print data
udp_ser.close()
