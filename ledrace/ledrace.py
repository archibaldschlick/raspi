import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT)
	GPIO.setup(17, GPIO.OUT)

def loop():
	count = 3
	print count
	while count > 0:
  	 	GPIO.output(17,False)
		time.sleep(1)
    	GPIO.output(17,True)
    	time.sleep(1)
    	count = count -1
    	print count
	#else:
    	print "GO!"
    	GPIO.output(4,False)
    	time.sleep(3)
    	GPIO.output(4,True)
def destroy():
	GPIO.output(4,False)
	GPIO.output(17,True)
	GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()