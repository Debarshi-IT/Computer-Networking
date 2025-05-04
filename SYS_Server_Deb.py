#SYSTEM SERVER
import socket
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.84.86",1234))
s.listen(1)
print("Server is ready to accept connection")
c,addr=s.accept()
print("Client address id",addr)
while True:
    sm=input("Enter msg")
    c.send(sm.encode())
    rm=c.recv(1024)
    print("Client send",rm.decode())
    if sm==" bye" or rm.decode()==" bye":
        break
s.close()
