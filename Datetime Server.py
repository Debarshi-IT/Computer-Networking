#SYSTEM DATETIME SERVER
import socket
import datetime
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.84.86",1234)) #change according to system IP address
s.listen(5)
while True:
    c,addr=s.accept()
    print("Server is connected with",addr)
    x=datetime.datetime.now()
    x=str(x)
    c.send(x.encode())
