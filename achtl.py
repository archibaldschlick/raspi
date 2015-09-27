import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

l = [4,16,12,23,5,27,18,17]
count = 30
for i in l:
    GPIO.setup(i, GPIO.OUT)

while count>0:
        for i in l:
            GPIO.output(i,False)
            time.sleep(0.05)    
            GPIO.output(i,True)
            
        for i in reversed(l):
            GPIO.output(i,False)
            time.sleep(0.1)
            GPIO.output(i,True)
	count = count -1		

