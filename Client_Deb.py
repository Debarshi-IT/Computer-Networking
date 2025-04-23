#CLIENT
import socket
c= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",1234))
print("Client is connected with server")
while True:
    rm=c.recv(1024)
    print("Server send",rm.decode())
    sm=input("Enter msg")
    c.send(sm.encode())
    if sm=="bye" or rm.decode()=="bye":
        break
c.close()
