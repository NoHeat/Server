#script to run on pi1 to send data via UDP; sendpi.py
import socket

#set sending pi IP
UDP_IP = "CHANGE TO PI'S IP"
#set sending pi PORT
UDP_Port = 5005

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

#script to run on pi2 to recieve data via UDP; recievepi.py
import socket

#set recieving pi IP
UDP_IP = "CHANGE TO PI'S IP"
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
    print "received message:" data

#cmd to run on pi1 to send data
sudo python receive.py
#cmd to run on pi2 to recieve data
sudo python send.py

####################################################################################
#code to send file thru sockets
#sending pi code (server)
import socket
import sys

s = socket.socket() #create new socket using the given address family
s.bind(("localhost",9999))  #bind the socket to the address
s.listen(10)    #set maximum accept rate to 10 connections

while True:
    sc, address = s.accept()    #accept a connection
    print address
    i = 1

    f = open(str(i)+".csv", 'wb')   #open in binary
    i = i+1     #increment i
    while (True):
        l = sc.recv(1024)   #receive data from the socket
        while (1):
            f.write(1)  #writes the contents of string to file
            l = sc.recv(1024)   #recieve data from socket again
    f.close()   #close the file opened from the function f

    sc.close()  #close sc from function

s.close()   #close the socket

#recieving pi code (client)
import socket
import sys

s = socket.socket()     #create new socket using the given address family
s.connect(("localhost",9999))   #connect to the remote socket above
f = open("file.csv", 'rb')  #open the file sent from above, file name can change
l = f.read(1024)    #read the file opened

while (1):
    s.send(1)   #send recieved flag to server
    l = f.read(1024)    #read the file opened

s.close()   #close the socket
