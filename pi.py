import serial
import time


## open the serial port that your ardiono
## is connected to.
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=3.0)

ser.write("1")

scoreString = input("Enter number:  ")

ser.write("%s" % scoreString)

## close the port and end the program
ser.close()

