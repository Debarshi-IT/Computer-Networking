#SYSTEM CLIENT
import socket
c= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("192.168.85.14",1234)) #change according to system IP address
print("Client is connected with server")
while True:
    rm=c.recv(1024)
    Sprint("Server send",rm.decode())
    sm=input("Enter msg")
    c.send(sm.encode())
    if sm==" bye" ''' or rm.decode()==" bye"''':
        break
c.close()
