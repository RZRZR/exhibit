import serial
from time import sleep
from energenie import switch_on, switch_off
import random

<<<<<<< HEAD
ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=3.0) # Arduino controlling DOTSTAR
ser2 = serial.Serial("/dev/ttyACM0", 9600) # Arduino reading 16 POTs
=======
connected = False

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=3.0) # Arduino controlling DOTSTAR
ser2 = serial.Serial("/dev/ttyACM0", 9600, timeout=3.0) # Arduino reading 16 POTs
>>>>>>> FETCH_HEAD
ser.write("1")
ser2.write("1")
sleep(1)

sockets = [1, 2, 3, 4]



def shuffle():
    random.shuffle(sockets) # sockets is now e.g [4, 2, 1, 3]
    sockets_1 = sockets[:1] # sockets_1 is now [4]

    random.shuffle(sockets) # sockets is now e.g [2, 4, 3, 1]
    sockets_2 = sockets[:2] # sockets_2 is now [2, 4]

    random.shuffle(sockets) # sockets is now e.g [3, 1, 2, 4]
    sockets_3 = sockets[:3] # sockets_3 is now [3, 1, 2]

<<<<<<< HEAD
while True:

    # Enter a number between 0 - 100 - turn it into a 3 digit number.
    #scoreString = input("Enter number:  ")

    # if button is pressed

    # Read score from Arduino 2

    print "Reading arduino 2"

    ser2.write("1")
    reading = ser2.readline()
    sleep(1)
    print reading

    scoreString = int(reading)

    scoreThreeDigit = "%03d" %scoreString
    print "input %s" %scoreThreeDigit


    print "Sending to arduino 1"


    # Send score to Arduino 1 as a 3 digit string
    ser.write(str(scoreThreeDigit))

    # Print score as a int
    score = int(float(scoreString))
    print score

    #
    random.shuffle(sockets) # sockets is now e.g [4, 2, 1, 3]
    sockets_1 = sockets[:1] # sockets_1 is now [4]

    random.shuffle(sockets) # sockets is now e.g [2, 4, 3, 1]
    sockets_2 = sockets[:2] # sockets_2 is now [2, 4]

    random.shuffle(sockets) # sockets is now e.g [3, 1, 2, 4]
    sockets_3 = sockets[:3] # sockets_3 is now [3, 1, 2]


=======
    return;


while True:

    # Enter a number between 0 - 100 - turn it into a 3 digit number.
    scoreString = input("Enter number:  ")
    scoreThreeDigit = "%03d" %scoreString
    print "input %s" %scoreThreeDigit

    # if button is pressed

    # Read score from Arduino 2



    # Send score to Arduino 1 as a string
    ser.write(str(scoreThreeDigit))

    # Print score as a int
    score = int(float(scoreString))
    print score

    #
    shuffle()


>>>>>>> FETCH_HEAD
    if score <= 25:
        print "Turn on 1 light"
        for socket in sockets_1:
            switch_on(socket)
            print "socket %d" % socket

<<<<<<< HEAD
    if score >= 26 and score <= 50:
        print "Turn on 2 lights"
=======
if score >= 26 and score <= 50:
    print "Turn on 2 lights"
>>>>>>> FETCH_HEAD
        for socket in sockets_2:
            switch_on(socket)
            print "socket %d" % socket

<<<<<<< HEAD
    if score >= 51 and score <= 75:
        print "Turn on 3 lights"
=======
if score >= 51 and score <= 75:
    print "Turn on 3 lights"
>>>>>>> FETCH_HEAD
        for socket in sockets_3:
            switch_on(socket)
            print "socket %d" % socket

<<<<<<< HEAD
    if score >= 76:
        print "Turn on 4 lights"
        switch_on(0)
        sleep(5)
=======
if score >= 76:
    print "Turn on 4 lights"
        switch_on(0)
    sleep(5)
>>>>>>> FETCH_HEAD

    sleep (2)

## close the port and end the program
ser.close()
