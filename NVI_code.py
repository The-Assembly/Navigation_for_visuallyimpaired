import RPi.GPIO as GPIO
import time
from gtts import gTTS
import os
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17
##

##

motor1 = 14
##

##

GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
##

##

tts = gTTS(text='Turn right', lang='en')
tts.save("right.mp3")

##
##


##


def distanceMEasurement(TRIG,ECHO):
    
    ##
    time.sleep(0.00001)
    ##

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    return distance           

try:
    while True:
       
        distanceFound = distanceMEasurement(TRIG,ECHO)
        ##
        ##

        if(distanceFound <10 and distanceFound2 <10): ## Tells the user to turn right when an obstacle is detected on the left
            os.system("omxplayer right.mp3")
            GPIO.output(motor3,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(motor3,GPIO.LOW)
            print "Distance2:",distanceFound2,"cm"

        if(distanceFound <10 and distanceFound3 <10): ## Tells the user to turn left when an obstacle is detected on the right
            os.system("omxplayer left.mp3")
            ##
            time.sleep(0.5)
            ##
            print "Distance3:",distanceFound3,"cm"
except KeyboardInterrupt:
    print "Stopped"
    GPIO.output(motor1,GPIO.LOW)
	##
	##
    GPIO.cleanup()
