#recieve Client
import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("192.168.84.68",1235)) #change according to system IP address
print("Server is connected")
msg=c.recv(1024)
print("Server sent Date and Time: ",msg.decode())
c.close()
