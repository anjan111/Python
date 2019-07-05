# tcp_server
import socket as sock

tcp_ser = sock.socket(sock.AF_INET,sock.SOCK_STREAM)

ip = sock.gethostname()
port = 5000

tcp_ser.bind((ip,port))
tcp_ser.listen(1)

conn,addr = tcp_ser.accept()
conn.send("hello")
data = conn.recv(1024)
print data
tcp_ser.close()
