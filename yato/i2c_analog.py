
"""
i2c test
use attiny85
"""

import smbus2
import time

bus = smbus2.SMBus(1)

try:
	while True:
		data = bus.read_byte_data(0x2a, 0x00)
		print(data)
		time.sleep(0.5)
except KeyboardInterrupt:
	pass
