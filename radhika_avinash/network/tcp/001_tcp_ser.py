#TCP SERVER
import socket as sock
print "CREATING TCP SERVER"
tcp_ser =sock.socket(sock.AF_INET,sock.SOCK_STREAM)
ip = sock.gethostname()
port = 5000
print "fixing ip and port to server :",(ip,port)
tcp_ser.bind((ip,port))
tcp_ser.listen(2) # maximum can connect only 2 clients
print "waiting for clinet1 req : ",
con1,addr_c1 =tcp_ser.accept()
print addr_c1

print "waiting for clinet2 req : ",
con2,addr_c2 =tcp_ser.accept()
print addr_c2
data = input("enter sending data : ")
con1.send(data)
con2.send(data)
print "waiting for client1 data : ",
data=con1.recv(1024)
print data
data=con2.recv(1024)
print "waiting for client2 data : ",
print data
tcp_ser.close()
