#This script is used along with HostServer.py . This script is used to read data from the console,
#send it over the serial port to the WiReach which in turn sends its to the remote host.


import os
import serial
import sys

#http://pyserial.wiki.sourceforge.net/pySerial
#http://pyserial.svn.sourceforge.net/viewvc/pyserial/

# Windows - master_port=serial.Serial(8)
master_port=serial.Serial('/dev/ttyS0')
master_port.open()

while True:
    try:
        valStr = raw_input("\n[SerialNet]# ")
        if valStr == 'exit':
            break

        master_port.write(valStr)

    except KeyboardInterrupt: #Ctrl-C 
        print "\nUser has closed the script."
        break
      
    except EOFError: # Ctrl-Z
        print "\nUser has closed the script."
        break
 
        

#master_port.write('This is a test string to demonstrate that data sent over a serial port is transferred to to remote IP host\r\n')


master_port.close()
sys.exit(0)