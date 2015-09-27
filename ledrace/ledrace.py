import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)



count = 3
print count

# endless loop, on/off for 1 second
while count > 0:
    GPIO.output(17,False)
    time.sleep(1)
    GPIO.output(17,True)
    time.sleep(1)
    count = count -1
    print count

else:
    print "GO!"
    GPIO.output(4,False)
    time.sleep(3)
    GPIO.output(4,True)
    
