import serial
from time import sleep
from energenie import switch_on, switch_off
import random

connected = False

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=3.0)
ser.write("1")
sleep(1)

sockets = [1, 2, 3, 4]


while True:
    scoreString = input("Enter number:  ")
    scorePrint = "%03d" %scoreString
    # "{0:0=3d}".format(scoreString)
    print "input %s" %scorePrint
    ser.write(str(scorePrint))
    score = int(float(scoreString))
    print score
    switch_off(0)
    random.shuffle(sockets) # sockets is now e.g [4, 2, 1, 3]
    sockets_1 = sockets[:1] # sockets_1 is now [4]

    random.shuffle(sockets) # sockets is now e.g [2, 4, 3, 1]
    sockets_2 = sockets[:2] # sockets_2 is now [2, 4]

    random.shuffle(sockets) # sockets is now e.g [3, 1, 2, 4]
    sockets_3 = sockets[:3] # sockets_3 is now [3, 1, 2]

    if score <= 25:
        print "Turn on 1 light"
        for socket in sockets_1:
            switch_on(socket)
            print "socket %d" % socket

    if score >= 26 and score <= 50:
        print "Turn on 2 lights"
        for socket in sockets_2:
            switch_on(socket)
            sleep(1)
            print "socket %d" % socket

    if score >= 51 and score <= 75:
        print "Turn on 3 lights"
        for socket in sockets_3:
            switch_on(socket)
            sleep(1)
            print "socket %d" % socket

    if score >= 76:
        print "Turn on 4 lights"
        switch_on(0)
    sleep(15)
    switch_on(0)




## close the port and end the program
ser.close()
