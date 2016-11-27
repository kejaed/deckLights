import serial
import sys

ser = serial.Serial('/dev/ttyACM0',57600,timeout=5)

# have a readline here to wait for the arduino to write "---SETUP COMPLETE---" 
# before we continue with the program
# note that the arduino will be reset each time we connect
# can this action be turned off?

hello = ser.readline()

print(hello)

ser.write(b'm0')
ser.close()
