import os
import serial
import sys
import time

#This Python script is used to set up the SerialNet mode. Should be called once on WiReach boot-up.
#Be aware that once in SerialNet mode, it would persist across power-cycles and requires an escape
#sequence '+++' to get out.

#Settings being used for SerialNet Parameters:

#HSRV = 172.16.0.227:39999
#LPRT = 39998
#MBTB = 1024
#MTTF = 1000
#MCBF = 25
#AWS  = 1
#Everything else remains as the default.

#http://pyserial.wiki.sourceforge.net/pySerial
#http://pyserial.svn.sourceforge.net/viewvc/pyserial/

# Windows - master_port=serial.Serial(8)
master_port=serial.Serial('/dev/ttyS0')
master_port.open()

master_port.write('AT+i\r\n')
response = master_port.read(10)
print response, len(response)


master_port.write('AT+iUP\r\n')
response = master_port.read(20)
print response, len(response)

time.sleep(2)

master_port.write('AT+iHIF=1\r\n')
response = master_port.read(20)
print response, len(response)

master_port.write('AT+iSNMD=3\r\n')
response = master_port.read(20)
print response, len(response)

time.sleep(3)


master_port.close()
sys.exit(0)

