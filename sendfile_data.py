#code to send file thru sockets
#sending pi code (server)
import socket
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50002              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create new socket using the given address family
s.bind((HOST,PORT))  #bind the socket to the address
s.listen(10)    #set maximum accept rate to 10 connections
while True:
    sc, address = s.accept()    #accept a connection
    f = open('/root/Desktop/server/Server/file2.csv', 'wb')   #open in binary
    while True:
        l = sc.recv(1024)   #receive data from the socket
        while (l):	
            f.write(l)  #writes the contents of string to file
            l = sc.recv(1024)   #recieve data from socket again	    
        f.close()   #close the file opened from the function f
        sc.close()  #close sc from function
        break
    break
s.close()   #close the socket
exit()
