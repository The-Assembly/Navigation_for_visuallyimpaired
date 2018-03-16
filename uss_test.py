import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 11

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,1)
#time.sleep(0.00001)
GPIO.output(TRIG,0)


while True:
    
        #print("tt")
          GPIO.output(TRIG, False)                 #Set TRIG as LOW
        ##print ("Waitng For Sensor To Settle")
          #sleep(2)                       #Delay of 2 seconds

          GPIO.output(TRIG, True)                  #Set TRIG as HIGH
          sleep(0.00001)                      #Delay of 0.00001 seconds
          GPIO.output(TRIG, False)                 #Set TRIG as LOW

          while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()              #Saves the last known time of LOW pulse
            #print("0")
            
          while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse 
            #print("1")

          pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

          distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
          distance = round(distance, 2)            #Round to two distances
          print (distance)
          sleep(0.5)

             
