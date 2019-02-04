# creating the tcp socket

import socket 
tcp_ser = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip =socket.gethostname()
port =5000
tcp_ser.bind((ip,port))
tcp_ser.listen(1)
conn ,addr = tcp_ser.accept()
conn.send("hello")
data = conn.recv(1024)
print data
print addr
conn.close()
