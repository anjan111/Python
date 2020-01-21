#UDP SERVER
import socket as sock
print "creating UDP SERVER "
udp_ser = sock.socket(sock.AF_INET,sock.SOCK_DGRAM)
ip = sock.gethostname()
port = 5000
print "fixing the ip and port number ",(ip,port)
udp_ser.bind((ip,port))
data = input("enter some data for sending : ")
udp_ser.sendto(data,(ip,5005))
print "waiting for data receving : ",
data ,addr_c = udp_ser.recvfrom(1024)
print data," server address : ",addr_c
udp_ser.close()
