#UDP CLIENT
import socket as sock
print "creating UDP CLIENT"
udp_cli = sock.socket(sock.AF_INET,sock.SOCK_DGRAM)
ip = sock.gethostname()
port = 5005
print "fixing the ip and port number ",(ip,port)
udp_cli.bind((ip,port))
print "waiting for data receving : ",
data ,addr_s = udp_cli.recvfrom(1024)
print data," server address : ",addr_s
data = input("enter some data for sending : ")
udp_cli.sendto(data,(ip,5000))
udp_cli.close()
