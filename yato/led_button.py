
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(21, GPIO.IN) 
 
try:
    while True:
        if GPIO.input(21) == GPIO.HIGH:
            GPIO.output(4, GPIO.HIGH)
        else:
            GPIO.output(4, GPIO.LOW)
 
except KeyboardInterrupt:
    pass
 
GPIO.cleanup() 
