#This script is used along with RecvSerial.py . This script will read the data entered into the console,
#send it over IP to the WiReach module.


import os
import sys
import socket

REMOTE_IP = '172.16.0.200'
REMOTE_PORT = 39998

def SerialConnect():
    server_sock=0
    connect_result=0
    try:
      serial_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except:
      print "Creating a socket failed."
      return 0

    connect_result=serial_sock.connect((REMOTE_IP,REMOTE_PORT))


    while True:
        try:
            valStr = raw_input("\n[SerialNet]# ")
            if valStr == 'exit':
                break

            serial_sock.send(valStr)
            serial_sock.send('\r\n')

        except KeyboardInterrupt: #Ctrl-C 
            print "\nUser has closed the script."
            break
        
        except EOFError: # Ctrl-Z
            print "\nUser has closed the script."
            break
    

#    serial_sock.send("This is a test string that is being sent to demonstrate that data sent from a remote IP is delivered to the serial device.\r\n") 

    serial_sock.close()
   
    print "Closed Connected"

if __name__ == "__main__":
    SerialConnect()