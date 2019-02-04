# creating the tcp socket

import socket
tcp_cli = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip =socket.gethostname()
port =5005
tcp_cli.bind((ip,port))
tcp_cli.connect((ip,5000))
data = tcp_cli.recv(1024)
print data
tcp_cli.send("hai")
tcp_cli.close()

