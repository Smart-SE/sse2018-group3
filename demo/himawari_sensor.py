
import heartbeat
import volume

import RPi.GPIO as GPIO
import time
import json
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

sensor = { "data":0, "hist":[0,0,0,0,0,0,0,0,0,0] }

try:
    while True:
        if GPIO.input(21) == GPIO.HIGH:
            GPIO.output(4, GPIO.HIGH)
            data = volume.getad()
            data = data * 255 / 166
            
        else:
            GPIO.output(4, GPIO.LOW)
            data = heartbeat.get_heartbeat()
            data = data * 255 / 120
        
        if data < 0 :
            data = 0
        elif data > 255:
            data = 255
        data = int(data)
        sensor["data"] = data
        sensor["hist"].pop(0)
        sensor["hist"].append(data)
        jfile = open("sensor.json","w")
        json.dump(sensor,jfile)
        jfile.close()
        print( sensor )
 
except KeyboardInterrupt:
    pass
 

GPIO.cleanup()


