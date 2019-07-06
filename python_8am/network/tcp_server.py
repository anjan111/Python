# tcp_server
import socket as sock

tcp_ser = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
print "TCP server create"
ip = sock.gethostname()
port = 5000
print "fixif id and port "
tcp_ser.bind((ip,port))
print "fixing the no of client "
tcp_ser.listen(1)

print "waiting for connection from client :"
conn,addr = tcp_ser.accept()
conn.send(input("enter some data to send to client : "))
print"waiting for receving the data from client : "
data = conn.recv(1024)

print data
tcp_ser.close()
input("enter some daata ")
