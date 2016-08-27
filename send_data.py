#script to run on pi1 to send data via UDP; sendpi.py
import socket
#set sending pi IP
UDP_IP = "192.168.1.175"
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