#script to run on pi2 to recieve data via UDP; recievepi.py
import socket
#script to run on pi1 to send data via UDP; sendpi.py
import socket

#set sending pi IP
UDP_IP = "CHANGE TO PI'S IP"
#set sending pi PORT
UDP_PORT = 5005

#message is what is being sent, change to file
MESSAGE = "Hello, World!"

#sample testing print statements
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

#setting TCP/IP sockets for communication
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP

#defining what to send over sockets
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
#MESSAGE = "data"

#set recieving pi IP
UDP_IP = "192.168.0.100"
#set recieving pi PORT
UDP_PORT = 5005

#setting TCP/IP sockets for communication
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP

#defining what to accept when recieving
sock.bind(MESSAGE, (UDP_IP, UDP_PORT))

#loop for running for recieving data
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #accepted statement confirmation
    print "received message:", data
