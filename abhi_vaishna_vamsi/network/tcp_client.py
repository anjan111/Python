# tcp_client 
import socket as sock

tcp_cli = sock.socket(sock.AF_INET,sock.SOCK_STREAM)

ip = sock.gethostname()
port =5005

tcp_cli.bind((ip,port))

tcp_cli.connect((ip,5000))

data = tcp_cli.recv(1024)

print data
tcp_cli.send("bye")

tcp_cli.close()
