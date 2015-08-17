import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18,GPIO.IN)

# input of the switch will change the state of the LED
while True:
    GPIO.output(17,GPIO.input(18))
    time.sleep(1.05)
