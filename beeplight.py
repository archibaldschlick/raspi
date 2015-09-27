#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import random


BeepPin = 11
Red = 18
Yellow = 22
Green = 32
ls = [11,18,22,32]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
for i in ls:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,True)

count = 10
sound = 1

while True:    
    if __name__ == '__main__':     # Program start from here

        if count > 7:
            GPIO.output(BeepPin, GPIO.LOW)
            GPIO.output(Red, False)
            time.sleep(sound)
            GPIO.output(BeepPin, GPIO.HIGH)
            GPIO.output(Red, True)
	    time.sleep(0.5)
	    sound = sound-0.1
            print count
            count -= 1
        elif count>4:
    	    GPIO.output(BeepPin, GPIO.LOW)
            GPIO.output(Yellow, False)
	    time.sleep(sound)
    	    GPIO.output(BeepPin, GPIO.HIGH)
	    GPIO.output(Yellow, True)
	    time.sleep(0.5)
	    print count
            count = count -1
	    sound = sound-0.1
        else:
            if count >0:
                GPIO.output(BeepPin, GPIO.LOW)
                GPIO.output(Green, False)
	        time.sleep(sound)
    	        GPIO.output(BeepPin, GPIO.HIGH)
	        GPIO.output(Green, True)
	        time.sleep(0.5)
	        count -= 1
	        sound = sound-0.1
                print count
            else:
                GPIO.output(Green,False)
                time.sleep(3)
                break
    else:
        GPIO.output(11,True)
        GPIO.cleanup()
        
  
