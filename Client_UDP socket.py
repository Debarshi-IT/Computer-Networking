#UDP CLIENT
import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="169.254.102.30"
port_num=1235
port=1234
Msg_Size=1024

c.bind((ip,port_num))
print("Node is ready")
while True:
    msg=input("Enter msg: ")
    c.sendto(msg.encode(),(ip,port))
    msg1,addr=c.recvfrom(Msg_Size)
    print("Sender is:",addr,"---->",msg1.decode())
    if msg=="bye" or msg1.decode()=="bye":
        break

c.close()
