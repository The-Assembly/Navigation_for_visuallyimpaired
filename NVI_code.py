import RPi.GPIO as GPIO
import time
from gtts import gTTS
import os
##import threading
#import pyttsx
#engine = pyttsx.init()
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17
TRIG2 = 24
ECHO2 =23
TRIG3 = 5
ECHO3 = 25
#GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
motor1 = 14
motor2 = 15
motor3 = 26
GPIO.setmode(GPIO.BCM)
#while 1:
GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(motor2,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(motor3,GPIO.OUT)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)

tts = gTTS(text='Obstacle on the left, Turn right', lang='en')
tts.save("right.mp3")

tts = gTTS(text='Obstacle on the right,Turn left', lang='en')
tts.save("left.mp3")




def distanceMEasurement(TRIG,ECHO):
    
    #print "Distance Measurement In Progress"
    
    #print "Waiting For Sensor To Settle"
    

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start


    distance = pulse_duration * 17150


    distance = round(distance, 2)
    return distance

##def ultrasonic_1():
##    try:
##        while True:
##            #time.sleep(2)
##            distanceFound = distanceMEasurement(TRIG,ECHO)
##            #print "Distance 1:",distanceFound,"cm"
##            if distanceFound <= 10:
##                GPIO.output(motor1,GPIO.HIGH)
##                time.sleep(0.5)
##                GPIO.output(motor1,GPIO.LOW)
####            else:
####                GPIO.output(motor1,GPIO.LOW)
##    except KeyboardInterrupt:
##        print "Stopped"
##        GPIO.cleanup()
##
##def ultrasonic_2():
##    try:
##        while True:
##            #time.sleep(2)
##            distanceFound2 = distanceMEasurement(TRIG2,ECHO2)
##            #print "Distance 2:",distanceFound2,"cm"
##            if distanceFound2 <= 10:
##                GPIO.output(motor2,GPIO.HIGH)
##                time.sleep(0.5)
##                GPIO.output(motor2,GPIO.LOW)
####            else:
####                GPIO.output(motor2,GPIO.LOW)
##    except KeyboardInterrupt:
##        print "Stopped"
##        GPIO.cleanup
##     
##
##def ultrasonic_3():
##    try:
##        while True:
##            #time.sleep(2)
##            distanceFound3 = distanceMEasurement(TRIG3,ECHO3)
##            #print "Distance 3:",distanceFound3,"cm"
##            if distanceFound3 <= 10:
##                GPIO.output(motor3,GPIO.HIGH)
##                time.sleep(0.5)
##                GPIO.output(motor3,GPIO.LOW)
####            else:
####                GPIO.output(motor3,GPIO.LOW)
##    except KeyboardInterrupt:
##        print "Stopped"
##        GPIO.output(motor1,GPIO.LOW)
##        GPIO.output(motor2,GPIO.LOW)
##        GPIO.output(motor3,GPIO.LOW)
##        GPIO.cleanup()
##    
##            
##            

try:
    while True:
       
        distanceFound = distanceMEasurement(TRIG,ECHO)
        distanceFound2 = distanceMEasurement(TRIG2,ECHO2)
        distanceFound3 = distanceMEasurement(TRIG3,ECHO3)
##        print "Distance1:",distanceFound,"cm"
##        if distanceFound <= 10:
##            GPIO.output(motor1,GPIO.HIGH)
##            time.sleep(0.5)
##            GPIO.output(motor1,GPIO.LOW)
##        
##
##        print "Distance2:",distanceFound2,"cm"
##        if distanceFound2 <= 10:
##            GPIO.output(motor2,GPIO.HIGH)
##            time.sleep(0.5)
##            GPIO.output(motor2,GPIO.LOW)
##
##        
##        print "Distance3:",distanceFound3,"cm"
##        if distanceFound3 <= 10:
##            GPIO.output(motor3,GPIO.HIGH)
##            time.sleep(0.5)
##            GPIO.output(motor3,GPIO.LOW)

        if(distanceFound <10 and distanceFound2 <10):
            os.system("omxplayer right.mp3")
            GPIO.output(motor3,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(motor3,GPIO.LOW)
            print "Distance2:",distanceFound2,"cm"

        if(distanceFound <10 and distanceFound3 <10):
            os.system("omxplayer left.mp3")
            GPIO.output(motor2,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(motor2,GPIO.LOW)
            print "Distance3:",distanceFound3,"cm"
except KeyboardInterrupt:
    print "Stopped"
    GPIO.output(motor1,GPIO.LOW)
    GPIO.output(motor2,GPIO.LOW)
    GPIO.output(motor3,GPIO.LOW)
    GPIO.cleanup()

##if __name__=='__main__':
##    t1 = threading.Thread(target=ultrasonic_1)
##    t2 = threading.Thread(target=ultrasonic_2)
##    t3 = threading.Thread(target=ultrasonic_3)
##    
##    t1.start()
##    t2.start()
##    t3.start()
##    


