import serial
from time import sleep
from energenie import switch_on, switch_off
import random

connected = False

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=3.0)
ser.write("1")
sleep(1)

sockets = list(range(4))
random.shuffle(sockets)


threeSockets = sockets.pop()
twoSockets = threeSockets.pop()
oneSockets = twoSocket.pop()


while True:
    scoreString = input("Enter number:  ")
        ser.write("%s" % scoreString)
        score = int(float(scoreString))
        print score

        if score <= 2:
            print "Turn on 1 light"
                for socket in onesockets:
                switch_on(socket)
                print socket
            
        if score >= 3 and score <= 4:
            print "Turn on 2 lights"
            for socket in twosockets:
                switch_on(socket)
                print socket

        if score >= 5 and score <= 7:
            print "Turn on 3 lights"
            for socket in threesockets:
                switch_on(socket)
                print socket

        if score >= 8:
            print "Turn on 4 lights"
            switch_on(0)




## close the port and end the program
ser.close()