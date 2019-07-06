# tcp_client 
import socket as sock
tcp_cli = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
print "TCP client create"
ip = sock.gethostname()
port =5005

print "fixif id and port "
tcp_cli.bind((ip,port))

print "sending the conncetion  from client to server"
tcp_cli.connect((ip,5000))

print"receving the data from server :"
data = tcp_cli.recv(1024)

print data

tcp_cli.send(input("enter some data to sending to server : "))

tcp_cli.close()
input("enter any thing to close ")
