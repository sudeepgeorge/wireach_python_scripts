#This script is used along with SendSerial.py . It is used to read the data that is sent over
#serial port by the WiReach module and displays it to the user.


import os
import serial
import sys
import time

#http://pyserial.wiki.sourceforge.net/pySerial
#http://pyserial.svn.sourceforge.net/viewvc/pyserial/

# Windows - master_port=serial.Serial(8)
master_port=serial.Serial('/dev/ttyS0')
master_port.open()


while True:
    try:
        #read_size = master_port.inWaiting()
        #sys.stdout.flush()
        response = master_port.read(1)
        sys.stdout.write(response) # This avoids the insertion of \n or ' ' by print command.
        

    except KeyboardInterrupt: #Ctrl-C 
        print "\nUser has closed the script."
        break
      
    except EOFError: # Ctrl-Z
        print "\nUser has closed the script."
        break
 

master_port.close()

    