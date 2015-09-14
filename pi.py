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
    ser.write("%s" % scoreString)
    score = int(float(scoreString))
    print score
    
    random.shuffle(sockets) # sockets is now e.g [4, 2, 1, 3]
    sockets_1 = sockets[:1] # sockets_1 is now [4]
    
    random.shuffle(sockets) # sockets is now e.g [2, 4, 3, 1]
    sockets_2 = sockets[:2] # sockets_2 is now [2, 4]
    
    random.shuffle(sockets) # sockets is now e.g [3, 1, 2, 4]
    sockets_3 = sockets[:3] # sockets_3 is now [3, 1, 2]

    if score <= 2:
        print "Turn on 1 light"
        for socket in sockets_1:
            switch_on(socket)
            print socket

    if score >= 3 and score <= 4:
        print "Turn on 2 lights"
        for socket in sockets_2:
            switch_on(socket)
            print socket

    if score >= 5 and score <= 7:
        print "Turn on 3 lights"
        for socket in sockets_3:
            switch_on(socket)
            print socket

    if score >= 8:
        print "Turn on 4 lights"
        switch_on(0)




## close the port and end the program
ser.close()

