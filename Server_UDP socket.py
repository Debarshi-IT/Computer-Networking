#UDP SERVER
import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="169.254.102.30"
port_num=1234
port=1235
Msg_Size=1024

c.bind((ip,port_num))
print("Node is ready")
while True:
    msg1,addr=c.recvfrom(Msg_Size)
    print("Sender is:",addr,"---->",msg1.decode())
    msg=input("Enter msg: ")
    c.sendto(msg.encode(),(ip,port))
    if msg=="bye" or msg1.decode()=="bye":
        break
c.close()
