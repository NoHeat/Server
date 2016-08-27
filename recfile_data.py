#recieving pi code (client)
import socket
import sys

HOST = '192.168.1.26'    # The remote host
PORT = 50002             # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #create new socket using the given address family
s.connect((HOST, PORT))   #connect to the remote socket above
f = open("/home/pi/Desktop/server/Server/file2.csv", 'rb')  #open the file sent from above, file name can change
l = f.read(1024)    #read the file opened

while (l):
    s.send(l)   #send recieved flag to server
    l = f.read(1024)    #read the file opened
f.close()
s.shutdown(socket.SHUT_WR)
print s.recv(1024)
s.close()   #close the socket
