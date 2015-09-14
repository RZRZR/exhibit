## import the serial library
import serial
from time import sleep
from energenie import switch_on, switch_off

## Boolean variable that will represent
## whether or not the arduino is connected
connected = False

## open the serial port that your ardiono
## is connected to.

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=3.0)
ser.write("1")
sleep(1)

while True:
    scoreString = input("Enter number:  ")
        ser.write("%s" % scoreString)
        score = int(float(scoreString))
        print score
        if score <= 2:
            switch_on(1)
                print "Turn on 1 light"
        if score >= 3 and score <= 4:
            switch_on(1)
                switch_on(2)
                print "Turn on 2 lights"
        if score >= 5 and score <= 7:
            switch_on(1)
                switch_on(2)
                switch_on(3)
                print "Turn on 3 lights"
        if score >= 8:
            switch_on(1)
                switch_on(2)
                switch_on(3)
                switch_on(4)
                print "Turn on 4 lights"




## close the port and end the program
ser.close()

