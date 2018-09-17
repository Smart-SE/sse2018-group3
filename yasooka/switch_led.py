
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN) 
 
try:
    while True:
        if GPIO.input(24) == GPIO.HIGH:
            GPIO.output(23, GPIO.HIGH)
        else:
            GPIO.output(23, GPIO.LOW)
        time.sleep(0.5)
 
except KeyboardInterrupt:
    pass
 
GPIO.cleanup() 
