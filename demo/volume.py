

import smbus2
import time

def getad():
    bus = smbus2.SMBus(1)
    time.sleep(2)
    data = bus.read_byte_data(0x2a, 0x00)
#    print(data)
    return data
    

