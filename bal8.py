import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

l = [4,16,12,23,5,27,18,17]
x = range(10)
count = 10
for i in l:
    GPIO.setup(i, GPIO.OUT)
print "In drei Sekunden oder spaeter"
time.sleep(3)

for k in x:
    if GPIO.input(21) == False:
            for i in l:
                GPIO.output(i,False)
                time.sleep(0.05)    
                GPIO.output(i,True)
            
            for i in reversed(l):
                GPIO.output(i,False)
                time.sleep(0.1)
                GPIO.output(i,True)
	    count = count -1
            print count
    else:
        count = count-1
        print count
        time.sleep(1)


