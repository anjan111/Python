#udp client
import socket
udp_cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print"UDP CLIENT CREATED"
ip = socket.gethostname()
port = 5005
print "fixing the ip and port number "
udp_cli.bind((ip,port))
print "receiving the daata from server : "
data =udp_cli.recvfrom(1024)
print data
data = input("enter some data to sending : ")
udp_cli.sendto(data,(ip,5000))
udp_cli.close()

input("enter any character to close")
