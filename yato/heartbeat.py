
import numpy as np
import matplotlib.pyplot as plt
import smbus2
import time

bus = smbus2.SMBus(1)

heartbeat = []

for i in range(100):
	data = bus.read_i2c_block_data(0x2a, 0x00, 2)
	#print(data)
	heartbeat += [data[1]]
	time.sleep(0.02)

#print(heartbeat)

plt.plot(heartbeat)
plt.savefig("heartbeat.png")


