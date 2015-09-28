#!/usr/bin/env python
import RPi.GPIO as GPIO

buttonPin = 13
ledGreenPin = 11
ledRedPin = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledGreenPin, GPIO.OUT)
	GPIO.setup(ledRedPin, GPIO.OUT)
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(ledGreenPin, GPIO.HIGH)
	GPIO.output(ledRedPin, GPIO.HIGH)
def loop():
	while True: 
		if GPIO.input(buttonPin) == GPIO.LOW:
		   print '...red led on'
		   GPIO.output(ledRedPin, GPIO.LOW)
		   GPIO.output(ledGreenPin, GPIO.HIGH)
		else: 
			print 'green led on...'
			GPIO.output(ledGreenPin, GPIO.LOW)
			GPIO.output(ledRedPin, GPIO.HIGH)

def destroy():
	GPIO.output(ledGreenPin, GPIO.HIGH)
	GPIO.output(ledRedPin, GPIO.HIGH)
	GPIO.cleanup()

if __name__ == '__main__':    
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
