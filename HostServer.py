#This script is used along with Sendserver.py.
#This script creates a socket on the host machine and listens to incoming requests and processes them.
#SendServer.py sends data to this socket.

import os
import sys
import socket

TARGET = '172.16.0.227'
TARGET_PORT = 39999

def ServerConnect():
    server_sock=0
    connect_result=0
    try:
      server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except:
      print "Creating a socket failed."
      return 0

    connect_result=server_sock.bind((TARGET,TARGET_PORT))

    server_sock.listen(1)

    conn,addr = server_sock.accept()

    print 'Server connected by: ', addr

    while True:
        try: 
            data = conn.recv(1024)
            if not data: break
            print data
            
        except KeyboardInterrupt: #Ctrl-C 
            print "\nUser has closed the script."
            break
        
        except EOFError: # Ctrl-Z
            print "\nUser has closed the script."
            break


    conn.close()
    print "Closed Connected"

if __name__ == "__main__":
    ServerConnect()

    


